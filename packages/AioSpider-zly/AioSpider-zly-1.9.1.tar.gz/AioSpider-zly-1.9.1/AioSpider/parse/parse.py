import re
import json
from typing import Optional, TypeVar, Union, Callable

import execjs
from lxml import etree
from lxml.etree import _Element, _ElementUnicodeResult, _ElementStringResult
from bs4 import BeautifulSoup, ResultSet, Tag

from AioSpider import logger
from AioSpider.tools.tools import re_text


Xpath = TypeVar("XpathParser")
Re = TypeVar("ReParser")
Css = TypeVar("CssParser")
_Parser = TypeVar("Parser")


class XpathParser:

    replace_dic = {'&quot;': '"'}

    def __init__(self, text: Union[str, list, _Element] = None):

        if isinstance(text, str):
            self.html = etree.HTML(text)
        else:
            self.html = text

    def __str__(self):
        return f'{self.__class__.__name__} {self.html}'

    __repr__ = __str__

    def __getitem__(self, index):
        return self.__class__(self.html[index])

    def __len__(self):
        if isinstance(self.html, list):
            return len(self.html)
        else:
            return 1 if self.html else 0

    def xpath(self, query: str, **kwargs: dict) -> Xpath:

        if self.html is None:
            return self.__class__()

        if isinstance(self.html, _Element):
            return self.__class__(self.html.xpath(query, **kwargs))

        if isinstance(self.html, list):
            x = [i.xpath(query, **kwargs) for i in self.html if isinstance(i, _Element)]
            return self.__class__([j for i in x for j in i])

        return self

    def empty(self):
        return not bool(self.html)

    def remove_tags(self, tags: Union[str, list]):

        if isinstance(tags, str):
            tags = [tags]

        if not isinstance(self.html, list):
            self.html = [self.html]

        for item in self.html:
            if not isinstance(item, _Element):
                continue

            for tag in tags:
                elements = item.xpath(f"//{tag}")
                for element in elements:
                    parent = element.getparent()
                    if parent is not None:
                        parent.remove(element)

        return self

    def get_follow_tags(self, tag: str = None, n: int = None):

        if tag is None:
            tag = '*'

        if isinstance(self.html, _Element):
            if n is None:
                self.html = self.html.xpath(f"following-sibling::{tag}")
            else:
                self.html = self.html.xpath(f"following-sibling::{tag}[{n}]")

        if isinstance(self.html, list):
            self.html = [
                i.xpath(f"following-sibling::{tag}") if n is None else i.xpath(f"following-sibling::{tag}[{n}]")
                for i in self.html
            ]
            self.html = [j for i in self.html for j in i]

        return self

    def get_preced_tags(self, tag: str = None, n: int = None):

        if tag is None:
            tag = '*'

        if isinstance(self.html, _Element):
            if n is None:
                self.html = self.html.xpath(f"preceding-sibling::{tag}")
            else:
                self.html = self.html.xpath(f"preceding-sibling::{tag}[{n}]")

        if isinstance(self.html, list):
            self.html = [
                i.xpath(f"preceding-sibling::{tag}") if n is None else i.xpath(f"preceding-sibling::{tag}[{n}]")
                for i in self.html
            ]
            self.html = [j for i in self.html for j in i]

        return self

    def to_string(self, encoding='unicode', delete: Union[str, list] = '\n'):

        ele = self.extract_first()

        if ele is None:
            return ''

        if ele.html is None:
            return ''

        try:
            txt = etree.tostring(ele.html, encoding=encoding)
        except Exception as e:
            logger.error(f"xpath to_string异常: {e}")
            txt = ""

        if isinstance(delete, str):
            delete = [delete]

        for i in delete:
            txt = txt.replace(i, '')

        return txt

    def text(self) -> str:

        if not self.html:
            return ''

        text = ''

        if isinstance(self.html, (str, _ElementUnicodeResult, _ElementStringResult)):
            text = str(self.html)

        if isinstance(self.html, _Element):
            strings = self.html.xpath('//text()')
            text = ''.join(strings) if strings else ''

        if isinstance(self.html, list):
            if isinstance(self.html[0], (str, _ElementUnicodeResult, _ElementStringResult)):
                text = ''.join(self.html)
            elif isinstance(self.html[0], _Element):
                text = ''.join(self.html[0].xpath('//text()'))
            else:
                return ''

        for k, v in self.replace_dic.items():
            text = text.replace(k, v)

        return text

    def extract(self):
        self.html = self.html if isinstance(self.html, list) else [self.html]
        return self

    def extract_first(self) -> Xpath:
        if isinstance(self.html, list):
            self.html = self.html[0] if self.html else ''
        else:
            self.html = self.html if isinstance(self.html, _Element) else ''
        return self.__class__(self.html)

    def extract_last(self) -> Xpath:
        if isinstance(self.html, list):
            self.html = self.html[-1] if self.html else ''
        else:
            self.html = self.html if isinstance(self.html, _Element) else ''
        return self.__class__(self.html)


class ReParser:

    def __init__(self, text: Union[str, list] = None):
        self.string = text

    def __str__(self):
        return f'{self.__class__.__name__} {self.string}'

    __repr__ = __str__

    def __getitem__(self, index):
        return self.__class__(self.string[index])

    def __len__(self):
        if isinstance(self.string, list):
            return len(self.string)
        else:
            return 1 if self.string else 0

    def re(self, query: str, flags: int = 0) -> Re:

        if self.string is None:
            return self

        if isinstance(self.string, str):
            return self.__class__(re.findall(query, self.string, flags=flags))

        if isinstance(self.string, list):
            arr = [re.findall(query, i, flags=flags) for i in self.string if isinstance(i, str)]
            return self.__class__([j for i in arr for j in i])

        return self

    def empty(self):
        return bool(self.string)

    def text(self) -> str:

        if not self.string:
            return ''

        if isinstance(self.string, str):
            return self.string

        if isinstance(self.string, list):
            return self.string[0] if isinstance(self.string[0], str) else ''

        return ''

    def extract(self):
        self.string = self.string if isinstance(self.string, list) else [self.string]
        return self

    def extract_first(self):
        if isinstance(self.string, list):
            self.string = self.string[0] if self.string else ''
        return self

    def extract_last(self):
        if isinstance(self.string, list):
            self.string = self.string[-1] if self.string else ''
        return self


class CssParser:

    def __init__(self, text: Union[str, list] = None):
        if isinstance(text, str):
            self.tag = BeautifulSoup(text, 'html.parser')
        else:
            self.tag = text

    def __str__(self):
        return f'{self.__class__.__name__} {self.tag}'

    __repr__ = __str__

    def __getitem__(self, index):
        return self.__class__(self.tag[index])

    def __len__(self):
        if isinstance(self.tag, list):
            return len(self.tag)
        else:
            return 1 if self.tag else 0

    def css(self, query: str, **kwargs) -> Css:

        if self.tag is None:
            return self

        if isinstance(self.tag, Tag):
            return self.__class__(self.tag.select(query, **kwargs))

        if isinstance(self.tag, ResultSet):
            arr = [i.select(query, **kwargs) for i in self.tag if isinstance(i, Tag)]
            return self.__class__([j for i in arr for j in i])

        return self

    def empty(self):
        return bool(self.tag)

    def text(self) -> str:

        if isinstance(self.tag, str):
            return self.tag

        if isinstance(self.tag, Tag):
            return str(self.tag.contents[0])

        if isinstance(self.tag, list):
            if not self.tag:
                return ''
            if isinstance(self.tag[0], str):
                return self.tag[0]
            if isinstance(self.tag[0], Tag):
                return str(self.tag[0].contents[0])

        return ''

    def extract(self):
        self.tag = self.tag if isinstance(self.tag, list) else [self.tag]
        return self

    def extract_first(self):
        if isinstance(self.tag, list):
            self.tag = self.tag[0] if self.tag else Tag()
        return self

    def extract_last(self):
        if isinstance(self.tag, list):
            self.tag = self.tag[-1] if self.tag else Tag()
        return self
        
    def to_string(self, encoding='unicode', delete: Union[str, list] = '\n'):

        tag = self.extract_first()

        if tag is None:
            return ''

        if isinstance(tag, Tag):
            txt = tag.string

        if isinstance(delete, str):
            delete = [delete]

        for i in delete:
            txt = txt.replace(i, '')

        return txt
    
    def attrs(self, key: str = None, default=None):

        if isinstance(self.tag, Tag):
            if key is None:
                return self.tag.attrs
            else:
                return self.tag.attrs.get(key, default)

        if isinstance(self.tag, list):
            if key is None:
                x = [i.attrs for i in self.tag if isinstance(self.tag[0], Tag)]
            else:
                x = [i.attrs.get(key, default) for i in self.tag if isinstance(self.tag[0], Tag)]
            if not x:
                return default
            elif len(x) == 1:
                return x[0]
            else:
                return x

        return default


class Parser:

    escape = {
        '&quot;': '"'
    }

    def __init__(self, text: str = None):
        self._text = text
        self._execjs = None

    def __str__(self):
        return f'{self.__class__.__name__} {self._text})'

    def __getitem__(self, index):
        return self.__class__(self._text[index])

    def __len__(self):
        return len(self._text)

    __repr__ = __str__

    @property
    def text(self) -> str:
        if self._text is None:
            return ''
        if isinstance(self._text, str):
            return self._text
        text = self._text.text()
        for k, v in self.escape.items():
            text = text.replace(k, v)
        return text

    def json(self) -> dict:

        def parse_json(content, max_attempts=3):

            if isinstance(content, dict):
                return content

            attempts = 0
            while attempts < max_attempts:
                try:
                    if isinstance(content, dict):
                        return content
                    parsed_json = json.loads(content)
                    if isinstance(parsed_json, str):
                        content = re.sub(r'\\u[\da-zA-Z]+', '', parsed_json)
                    else:
                        return parsed_json
                except json.decoder.JSONDecodeError:
                    content = {}
                attempts += 1
            return {}

        text = self.strip_text()

        if text is None:
            return {}
        
        if not text:
            return {}

        return parse_json(text)

    def jsonp(self):

        if self.text is None:
            return {}

        if not self.text:
            return {}

        text = '{' + re_text(self.text, r'\{(.*)\}') + '}'

        try:
            return json.loads(text)
        except json.decoder.JSONDecodeError:
            return {}

    def strip_text(self, strip: Optional[str] = None, callback: Callable[[str], str] = None) -> str:
        text = self.text.strip() if strip is None else self.text.strip(strip)
        return callback(text) if callback is not None else text
    
    @property
    def execjs(self):
        if self._execjs is None:
            self._execjs = execjs.compile(self.text)
        return self._execjs

    def eval(self, name):
        return self.execjs.eval(name)

    def call_method(self, name, *args):
        return self.execjs.call(name, *args)

    def extract_first(self):
        return self.__class__(self._text.extract_first())

    def extract_last(self):
        return self.__class__(self._text.extract_last())

    def extract(self):
        return [self.__class__(i) for i in self._text.extract()]
    
    def extract_text(self):
        return [self.__class__(i).text for i in self._text.extract()]

    def re(self, query: str, flags: int = 0) -> _Parser:

        if self._text is None:
            return self

        if isinstance(self._text, ReParser):
            return self.__class__(self._text.re(query, flags=flags))

        if isinstance(self._text, XpathParser):
            return self.__class__(ReParser(self.text).re(query, flags=flags))

        if isinstance(self._text, CssParser):
            return self.__class__(ReParser(self.text).re(query, flags=flags))

        return self.__class__(ReParser(self._text).re(query, flags=flags))

    def xpath(self, query: str, **kwargs: dict) -> _Parser:

        if self._text is None:
            return self

        if isinstance(self._text, XpathParser):
            return self.__class__(self._text.xpath(query, **kwargs))

        if isinstance(self._text, ReParser):
            return self.__class__(XpathParser(self.text).xpath(query, **kwargs))

        if isinstance(self._text, CssParser):
            return self.__class__(XpathParser(self.to_string()).xpath(query, **kwargs))

        return self.__class__(XpathParser(self._text).xpath(query, **kwargs))

    def css(self, query: str, **kwargs: dict) -> _Parser:

        if self._text is None:
            return self

        if isinstance(self._text, CssParser):
            return self.__class__(self._text.css(query, **kwargs))

        if isinstance(self._text, XpathParser):
            return self.__class__(self.to_string())

        if isinstance(self._text, ReParser):
            return self.__class__(self.text)

        return self.__class__(CssParser(self._text).css(query, **kwargs))

    @property
    def empty(self):
        return self._text.empty()

    def remove_tags(self, tags: Union[str, list]):
        if isinstance(self._text, XpathParser):
            self._text = self._text.remove_tags(tags)
        return self

    def get_follow_tags(self, tag: str = None, n: int = None):
        if isinstance(self._text, XpathParser):
            self._text = self._text.get_follow_tags(tag=tag, n=n)
        return self

    def get_preced_tags(self, tag: str = None, n: int = None):
        if isinstance(self._text, XpathParser):
            self._text = self._text.get_preced_tags(tag=tag, n=n)
        return self

    def to_string(self, encoding='unicode', delete: Union[str, list] = '\n'):

        if isinstance(self._text, (XpathParser, CssParser)):
            return self._text.to_string(encoding=encoding, delete=delete)

        return ''
    
    def attrs(self, key: str = None, default=None):
        
        if isinstance(self._text, CssParser):
            return self.__class__(self._text.attrs(key=key, default=default))

        return None
