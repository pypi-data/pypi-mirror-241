from typing import List, Union

from AioSpider import logger
from AioSpider.signal import Signal
from AioSpider.constants import SignalType, BackendEngine
from AioSpider.exceptions import SystemConfigError
from AioSpider.http.base import BaseRequest
from AioSpider.requestpool.done import RequestDB
from AioSpider.requestpool.pending import PendingRequest
from AioSpider.requestpool.failure import FailureRequest
from .waiting import WaitingRequest, WaitingRedisRequest


class RequestPool:
    
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.__init__(*args, **kwargs)
        return instance.loads_cache()

    def __init__(self, spider, settings, connector, backend=BackendEngine.queue):

        self.spider = spider
        self.settings = settings
        self.backend = backend
        self.waiting = self._init_waiting(connector)
        self.pending = PendingRequest()
        self.failure = FailureRequest(settings)
        self.done = RequestDB(spider, settings, connector, backend)
        self._last_percent = 0
        Signal().connect(SignalType.request_close, self.close)

    def _init_waiting(self, connector):

        if self.backend == BackendEngine.queue:
            return WaitingRequest(
                depth_priority=self.settings.SpiderRequestConfig.DepthPriority
            )

        if self.backend == BackendEngine.redis:
            return WaitingRedisRequest(
                connector, self.spider, depth_priority=self.settings.SpiderRequestConfig.DepthPriority
            )

        raise SystemConfigError(flag=2)

    async def close(self):
        # 缓存
        await self._dumps_cache()
        await Signal().emit(SignalType.waiting_close)
        await Signal().emit(SignalType.pending_close)
        await Signal().emit(SignalType.failure_close)
        await Signal().emit(SignalType.done_close)

    async def loads_cache(self):
        await self.done.load_requests()
        return self

    async def _dumps_cache(self):
        await self.done.dump_requests(strict=False)

    async def set_status(self, response):

        request = response.request

        # 从pending队列中删除
        if await self.pending.has_request(request):
            await self.pending.remove_request(request)

        await self.update_status(response, request)

        return

    async def update_status(self, response, request):
        """更新状态"""

        if response.status == 200:
            await self.done.set_success(request)
            if await self.failure.has_request(request):
                await self.failure.remove_request(request)
            if await self.done.has_request(request):
                await self.done.remove_failure(request)
        else:
            r = await self.failure.put_request(request)
            if not r:
                await self.done.set_failure(request)

    async def push_to_waiting(self, request: Union[BaseRequest, List[BaseRequest]]):
        """将request添加到waiting队列"""
        count = await self._push_requests_to_waiting(request)
        logger.debug(f'{count} 个请求添加到 waiting 队列')

    async def _push_requests_to_waiting(self, request: Union[BaseRequest, List[BaseRequest]]):
        """将多个request添加到waiting队列"""

        if not isinstance(request, list):
            request = [request]

        count = 0
        for req in request:
            if await self._is_request_valid_and_unique(req):
                await self.waiting.put_request(req)
                count += 1

        return count

    async def _is_request_valid_and_unique(self, request: BaseRequest):
        """判断请求是否有效且唯一"""

        queue = await self._request_exists_queue(request)
        if queue:
            logger.debug(f'request 已存在{queue}队列中 ---> {request}')
            return False

        if not request.domain or '.' not in request.domain or 'http' not in request.website:
            logger.debug(f'该request可能存在问题，已自动丢弃 ---> {request}')
            return False

        return True

    async def _request_exists_queue(self, request: BaseRequest):
        if request.dnt_filter:
            return None
        for queue in [self.waiting, self.pending, self.failure, self.done]:
            if await queue.has_request(request):
                return queue.name
        return None

    async def push_to_failure(self, request: BaseRequest):

        if await self.done.has_request(request):
            return None
        if await self.pending.has_request(request):
            await self.pending.remove_request(request)
            return None
        if await self.waiting.has_request(request):
            await self.waiting.remove_request(request)
            return None
        await self.failure.put_request(request)

    async def get_request(self, count: int):
        """从请求池中获取request"""

        async def _get_valid_request():
            while True:
                if not await self.waiting_empty():
                    requests = self.waiting.get_requests(count)
                elif not await self.failure_empty():
                    requests = self.failure.get_requests(count)
                else:
                    return
   
                async for request in requests:
                    if not (await self.pending.has_request(request) or await self.done.has_request(request)):
                        yield request

        async for request in _get_valid_request():
            if request is not None:
                yield await self.pending.put_request(request)

    async def waiting_size(self):
        return await self.waiting.request_size()

    def pending_size(self):
        return self.pending.request_size()

    def failure_size(self):
        return self.failure.request_size()

    async def done_size(self):
        return await self.done.request_size()
    
    def success_size(self):
        return self.done.done.success_count

    async def waiting_empty(self):
        return await self.waiting_size() == 0

    def pending_empty(self):
        return self.pending_size() == 0

    async def failure_empty(self):
        return await self.failure.empty()
