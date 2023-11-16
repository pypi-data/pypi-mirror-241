__all__ = ['WaitingRequest', 'WaitingRedisRequest']

import heapq
import random
import asyncio
from collections import defaultdict

from AioSpider import tools
from AioSpider.signal import Signal
from AioSpider.constants import SignalType
from AioSpider.http.base import BaseRequest
from AioSpider.requestpool.abc import RequestBaseABC


class WaitingRequest(RequestBaseABC):

    def __init__(self, depth_priority):
        self.name = 'waiting'
        self.waiting = {}
        self.depth_priority = depth_priority
        self.waiting_count = 0
        self.max_host_name = ''
        self.max_host_count = 0
        self.request_hashes = defaultdict(dict)
        Signal().connect(SignalType.waiting_close, self.close)

    async def put_request(self, request: BaseRequest):

        host = request.domain
        if host not in self.waiting:
            self.waiting[host] = []

        heapq.heappush(self.waiting[host], (-request.priority, request.depth, request.hash, request))
        
        self.waiting_count += 1
        self.request_hashes[host][request.hash] = self.request_hashes[host].get(request.hash, 0) + 1
        self._update_max_host(host)

    async def get_requests(self, count):

        requests_obtained = 0

        while requests_obtained < count and self.waiting_count > 0:
            max_requests_to_get = min(self.max_host_count, count - requests_obtained)

            for _ in range(max_requests_to_get):

                _, _, _, request = heapq.heappop(self.waiting[self.max_host_name])

                if request.hash in self.request_hashes.get(request.domain, {}):
                    if self.request_hashes[request.domain][request.hash] > 1:
                        self.request_hashes[request.domain][request.hash] -= 1
                    else:
                        self.request_hashes[request.domain].pop(request.hash)

                requests_obtained += 1
                self.waiting_count -= 1

                if not self.waiting[self.max_host_name]:
                    self.waiting.pop(self.max_host_name)

                self._update_max_host()

                yield request

    async def has_request(self, request: BaseRequest):
        host = request.domain
        return request.hash in self.request_hashes.get(host, set())

    async def request_size(self):
        return self.waiting_count

    def _update_max_host(self, new_host=None):
        if new_host and len(self.waiting[new_host]) > self.max_host_count:
            self.max_host_name = new_host
            self.max_host_count = len(self.waiting[new_host])
        else:
            if self.waiting:
                self.max_host_name, host_list = max(
                    self.waiting.items(), key=lambda x: len(x[1])
                )
                self.max_host_count = len(host_list)
            else:
                self.max_host_name, self.max_host_count = '', 0
                
    async def close(self):
        self.waiting = {}
        self.waiting_count = 0
        self.max_host_name = ''
        self.max_host_count = 0
        self.request_hashes = defaultdict(dict)


class WaitingRedisRequest(RequestBaseABC):

    def __init__(self, connector, spider, depth_priority):
        self.name = 'redis waiting'
        self.conn = connector['redis']['DEFAULT']
        self.spider = spider
        self.depth_priority = depth_priority
        Signal().connect(SignalType.waiting_close, self.close)
        self.redis_request_key = f'{self.spider.name}:waiting'

    async def put_request(self, request: BaseRequest):
        await self.conn.order_set.zadd(
            self.redis_request_key,
            {tools.dump_json(request.to_dict()): tools.make_timestamp()}
        )

    async def get_requests(self, count):

        while count > 0:
            fetch_count = count
            async for item in self._fetch_request(self.redis_request_key, fetch_count):
                yield item
            count -= fetch_count

    async def has_request(self, request: BaseRequest):
        x = await self.conn.order_set.zscore(
            self.redis_request_key,
            tools.dump_json(request.to_dict())
        )
        return x is not None

    async def _fetch_request(self, key, count):

        requests = await self.conn.order_set.zrange(key, 0, count - 1)
        await self.conn.order_set.zrem(key, *requests)

        for req in requests:
            yield BaseRequest.from_dict(tools.load_json(req))

    async def request_size(self):
        return await self.conn.order_set.zcard(self.redis_request_key)

    async def close(self):
        await self.conn.delete(self.redis_request_key)
        self.conn = None
