__all__ = [
    'AsyncCSVFile', 'AsyncMongoAPI', 'AsyncMySQLAPI', 'AsyncSQLiteAPI', 'RedisLock',
    'SyncMongoAPI', 'SyncMySQLAPI', 'SyncSQLiteAPI', 'Connector'
]

from .async_db import (
    AsyncCSVFile, AsyncMongoAPI, AsyncMySQLAPI, AsyncSQLiteAPI, RedisLock
)
from .sync_db import (
    SyncMongoAPI, SyncMySQLAPI, SyncSQLiteAPI
)


class Connector:

    def __init__(self):
        self._connector = dict()

    def __getitem__(self, name):
        return self._connector[name]

    def __setitem__(self, name, connect):
        setattr(self, name, connect)
        self._connector[name] = connect

    def __contains__(self, item):
        return item in self._connector

    def __str__(self):
        return f'Connector({self._connector})'

    __repr__ = __str__

