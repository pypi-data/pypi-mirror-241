import asyncio
import numbers

import aiohttp

from AioSpider import logger
from AioSpider import constants
from AioSpider.exceptions import RequestError
from AioSpider.http.base import BaseRequest
from AioSpider.http.response import Response


class BaseMeta:

    def __init__(self, request_config, pool_config, *args, **kwargs):
        self.request_config = request_config
        self.pool_config = pool_config

    async def __call__(self, request: BaseRequest, *args, **kwargs):
        return await self.request(request)

    async def request(self, request: BaseRequest):

        self.validate_request(request)
        attrs = self.query_attrs(request)
        attrs = self.handle_proxy(attrs)
        
        if request.method.upper() == 'GET':
            return await self.get(request, **attrs)

        if request.method.upper() == 'POST':
            return await self.post(request, **attrs)

        raise RequestError()

    def query_attrs(self, request: BaseRequest):

        if not request:
            return None

        attrs = {
            'headers': request.headers,
            'timeout': request.timeout or self.request_config.REQUEST_TIMEOUT,
            'cookies': request.cookies,
            'params': request.params,
            'data': request.data,
            'proxy': request.proxy
        }

        url = request.url
        if '?' not in url:
            attrs['params'] = request.params
        attrs['url'] = url

        return attrs

    def validate_request(self, request: BaseRequest):

        # 判断请求方法是否合法
        if request.method.upper() not in constants.RequestMethod:
            raise ValueError(f"无效的请求方法: {request.method}")

        # 检查url是否合法
        if not request.scheme or not request.domain:
            raise ValueError(f"无效的 URL: {request.url}")

        return True
    
    @staticmethod
    def handle_request_except(func):

        async def ware(self, request, **kwargs):
             
            times = 1 if self.request_config.REQUEST_ERROR_RETRY_TIMES <= 0 else \
                self.request_config.REQUEST_ERROR_RETRY_TIMES
            index = 1
            exception = None
            
            while index <= times:
                index += 1
                try:
                    return await func(self, request, **kwargs)
                except RuntimeError as e:
                    if 'Session is closed' in str(e):
                        self._closed = True
                        logger.warning(f'{request} 请求异常，Session 被异常关闭，正在自动处理...')
                        return await func(self, request, **kwargs)
                    else:
                        logger.error(f'{request} 请求异常，正在进行第{index}次重试，异常原因：{e}')
                        exception = e
                except Exception as e:
                    logger.error(f'{request} 请求异常，正在进行第{index}次重试，异常原因：{e}')
                    exception = e
                await asyncio.sleep(self.request_config.REQUEST_ERROR_RETRY_SLEEP)
                
            return exception

        return ware

    @staticmethod
    def handle_response_except(func):

        async def ware(self, *args, **kwargs):
            try:
                return await func(self, *args, **kwargs)
            except Exception as e:
                return e

        return ware


class RequestMeta(BaseMeta):

    def __init__(self, request_config, pool_config):
        super().__init__(request_config, pool_config)
        self._session = None
        self._closed = True

    @staticmethod
    def handle_proxy(attrs):
        proxy = attrs.pop('proxy', None)

        if not proxy:
            attrs['proxies'] = None
            return attrs

        if isinstance(proxy, dict):
            attrs['proxies'] = proxy
            return attrs

        if 'http' not in proxy:
            attrs['proxies'] = {
                'http': 'http://' + proxy, 'https': 'http://' + proxy
            }
        else:
            attrs['proxies'] = {'http': proxy, 'https': proxy}

        return attrs
    
    def process_response(self, req: BaseRequest, resp) -> Response:
        return Response(
            status=resp.status_code, headers=dict(resp.headers),
            content=resp.content, request=req
        )


class AiohttpMeta(BaseMeta):

    def __init__(self, request_config, pool_config):
        super().__init__(request_config, pool_config)
        self._connector = None
        self._session = None
        self._closed = True

    def query_attrs(self, request: BaseRequest):
        attrs = super().query_attrs(request=request)

        if attrs.get('timeout') and isinstance(attrs['timeout'], numbers.Number):
            attrs['timeout'] = aiohttp.ClientTimeout(total=int(attrs['timeout']))

        return attrs
    
    @staticmethod
    def handle_proxy(attrs):

        if attrs['proxy'] is None:
            return attrs

        if 'http' not in attrs['proxy']:
            attrs['proxy'] = 'http://' + attrs['proxy']

        return attrs
    
    async def process_response(self, req: BaseRequest, resp) -> Response:
        res = await resp.read()
        return Response(
            status=resp.status, headers=dict(resp.headers), content=await resp.read(), request=req
        )
