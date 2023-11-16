import re as _re
from typing import Any, Iterable


def join(data: Iterable, on: str = '') -> str:
    """
    拼接字符串
    Args:
        data: 可迭代对象，若data中的元素有非字符串类型的，会被强转
        on: 连接符
    Return:
        拼接后的字符串
    """

    if not isinstance(data, list):
        data = list(data)

    for index, value in enumerate(data):
        if isinstance(value, str):
            continue
        data[index] = str(value)

    return on.join(data)


def is_chinese(string: str) -> bool:
    """判断字符串是否是中文"""

    if not isinstance(string, str):
        return False

    return bool(re.search(r'[\u4e00-\u9fff]+', string))


def re(text: str, regx: str, default: Any = None, flag=_re.S) -> list:
    """
    正则 提取数据
    :param text: 原始文本数据
    :param regx: 正则表达式
    :param default: 默认值
    :return: default or list
    """

    if default is None:
        default = []

    t = _re.findall(regx, text, flag)
    return t if t else default


def re_match(text: str, regx: str) -> bool:
    """
    正则匹配
    Args:
        text: 原始文本数据
        regx: 正则表达式
    Return: 
        bool
    """

    return bool(_re.match(regx, text))


def re_text(text: str, regx: str, default: Any = None, flag=_re.S) -> str:
    """
    正则 提取文本数据
    Args:
        text: 原始文本数据
        regx: 正则表达式
        default: 默认值
    Return:
        default or list
    """

    if default is None:
        default = ''

    t = re(text=text, regx=regx, default=default, flag=flag)
    return t[0] if t else default


def re_sub(text: str, regx: str, replace: str) -> str:
    """
    正则 提取文本数据
    Args:
        text: 原始文本数据
        regx: 正则表达式
        replace: 替换值
    Return:
        返回被替换后的字符串
    """
    return _re.sub(regx, replace, text)


def eval_string(string: str, default: Any = None) -> Any:
    """
    执行字符串
    Args:
        string: 字符串
        default: 默认值
    Return:
        字符串执行结果 Any
    """
    if not isinstance(string, str):
        return string

    try:
        return eval(string)
    except Exception:
        return default

