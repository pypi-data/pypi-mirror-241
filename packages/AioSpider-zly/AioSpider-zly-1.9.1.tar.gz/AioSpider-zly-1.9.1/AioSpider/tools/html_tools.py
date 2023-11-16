import webbrowser
from typing import Iterable, Union, Any

from lxml.etree import _Element, HTML
from lxml.html.clean import Cleaner


def clean_html(html: str, remove_tags: Iterable = None, safe_attrs: Iterable = None) -> str:
    """
    清晰 html 文本
    Args:
        html: html 文本
        remove_tags: 移除 html 中不需要的标签，如：['a', 'p', 'img']
        safe_attrs: 保留相关属性，如：['src', 'href']
    Return:
        清晰后的html文本
    """

    if not html:
        return ''

    # 保存新闻的时候，很多属性不需要保存，不然会占用硬盘资源，所以只保留图片标签的src属性就行
    if remove_tags is None:
        remove_tags = []

    if safe_attrs is None:
        safe_attrs = []

    remove_tags = frozenset(remove_tags)
    safe_attrs = frozenset(safe_attrs)

    cleaner = Cleaner(safe_attrs=safe_attrs, remove_tags=remove_tags)
    return cleaner.clean_html(html)


def xpath(node: Union[str, _Element], query: str, default: Any = None) -> Union[list, _Element, str]:
    """
    xpath 提取数据
    Args:
        node: 原始 html 文本数据
        query: xpath 解析式
        default: 默认值
    Return:
        default or Union[list, _Element, str]
    """

    if not isinstance(node, (str, _Element)) or not isinstance(query, str):
        return default

    try:
        if isinstance(node, str):
            parsed_node = HTML(node)
        else:
            parsed_node = node
        return parsed_node.xpath(query)
    except:
        return default


def xpath_text(node: Union[str, _Element], query: str, on: str = None, default: str = None) -> str:
    """
    xpath 提取文本数据
    Args:
        node: 原始 html 文本数据
        query: xpath 解析式
        on: 连接符
        default: 默认值
    Return:
        xpath 提取出来的文本
    """

    if on is None:
        on = ''

    if default is None:
        default = ''

    text_list = xpath(node=node, query=query, default=default)

    if isinstance(text_list, list):
        return on.join(text_list) if text_list else default

    if isinstance(text_list, str):
        return text_list

    return default


def open_html(url: str):
    """
    用默认浏览器打开网址或文件
    Args:
        url: url
    Return:
        NoReturn
    """

    webbrowser.open(url)

