from AioSpider import constants
from .aiohttp_module import AiohttpSession, AiohttpNoSession
from .requests_module import RequestsSession, RequestsNoSession


def downloader_factory(request_config, pool_config):
    
    handler_map = {
        (None, True): AiohttpSession,
        (None, False): AiohttpNoSession,
        (constants.RequestWay.aiohttp, True): AiohttpSession,
        (constants.RequestWay.aiohttp, False): AiohttpNoSession,
        (constants.RequestWay.requests, True): RequestsSession,
        (constants.RequestWay.requests, False): RequestsNoSession
    }

    handler = handler_map.get(
        (request_config.REQUEST_USE_METHOD, request_config.REQUEST_USE_SESSION)
    )
    if handler is None:
        raise ValueError('请求库配置不正确，请检查配置文件')
    
    return handler(request_config, pool_config)


class Downloader:

    def __init__(self, request_config, pool_config, middleware):
        self._handle = downloader_factory(request_config, pool_config)
        self.middleware = middleware

    async def fetch(self, request):
        return await self._handle(request)
