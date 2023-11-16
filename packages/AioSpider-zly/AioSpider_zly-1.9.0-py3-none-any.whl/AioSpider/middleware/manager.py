import inspect

from AioSpider.constants import MiddlewareType
from AioSpider.http import BaseRequest, Response
from .spider import SpiderMiddleware


class MiddlewareManager:
    
    def __init__(self, spider):
        self.spider = spider
        self.download_middlewares = []
        self.spider_middlewares = []

    def register(self, middleware):
        if isinstance(middleware, SpiderMiddleware):
            self.spider_middlewares.append(middleware)
        else:
            self.download_middlewares.append(middleware)
            
    async def process_request(self, request: BaseRequest, type):

        if request is None:
            return False
        
        if type == MiddlewareType.download:
            middlewares = self.download_middlewares
        elif type == MiddlewareType.spider:
            middlewares = self.spider_middlewares
        else:
            raise TypeError('中间件类型错误')

        for m in middlewares:

            if not hasattr(m, 'process_request'):
                continue

            ret = await m.process_request(request) if inspect.iscoroutinefunction(
                m.process_request) else m.process_request(request)

            if ret is None:
                continue
            elif ret is False:
                return None
            elif isinstance(ret, (BaseRequest, Response)):
                return ret
            else:
                raise MiddlerwareError(flag=1)

        return request

    async def process_response(self, response: Response):

        if response is None:
            return False

        for m in reversed(self.download_middlewares):
            if not hasattr(m, 'process_response'):
                continue

            ret = await m.process_response(response) if inspect.iscoroutinefunction(
                m.process_response) else m.process_response(response)

            if ret is None:
                continue
            elif ret is False:
                return None
            elif isinstance(ret, (BaseRequest, Response)):
                return ret
            else:
                raise MiddlerwareError(flag=1)

        return response

    async def process_exception(self, request, exception):

        if exception is None:
            return None

        for m in self.download_middlewares:
            if not hasattr(m, 'process_exception'):
                continue

            ret = m.process_exception(request, exception)

            if ret is None:
                continue
            elif ret is False:
                return None
            elif isinstance(ret, Exception):
                raise ret
            elif isinstance(ret, (BaseRequest, Response)):
                return ret
            else:
                raise MiddlerwareError(flag=2)

        return None
