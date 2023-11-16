import asyncio
import inspect
import itertools
import os
import random
import time
import math
from datetime import datetime
from pprint import pformat
from pathlib import Path
from typing import Callable, Union, List

from AioSpider import logger, pretty_table, tools
from AioSpider.constants import SleepStrategy, MiddlewareType, SignalType, BackendEngine
from AioSpider.exceptions import *
from AioSpider.http import Response, BaseRequest
from AioSpider.loading import BootLoader
from AioSpider.models import Model
from AioSpider.signal import Signal
from AioSpider.db import RedisLock

from .patch import apply
from .concurrency_strategy import get_task_limit


apply()


class EngineBuilder:

    def __init__(self, engine, spider):
        self.bootloader = BootLoader()
        self.engine = engine
        self.spider = spider

    async def build(self):
        await self._load_settings()
        await self._load_logger()
        await self._load_welcome()
        await self._load_notice()
        await self._load_connection()
        await self._load_model()
        await self._load_request_pool()
        await self._load_browser()
        await self._load_middleware_manager()
        await self._load_downloader()
        await self._load_datamanage()

    async def _load_settings(self):
        self.engine.settings = self.bootloader.reload_settings(self.spider)

    async def _load_logger(self):
        self.bootloader.reload_logger(self.spider.name, self.engine.settings)

    async def _load_welcome(self):
        words = """
*------------------------------------------------------------------------------------------------------------------------------------------------*
|             __        __   _                                      _                  _    _      ____        _     _                           |
|             \ \      / /__| | ___ ___  _ __ ___   ___          _ | |_ ___           / \  (_) ___/ ___| _ __ (_) __| | ___ _ __                 |
|              \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \        |_  __/ _ \          / _ \ | |/ _ \___ \| '_ \| |/ _` |/ _ \ '__|                |
|               \ V  V /  __/ | (_| (_) | | | | | |  __/          | || (_) |        / ___ \| | (_) |__) | |_) | | (_| |  __/ |                   |
|                \_/\_/ \___|_|\___\___/|_| |_| |_|\___|           \__\___/        /_/   \_\_|\___/____/| .__/|_|\__,_|\___|_|                   |
|                                                                                                       |_|                                      |
*------------------------------------------------------------------------------------------------------------------------------------------------*
            """
        print(words)
        logger.info(f'{">" * 25} {self.spider.name}: 开始采集 {"<" * 25}')

    async def _load_notice(self):
        self.bootloader.reload_notice(self.spider.name, self.engine.settings)

    async def _load_connection(self):
        self.engine.connections = await self.bootloader.reload_connection(self.engine.settings)

    async def _load_model(self):
        self.engine.models = self.bootloader.reload_models(self.spider, self.engine.settings)

    async def _load_request_pool(self):
        from AioSpider.requestpool import RequestPool
        self.engine.request_pool = await RequestPool(
            self.spider, self.engine.settings, self.engine.connections, self.engine.backend
        )

    async def _load_browser(self):
        self.engine.browser = self.bootloader.reload_browser(self.engine.settings)

    async def _load_middleware_manager(self):
        self.engine.middleware_manager = self.bootloader.reload_middleware_manager(
            self.spider, self.engine.settings, self.engine.browser
        )

    async def _load_downloader(self):
        from AioSpider.downloader import Downloader
        self.engine.downloader = Downloader(
            request_config=self.engine.settings.SpiderRequestConfig,
            pool_config=self.engine.settings.ConnectPoolConfig,
            middleware=self.engine.middleware_manager.download_middlewares
        )

    async def _load_datamanage(self):
        from AioSpider.datamanager import DataManager

        data_manager = await DataManager(self.engine.settings, self.engine.connections, self.engine.models)
        self.engine.datamanager = EngineDataManagement(self.spider, self.engine.request_buffer, data_manager)
        logger.info(
            f'数据管理器已启动，加载到 {len(data_manager.models)} 个模型，\n{pformat(data_manager.models)}'
        )


class EngineDataManagement:

    def __init__(self, spider, queue, datamanager):
        self.spider = spider
        self.request_buffer = queue
        self.datamanager = datamanager

    async def process_response(self, response, request):
        """处理响应"""

        def get_callback_func(spider, request):
            callback = request.callback or spider.parse or spider.default_parse
            return getattr(spider, callback, None) if isinstance(callback, str) else callback

        callback = get_callback_func(self.spider, request)

        if not callable(callback):
            raise TypeError(f'回调必须是可调用类型')

        args = []
        for k in inspect.signature(callback).parameters:
            if k == 'self':
                args.append(self.spider)
            elif k == 'response':
                args.append(response)
            else:
                args.append(None)

        result = callback(*args)

        await self._process_callback(result, response.request.depth)

    async def _process_callback(self, result, depth):
        """处理响应回调结果"""

        if result is None or isinstance(result, Path):
            return

        if isinstance(result, Model):
            if result.source is None:
                result.source = self.spider.source
            await self._process_callback(await self.datamanager.commit(result), depth)
        elif isinstance(result, BaseRequest):
            result.depth = depth
            self.request_buffer.put(result)
        elif hasattr(result, '__iter__'):
            for item in result:
                await self._process_callback(item, depth)
        else:
            raise ValueError('回调必须返回Model对象或BaseRequest对象')

    async def close(self):
        await self.datamanager.close()
        

class BaseEngine:

    def __init__(self, spider):

        self.spider = spider
        self.settings = None
        self.models = None
        self.request_pool = None
        self.middleware_manager = None
        self.downloader = None
        self.connections = None
        self.datamanager = None
        self.browser = None
        self.slot = None

        # 开始事件循环
        self.loop = asyncio.get_event_loop()
        self.request_buffer = self.init_queue()

        self.start_time = datetime.now()
        self.crawing_time = 0
        self._per_request_sleep = None
        self._per_task_sleep = None
        self.avg_speed = 0
        self.task_limit = 1
        self.waiting_count = 0

    def start(self):
        """启动引擎"""

        try:
            # 将协程注册到事件循环中
            self.loop.run_until_complete(self.execute())
        except KeyboardInterrupt:
            self.loop.run_until_complete(self.close())
            logger.error('手动退出')
        except ValueError as e:
            logger.exception(e)
        except SystemConfigError as e:
            logger.error(e)
        # except BaseException as e:
        #     self.loop.run_until_complete(self.request_pool.close())
        #     logger.error(f'异常退出：原因：{e}')
        except Exception as e:
            raise e
        finally:
            self.loop.run_until_complete(self.loop.shutdown_asyncgens())

    async def execute(self):
        """ 执行初始化start_urls里面的请求 """
        await EngineBuilder(self, self.spider).build()
        await Signal().emit(SignalType.spider_open)
        
    @property
    def task_sleep(self):
        if self._per_task_sleep is None:
            sleep_config = self.settings.SpiderRequestConfig.REQUEST_CONCURRENCY_SLEEP
            if sleep_config['strategy'] == SleepStrategy.fixed:
                self._per_task_sleep = sleep_config['sleep']
            elif sleep_config['strategy'] == SleepStrategy.random:
                self._per_task_sleep = random.randint(
                    min(sleep_config['sleep']) * 100, max(sleep_config['sleep']) * 100
                ) / 100
            else:
                self._per_task_sleep = 1
        return self._per_task_sleep

    @property
    def request_sleep(self):
        if self._per_request_sleep is None:
            sleep_config = self.settings.SpiderRequestConfig.PER_REQUEST_SLEEP
            if sleep_config['strategy'] == SleepStrategy.fixed:
                self._per_request_sleep = sleep_config['sleep']
            elif sleep_config['strategy'] == SleepStrategy.random:
                self._per_request_sleep = random.randint(
                    min(sleep_config['sleep']) * 100, max(sleep_config['sleep']) * 100
                ) / 100
            else:
                self._per_request_sleep = 1
        return self._per_request_sleep

    async def apply_task_sleep(self):
        await asyncio.sleep(self.task_sleep)

    async def apply_request_sleep(self):
        await asyncio.sleep(self.request_sleep)

    async def request_pool_empty(self):
        return True if self.request_pool.pending_empty() and await self.request_pool.waiting_empty() and \
                       await self.request_pool.failure_empty() else False

    async def download(self, request):
        """从调度器中取出的请求交给下载器中处理"""

        async def process_middleware_response(self, response):

            if response is None:
                logger.warning(f'请求异常，系统将该请求添加到 failure 队列 {request}')
                await self.request_pool.push_to_failure(request)
                return None

            if isinstance(response, Response):
                await self.request_pool.set_status(response)
                return response

            if isinstance(response, BaseRequest):
                self.request_buffer.put(response)
                return None

            return None

        response = await self.downloader.fetch(request)
        await self.request_pool.pending.remove_request(request)

        if isinstance(response, Response):
            response = await self.middleware_manager.process_response(response)
            return await process_middleware_response(self, response)

        if isinstance(response, Exception):
            response = await self.middleware_manager.process_exception(request, response)
            return await process_middleware_response(self, response)
        
        raise TypeError('Respinse 类型错误')

    def format_running_time(self, running):

        hour, remainder = divmod(running, 3600)
        minute, second = divmod(remainder, 60)

        s = f'{int(hour)}时' if hour else ''
        s += f'{int(minute)}分' if minute else ''

        s += f'{int(second)}秒'

        return s

    def format_remaining_time(self, remaining):

        hour, remainder = divmod(remaining, 3600)
        minute, second = divmod(remainder, 60)

        s = f'{int(hour)}时' if hour else ''
        s += f'{int(minute)}分' if minute else ''

        s += f'{int(second)}秒'

        return s
    
    def get_concurrency_type(self):
        
        config = self.settings.ConcurrencyStrategyConfig
        
        if config.auto['enabled']:
            return '自动并发模式'
        elif config.fix['enabled']:
            return '固定并发模式'
        elif config.random['enabled']:
            return '随机并发模式'
        elif config.speed['enabled']:
            return '速度并发模式'
        elif config.time['enabled']:
            return '时间并发模式'
        else:
            raise

    async def close(self):

        completed_count = await self.request_pool.done_size()
        failure_count = self.request_pool.failure_size()
        running = round(time.time() - self.crawing_time, 3)
        speed = round(completed_count / running, 3) if running else 0

        item = [{
            "完成数量": completed_count, "失败数量": failure_count, "运行时间": running,
            '并发速度': speed, '完成进度': '100%'
        }]
        logger.info(f'爬取结束，总请求详情：\n{pretty_table(item)}')

        await Signal().emit(SignalType.browser_quit)
        await Signal().emit(SignalType.request_close)
        await Signal().emit(SignalType.session_close)
        await Signal().emit(SignalType.database_close)

        logger.info(f'{">" * 25} {self.spider.name}: 采集结束 {"<" * 25}')
        logger.info(f'{">" * 25} 总共用时: {datetime.now() - self.start_time} {"<" * 25}')

    async def spider_close(self):

        for model in self.models:
            model.verify(model)

        await Signal().emit(SignalType.spider_close)


class Engine(BaseEngine):

    backend = BackendEngine.queue
    
    def init_queue(self):
        # if self.backend == BackendEngine.queue:
        from .task_queue import Queue
        return Queue()
        # elif self.backend == BackendEngine.redis:
        #     from .task_queue import RedisQueue
        #     return RedisQueue()
        # else:
        #     raise

    async def execute(self):

        await super(Engine, self).execute()

        self.start_requests_iterator = self.spider.start_requests()

        # 如果start_requests_iterator已用完，则添加要跟踪的变量
        iterator_stop = False
        self.crawing_time = time.time()
        concurrency_type = self.get_concurrency_type()

        # 连续循环，从调度程序队列中获取请求
        while True:

            self.task_limit = get_task_limit(
                config=self.settings.ConcurrencyStrategyConfig,
                crawing_time=self.crawing_time,
                current_speed=self.avg_speed,
                task_limit=self.task_limit,
                waiting_count=self.waiting_count
            )
            logger.debug(f'并发类型：{concurrency_type}，当前并发数：{self.task_limit}')

            if self.task_limit <= 0:
                raise ValueError('Task limit 必须大于0')

            # 将 start_requests 生成的请求添加到 request_buffer
            iterator_stop = await self.determine_start_request_left(iterator_stop)

            # 将请求添加到waiting队列
            await self.push_request_to_waiting()

            # 处理waiting队列中的请求
            tasks = await self.process_waiting_requests()
            await self.process_tasks(tasks)
            await self.fresh_progress()

            # 暂停以遵循请求速率限制，更新进度条
            await self.apply_task_sleep()

            # 如果没有请求需要处理，则中断循环
            if iterator_stop and self.request_buffer.empty() and await self.request_pool_empty():
                break

        await self.datamanager.close()
        await self.spider_close()
        await self.close()

    async def determine_start_request_left(self, iterator_stop):
        """判断start_requests是否还有请求"""

        if not iterator_stop:
            count = self.task_limit * random.randint(2, 10)
            new_requests = list(itertools.islice(self.start_requests_iterator, count))

            if new_requests:
                self.request_buffer.put(new_requests)
                return True if len(new_requests) < count else False

        return True

    async def push_request_to_waiting(self):
        """将请求添加到waiting队列"""

        requests_to_push = []

        while self.request_buffer:
            req = self.request_buffer.get()
            request = await self.middleware_manager.process_request(req, type=MiddlewareType.spider)

            if isinstance(request, BaseRequest):
                request.depth += 1
                requests_to_push.append(request)
            elif isinstance(request, Response):
                await self.request_pool.pending.remove_request(req)
                await self.datamanager.process_response(request, req)

        if requests_to_push:
            await self.request_pool.push_to_waiting(requests_to_push)

    async def process_waiting_requests(self):
        """处理waiting队列中取出的请求"""

        idx = 0
        tasks = []
        task_limit = self.task_limit

        async for request in self.request_pool.get_request(task_limit):
            obj = await self.middleware_manager.process_request(request, type=MiddlewareType.download)

            if obj is None:
                await self.request_pool.pending.remove_request(request)
                await self.request_buffer.put(obj)
            elif isinstance(obj, BaseRequest):
                tasks.append(asyncio.create_task(self.download(request)))
            elif isinstance(obj, Response):
                await self.datamanager.process_response(obj, request)
            else:
                continue

            await self.apply_request_sleep()
            idx += 1
            if idx >= task_limit:
                break

        return tasks

    async def process_tasks(self, tasks):
        """处理响应"""

        responses = await asyncio.gather(*tasks)

        for response in responses:
            if response is None:
                continue
            res = await self.middleware_manager.process_response(response)
            if res is None:
                await self.request_pool.push_to_failure(obj)
                continue
            elif isinstance(res, Response):
                await self.datamanager.process_response(response, response.request)
            elif isinstance(res, BaseRequest):
                await self.request_buffer.put(res)
            else:
                continue

    def update_avg_speed(self, running, completed_count):
        self.avg_speed = round(completed_count / running, 3) if running else 0

    async def fresh_progress(self):
        """更新进度"""

        completed_count = await self.request_pool.done_size()
        running = round(time.time() - self.crawing_time, 3)
        
        if completed_count % self.task_limit != 0 and int(running) % 5 != 0 and int(running) % 3 != 0:
            return
        
        if completed_count == 0:
            logger.debug(
                f'已成功完成 {completed_count} 个请求，程序已运行{self.format_running_time(running)}，'
                f'即将爬取完成'
            )
            return 

        self.update_avg_speed(running, completed_count)
        waiting_count = await self.request_pool.waiting_size()
        self.waiting_count = waiting_count
        progress = round(
            (
                completed_count / (waiting_count + completed_count)
            ) if (
                    waiting_count + completed_count
            ) else 0, 5
        )

        remaining = round(waiting_count / self.avg_speed, 3) if waiting_count else 0

        item = [{
            "进行数量": self.request_pool.pending_size(), "完成数量": completed_count, "剩余数量": waiting_count, 
            "成功数量": self.request_pool.success_size(), "失败数量": self.request_pool.failure_size(),
            '并发速度': self.avg_speed, '完成进度': str(progress * 100)[:6] + '%'
        }]

        logger.debug(
            f'已成功完成 {completed_count} 个请求，程序已运行{self.format_running_time(running)}，'
            f'预计{self.format_remaining_time(remaining)}后爬取完成，进度明细：\n{pretty_table(item)}'
        )


class DistributeEngine(Engine):
    """分布式引擎"""

    backend = BackendEngine.redis

    def __init__(self, *args, **kwargs):
        super(DistributeEngine, self).__init__(*args, **kwargs)
        self.count = 0
        self.offset = 0
        self.redis_spider_key = f'{self.spider.name}:info'
        self.redis_lock_key = 'lock'
        self.redis_stop_key = 'stop'
        self.redis_count_key = 'count'

    async def spider_close(self):
        super(DistributeEngine, self).spider_close()
        conn = self.connections['redis']['DEFAULT']
        await conn.delete(self.redis_spider_key)

    def check_redis_configuration(self):
        if 'redis' not in self.connections:
            raise MissingConfigException(f'{self.spider.name}分布式爬虫未配置redis数据库')
        if 'DEFAULT' not in self.connections['redis']:
            raise MissingConfigException(f'{self.spider.name}分布式爬虫中redis未配置DEFAULT数据库')

    async def determine_start_request_left(self, iterator_stop):
        """判断start_requests是否还有请求"""

        conn = self.connections['redis']['DEFAULT']

        if iterator_stop:
            return await self.set_iterator_stop(conn)

        async with RedisLock(
                spider_key=self.redis_spider_key, lock_key=self.redis_lock_key, conn=conn, wait_timeout=10
        ) as lock:
            # 判断是否加锁，如果加锁则获取请求，否则进一步判断
            if not lock.locked:
                stop = await lock.conn.hash.hget(self.redis_spider_key, self.redis_stop_key)
                return stop == '1'

            count = self.task_limit * random.randint(2, 10)
            redis_count = await lock.conn.hash.hget(self.redis_spider_key, self.redis_count_key)
            redis_count = int(redis_count) if redis_count is not None else 0

            if redis_count > count:
                # 需要剪切
                list(itertools.islice(self.start_requests_iterator, redis_count - self.count))
                new_count = redis_count - self.count
                self.count += new_count
            else:
                new_count = 0

            new_requests = list(itertools.islice(self.start_requests_iterator, count))
            if new_requests:
                self.request_buffer.put(new_requests)
                self.count += len(new_requests)
                # 将两个操作移到锁内，确保原子执行
                await lock.conn.hash.hset(
                    self.redis_spider_key, self.redis_count_key, str(redis_count + new_count)
                )
                return await self.set_iterator_stop(conn) if new_count < count else False

        return True

    async def set_iterator_stop(self, conn):
        await conn.hash.hset(self.redis_spider_key, self.redis_stop_key, '1')
        return True

        
class BatchEngine(Engine):

    async def execute(self):

        while True:

            if not self.is_time_to_run():
                if self.spider.next_time < datetime.now():
                    self.spider.next_time = self.spider.get_next_time()
                    continue
                logger.debug(
                    f"爬虫({self.spider.name})还未到运行时间，{self.spider.name}将在{self.spider.next_time}启动，当前北京"
                    f"时间是{datetime.now()}，距离启动还有 {(self.spider.next_time - datetime.now()).total_seconds():,.5f} 秒"
                )
                time.sleep(0.9)
                continue

            # 爬虫运行前回调
            if not self.spider.cust_call_before():
                break

            self.spider.next_time = self.spider.get_next_time()

            # 执行登录逻辑
            self.spider.token = self.spider.cust_call_login(self.spider.username, self.spider.password)

            await super(BatchEngine, self).execute()

            # 爬虫结束后回调
            if not self.spider.cust_call_end():
                break

            await self.request_pool.done.close()
            
    def is_time_to_run(self):
        return datetime.now().replace(microsecond=0) == self.spider.next_time
