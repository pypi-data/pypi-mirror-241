import asyncio
import requests
from requests.adapters import HTTPAdapter

from AioSpider.signal import Signal
from AioSpider.constants import SignalType
from AioSpider.downloader.abc import RequestMeta
from AioSpider.tools.tools import singleton


@singleton
class RequestsSession(RequestMeta):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Signal().connect(SignalType.session_close, self.close)

    @property
    def session(self):
        if self._session is None or self._closed:
            self._session = requests.Session()

            adapter = HTTPAdapter(
                pool_connections=self.pool_config.MAX_CONNECT_COUNT,
                pool_maxsize=self.pool_config.LIMIT_PER_HOST,
                pool_block=True
            )

            self._session.mount("http://", adapter)
            self._session.mount("https://", adapter)
            self._closed = False

        return self._session

    @RequestMeta.handle_request_except
    async def get(self, request, **kwargs):
        resp = self.session.get(**kwargs)
        return self.process_response(request, resp)

    @RequestMeta.handle_request_except
    async def post(self, request, **kwargs):
        resp = self.session.post(**kwargs)
        return self.process_response(request, resp)

    async def close(self):
        
        if self._session is None:
            return

        self.session.close()
        self._session = None
        self._closed = True


class RequestsNoSession(RequestMeta):

    @RequestMeta.handle_request_except
    async def get(self, request, **kwargs):
        resp = requests.get(**kwargs)
        return self.process_response(request, resp)

    @RequestMeta.handle_request_except
    async def post(self, request, **kwargs):
        resp = requests.post(**kwargs)
        return self.process_response(request, resp)
