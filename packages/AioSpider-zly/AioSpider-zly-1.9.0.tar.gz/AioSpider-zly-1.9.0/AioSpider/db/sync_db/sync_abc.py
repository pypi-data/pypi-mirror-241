from abc import ABCMeta, abstractmethod

from AioSpider.signal import Signal
from AioSpider.constants import SignalType


class AbcDB(metaclass=ABCMeta):
    
    def __init__(self, *args, **kwargs):
        Signal().connect(SignalType.database_close, self.close)

    @abstractmethod
    async def find(self):
        pass

    @abstractmethod
    async def insert(self, table: str, item: dict):
        pass
    
    @abstractmethod
    async def update(self, table: str, item: dict):
        pass

    @abstractmethod
    def remove_one(self):
        pass

    @abstractmethod
    def remove_many(self):
        pass

    @abstractmethod
    def close(self):
        pass
