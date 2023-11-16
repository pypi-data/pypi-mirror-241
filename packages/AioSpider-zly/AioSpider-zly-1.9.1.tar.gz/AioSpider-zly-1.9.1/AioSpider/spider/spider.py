from typing import Union, Callable

from AioSpider import logger, robot
from AioSpider.constants import SignalType
from AioSpider.http import Response, BaseRequest, Request
from AioSpider.signal import Signal


class Spider:

    name: str = None
    source: str = None
    start_req_list: list = []

    class SpiderRequestConfig:
        pass

    class ConcurrencyStrategyConfig:
        pass

    class ConnectPoolConfig:
        pass

    class DataFilterConfig:
        pass

    class RequestFilterConfig:
        pass

    class RequestProxyConfig:
        pass

    class BrowserConfig:
        pass

    def __init__(
            self,
            *,
            username: str = None,
            password: str = None,
            cookies: dict = None, token: str = None,
            level: int = None,
            call_before: Callable[[], bool] = None,
            call_end: Callable[[], bool] = None,
            call_login: Callable[[str, str], str] = None,
    ):

        self.id: Optional[int] = None
        self.status: int = 0
        self.count: int = 0
        self.start_time: datetime = None
        self.interval: Optional[int] = None
        self.level: int = None
        self.username: Optional[str] = username
        self.password: Optional[str] = password
        self.cookies: Optional[dict] = cookies
        self.token: Optional[str] = token
        self.cust_call_before: Callable[[], bool] = call_before or (lambda: True)
        self.cust_call_end: Callable[[], bool] = call_end or (lambda: True)
        self.cust_call_login: Callable[[str, str], str] = call_login or (lambda username, password: '')

        Signal().connect(SignalType.spider_open, self.spider_open)
        Signal().connect(SignalType.spider_close, self.spider_close)
        
        self.set_name()

    def start(self):
        from AioSpider.core import Engine
        Engine(self).start()

    def set_name(self):
        if self.name is None:
            self.name = self.__class__.__name__

    def spider_open(self):
        logger.info(f'------------------- 爬虫：{self.name} 已启动 -------------------')
        robot.info(f'{self.name} 爬虫已启动')

    def spider_close(self):
        logger.info(f'------------------- 爬虫：{self.name} 已关闭 -------------------')
        robot.info(f'{self.name} 爬虫已关闭')

    def start_requests(self) -> BaseRequest:
        for req in self.start_req_list:
            yield req

    def parse(self, response):
        """
            解析回调函数
            @params: response: Response对象
            @return: Request | dict | None
        """
        pass

    def default_parse(self, response: Response):
        pass

    def process_error_status(self, request: BaseRequest, status: int):
        return request
