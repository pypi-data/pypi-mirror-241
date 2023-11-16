import time
import math
import random
from abc import ABCMeta, abstractmethod

from AioSpider.http import Response
from AioSpider.constants import SignalType
from AioSpider.signal import Signal


class SpiderMiddleware(metaclass=ABCMeta):
    """中间件基类"""

    def __init__(self, spider, settings, browser=None):
        self.spider = spider
        self.settings = settings
        self.browser = browser
        Signal().connect(SignalType.spider_open, self.spider_open, spider)
        Signal().connect(SignalType.spider_close, self.spider_close, spider)

    @abstractmethod
    def process_request(self, request):
        """
            处理请求
            @params:
                request: BaseRequest 对象
            @return:
                Request: 交由引擎重新调度该Request对象
                Response: 交由引擎重新调度该Response对象
                None: 正常，继续往下执行 穿过下一个中间件
                False: 丢弃该Request或Response对象
        """

        return None

    @abstractmethod
    def process_response(self, response):
        """
            处理请求
            @params:
                response: Response 对象
            @return:
                Request: 交由引擎重新调度该Request对象
                None: 正常，继续往下执行 穿过下一个中间件
                False: 丢弃该Request或Response对象
        """

        return None

    def spider_open(self, spider):
        pass

    def spider_close(self, spider):
        pass


class BrowserRenderMiddleware(SpiderMiddleware):

    def process_request(self, request):

        if request.render:
            return Response(request=request, browser=self.browser)

        return None

    def process_response(self, response):
        return None

