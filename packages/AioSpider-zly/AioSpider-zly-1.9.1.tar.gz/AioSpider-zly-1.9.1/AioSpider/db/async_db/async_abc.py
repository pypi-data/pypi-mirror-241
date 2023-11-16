from abc import ABCMeta, abstractmethod

from AioSpider.signal import Signal
from AioSpider.constants import SignalType


class AbcDB(metaclass=ABCMeta):

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.__init__(*args, **kwargs)
        return instance.connect()
    
    def __init__(self, *args, **kwargs):
        Signal().connect(SignalType.database_close, self.close)

    @abstractmethod
    async def find(self, table: str, encoding=None):
        pass

    @abstractmethod
    async def insert(self, table: str, items: list, auto_update: bool = False):
        pass

    @abstractmethod
    def remove_one(self):
        pass

    @abstractmethod
    def remove_many(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def close(self):
        pass
