from typing import Union
from .GroupRobot import Robot


__version__ = '1.0.0'
__author__ = 'zly'
__email__ = 'zly717216@163.com'
__publish__ = '2022-11-26'


def set_key_word(key_word: Union[str, list] = None):
    Robot.set_key_word(key_word)


def set_tpl(self, tpl: str = None):
    Robot.set_tpl(tpl)


__all__ = [
    'Robot', '__version__', '__author__', '__email__',
    '__publish__', 'set_token', 'set_key_word', 'set_tpl'
]
