__all__ = ['FailureRequest']

from collections import defaultdict
from typing import Dict

from AioSpider import logger
from AioSpider.signal import Signal
from AioSpider.constants import SignalType
from AioSpider.http.base import BaseRequest
from AioSpider.requestpool.abc import RequestBaseABC


class FailureRequest(RequestBaseABC):

    def __init__(self, settings):
        self.name = 'failure'
        self.failure = set()
        self.max_failure_times = settings.SpiderRequestConfig.MAX_FAILURE_RETRY_TIMES - 1
        self.failure_hash = defaultdict(int)
        Signal().connect(SignalType.failure_close, self.close)

    async def put_request(self, request: BaseRequest):
        """将请求添加到队列"""

        if self.failure_hash.get(request.hash, 0) >= self.max_failure_times:
            logger.warning(f'该请求失败次数超限，系统将自动丢弃处理！请求：{request}')
            return False

        self.failure.add(request)
        self.failure_hash[request.hash] = self.failure_hash.get(request.hash, 0) + 1
        return True

    async def remove_request(self, request: BaseRequest):
        """将请求移除队列"""
        self.failure.pop(request)

    async def get_requests(self, count):
        """从队列中获取一个请求"""
        
        count = count if count <= self.request_size() else self.request_size()
        if not self.failure:
            return

        for _ in range(count):
            if not self.failure:
                return 
            yield self.failure.pop()

    async def has_request(self, request: BaseRequest):
        return True if request in self.failure else False

    def request_size(self):
        return len(self.failure_hash)
    
    async def empty(self):
        return False if self.failure else True

    def get_failure_times(self, request: BaseRequest):
        return self.failure_hash.get(request.hash, 0)

    async def close(self):
        self.failure = set()
