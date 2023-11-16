import aiohttp

from AioSpider import logger
from AioSpider.signal import Signal
from AioSpider.constants import SignalType
from AioSpider.downloader.abc import AiohttpMeta
from AioSpider.tools.tools import singleton


@singleton
class AiohttpSession(AiohttpMeta):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Signal().connect(SignalType.session_close, self.close)

    @property
    def connector(self):
        if self._connector is None or self._closed:
            self._connector = aiohttp.TCPConnector(
                limit=self.pool_config.MAX_CONNECT_COUNT,
                use_dns_cache=self.pool_config.USE_DNS_CACHE,
                force_close=self.pool_config.FORCE_CLOSE,
                ttl_dns_cache=self.pool_config.TTL_DNS_CACHE,
                limit_per_host=self.pool_config.LIMIT_PER_HOST,
                verify_ssl=self.pool_config.VERIFY_SSL
            )
            self._closed = False

        return self._connector

    @property
    def session(self):
        if self._session is None or self._closed:
            self._session = aiohttp.ClientSession(connector=self.connector)
        return self._session

    @AiohttpMeta.handle_request_except
    async def get(self, request, **kwargs):
        async with self.session.get(**kwargs) as resp:
            return await self.process_response(request, resp)

    @AiohttpMeta.handle_request_except
    async def post(self, request, **kwargs):
        async with self.session.post(**kwargs) as resp:
            return await self.process_response(request, resp)

    async def close(self):

        if self._session is None:
            return

        await self.session.close()
        self._session = None
        self._closed = True
        logger.info("aiohttp session 会话已关闭")


class AiohttpNoSession(AiohttpMeta):

    @AiohttpMeta.handle_request_except
    async def get(self, request, **kwargs):
        async with aiohttp.request('GET', **kwargs) as resp:
            return await self.process_response(request, resp)

    @AiohttpMeta.handle_request_except
    async def post(self, request, **kwargs):
        async with aiohttp.request('POST', **kwargs) as resp:
            return await self.process_response(request, resp)
