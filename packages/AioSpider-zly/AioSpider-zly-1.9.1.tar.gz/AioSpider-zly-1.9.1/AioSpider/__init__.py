__all__ = [
    'tools', 'logger', 'pretty_table', 'robot'
]

import os
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Union

from loguru import logger
from AioSpider.tools import tools
from AioSpider.notice import Robot
from AioSpider.utils_pkg.prettytable import PrettyTable


def _get_work_path(path: Path = Path.cwd()):
    
    if str(path) == str(path.anchor):
        return None

    if {'spider', 'settings.py'} <= {i.name for i in path.iterdir()}:
        return path
    
    return _get_work_path(path.parent) or None


path = _get_work_path()
if path is not None:
    os.chdir(str(path))
    sys.path.append(str(path))

robot = Robot()


def pretty_table(item: Union[dict, List[dict]]):

    if isinstance(item, dict):
        item = [item]

    return str(PrettyTable(item=item))


class TableView:

    def __init__(self, items, bold=True):
        self.items = items
        self.bold = bold
        self.colors = [
            'red', 'green', 'yellow', 'magenta', 'cyan',
            'white', 'orange3', 'purple3', 'turquoise4'
        ]

    def console(self):
        from rich.console import Console
        from rich.table import Table

        console = Console()

        # 创建表格
        table = Table(header_style="bold blue", border_style='#d2c1ad')

        for index, k in enumerate(self.items[0].keys()):
            style = 'bold ' + self.colors[index] if self.bold else self.colors[index]
            table.add_column(k, justify="left", style=style, no_wrap=True)
            # table.add_column("Age", justify="center", style="magenta")
            # table.add_column("City", justify="right", style="green")

        for v in self.items:
            table.add_row(*[str(i) for i in v.values()])

        # 输出表格
        console.print(table)
    