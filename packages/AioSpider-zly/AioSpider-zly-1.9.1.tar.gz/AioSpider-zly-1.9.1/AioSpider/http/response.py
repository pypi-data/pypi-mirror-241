import platform
from typing import Optional
from pathlib import Path

import execjs
try:
    from cchardet import detect
except ModuleNotFoundError:
    from chardet import detect
    
from AioSpider.tools.tools import parse_json
from AioSpider.tools.html_tools import open_html
from AioSpider.tools.network_tools import extract_url
from AioSpider.constants import By
from AioSpider.parse import Parser

from .request import Request


class Response:
    """响应对象"""

    url = None
    text = None

    def __init__(
            self, status: int = 200, headers: Optional[dict] = None, content: bytes = None,
            request: Optional[Request] = None, browser=None, **kwargs
    ):

        self.headers = headers
        self.content = content
        self.status = status

        if request is None:
            self.request = Request('')
        else:
            self.request = request
            self._set_attr_from_request()
        self.__browser = browser

        for k in kwargs:
            setattr(self, k, kwargs[k])

        self.parser = Parser(self.text)

    def __str__(self):

        if self.request.help:
            s = f'Response <{self.request.help} {self.status} {self.request.method} {extract_url(self.url)}>'
        else:
            s = f'Response <{self.status} {self.request.method} {extract_url(self.url)}>'

        return s

    def _set_attr_from_request(self):
        """将request的属性绑定到response实例上"""

        self.url = self.request.url
        self._set_text()

        for attr in self.request.meta:
            setattr(self, attr, self.request.meta[attr])

    def _set_text(self):

        request = self.request
        content = self.content

        if not content:
            return None

        if hasattr(request, 'encoding') and request.encoding:
            encoding = request.encoding
        else:
            encoding = detect(content)["encoding"]
            encoding = encoding if encoding else (request.encoding or 'utf-8')
            encoding = "GB18030" if encoding.upper() in ("GBK", "GB2312") else encoding

        try:
            self.text = content.decode(encoding, "replace")
        except MemoryError:
            self.text = content.decode(encoding, "ignore")

    def re(self, regex, flags: int = 0) -> Parser:
        return Parser(self.text).re(regex, flags=flags)

    def xpath(self, query, **kwargs) -> Parser:
        return self.parser.xpath(query, **kwargs)
    
    def css(self, query, **kwargs) -> Parser:
        return self.parser.css(query, **kwargs)

    @property
    def json(self):
        return self.parser.json()

    @property
    def jsonp(self):
        return self.parser.jsonp()

    def eval(self, name):
        return self.parser.eval(name)

    def call_method(self, name, *args):
        return self.parser.call_method(name, *args)

    @property
    def browser(self):
        return self.__browser

    def goto(self):
        self.__browser.goto(self.request.url)

    def find_element(self, query: str = None, by: str = None):

        if by is None:
            by = By.XPATH

        return self.__browser.find_element(query, by)

    def find_elements(self, query: str = None, by: str = None):

        if by is None:
            by = By.XPATH

        return self.__browser.find_element(query, by)
    
    def render(self):

        if platform.system() == 'Windows':
            bin_path = Path(r'C:\$Recycle.Bin')
        elif platform.system() == 'Linux':
            bin_path = Path(r'~/.local/share/Trash')
        else:
            raise Exception('Unknown platform')

        try:
            (bin_path / 'tmp.html').write_text(self.text, encoding='utf-8')
        except:
            (bin_path / 'tmp.html').write_text(self.text, encoding='gbk')

        open_html(bin_path / 'tmp.html')

    def render_text(self):
        self.text = self.__browser.get_page_source()
        self.parser = Parser(self.text)

    def execute_js(self, js):
        return self.__browser.execute_js(js)
        
    def parse_json(self, index, default=None, callback=None):
        return parse_json(self.json, index, default=default, callback=callback)
    
    def set_text(self, text):
        self.text = text
        self.parser = Parser(self.text)
