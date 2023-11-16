from typing import List, Dict, Type

from AioSpider.tools.string_tools import join
from AioSpider.tools.encrypt_tools import make_md5
from AioSpider.models.models import Model

from .filter import DataFilter
from .init import TableSync, LoadingTableData
from .commit import SQLCommit, FileCommit, CSVCommit, MongoCommit, Container


class DataManager:
    
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.__init__(*args, **kwargs)
        return instance.open()

    def __init__(self, settings, connector, models: List[Type[Model]]):

        self.settings = settings
        self.connector = connector
        self.models = models
        self._size = settings.DataFilterConfig.COMMIT_SIZE
        self._container: Dict[str, Container] = None
        
        self.data_filter = DataFilter(
            enabled=settings.DataFilterConfig.ENABLED,
            method=settings.DataFilterConfig.FILTER_METHOD,
            capacity=settings.DataFilterConfig.BLOOM_INIT_CAPACITY,
            max_capacity=settings.DataFilterConfig.BLOOM_MAX_CAPACITY,
            error_rate=settings.DataFilterConfig.BLOOM_ERROR_RATE,
        )

    @property
    def containers(self) -> Dict[str, 'Container']:
        """返回包含不同连接器对应容器类的容器字典"""

        if self._container is None:

            size = {m.Meta.tb_name: m.Meta.commit_size or self._size for m in self.models}
            db = {m.Meta.tb_name: m.Meta.db or self._size for m in self.models}

            container_classes = {
                'mysql': SQLCommit,
                'sqlite': SQLCommit,
                'mongo': MongoCommit,
                'csv': CSVCommit,
                'file': FileCommit,
            }

            self._container = {
                connector: container_class(
                    self.connector[connector], size=size, db=db, task_limit=self.settings.DataFilterConfig.TASK_LIMIT
                )
                for connector, container_class in container_classes.items()
                if connector in self.connector
            }

        return self._container

    async def open(self):
        """打开数据管理器，创建表并加载数据"""

        await self._create_table()
        if self.settings.DataFilterConfig.ENABLED and self.settings.DataFilterConfig.LoadDataFromDB:
            await LoadingTableData(
                connector=self.connector, data_filter=self.data_filter, models=self.models
            ).load_data()
            
        return self
    
    async def close(self):
        for k, v in self.containers.items():
            await v.close()

    async def _create_table(self):
        """创建表格"""

        table_manager = TableSync(self.connector, models=self.models)

        table_creators = {
            'mysql': table_manager.create_sql_table,
            'sqlite': table_manager.create_sql_table,
            'csv': table_manager.create_csv_table,
        }

        for connector in self.connector:
            table_creator_func = table_creators.get(connector)
            if table_creator_func:
                await table_creator_func()

    async def commit(self, model: Type[Model]):
        """提交数据到指定容器"""

        table = model.Meta.tb_name
        item = model.make_item()

        duplicate_field = [f for f in model.get_unique_field() if f in item]
        if duplicate_field:
            item_hash = make_md5(
                join([item.get(i) for i in duplicate_field], on='-')
            )
        else:
            field = [i for i in model.fields.keys() if i != 'id']
            item_hash = make_md5(
                join([item.get(i) for i in field], on='-')
            )

        if self.data_filter.contains(table, item_hash):
            return None

        container = self.containers[model.Meta.engine]
        await container.add(table, item=item)
        
        if model.Meta.engine in ['mysql', 'sqlite']:
            await container.commit(table, auto_update=model.Meta.auto_update)
        elif model.Meta.engine == 'mongo':
            await container.commit(table, unique=model.get_unique_field(), auto_update=model.Meta.auto_update)
        elif model.Meta.engine == 'csv':
            await container.commit(table, encoding=model.Meta.encoding)
        elif model.Meta.engine == 'file':
            return await container.commit(model)
        else:
            raise NotImplemented
