__all__ = ['LoadBrowser']

from typing import Callable

from AioSpider.constants import BrowserType, By, SignalType
from AioSpider.signal import Signal

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Browser:

    def __init__(self, browser):
        self.browser = browser
        Signal().connect(SignalType.browser_quit, self.quit)

    def goto(self, url):
        self.browser.get(url)

    def refresh(self):
        self.browser.execute_script("location.reload()")

    def execute_js(self, js):
        return self.browser.execute_script(js)

    def get_cookies(self) -> dict:
        return {i['name']: i['value'] for i in self.browser.get_cookies()}

    def find_element(self, query: str, by: By):
        return self.browser.find_element(by=by, value=query)

    def find_elements(self, query: str, by: By):
        return self.browser.find_element(by=by, value=query)

    def get_page_source(self):
        return self.browser.page_source

    def implicitly_wait(self, timeout: int):
        self.browser.implicitly_wait(timeout)

    def wait_until(
            self, timeout: int, callback: Callable, msg: str = None, frequency: int = 0.5,
            ignored_exceptions=None
    ):
        return WebDriverWait(self.browser, timeout, frequency, ignored_exceptions).until(callback, msg)

    def quit(self):
        if self.browser is None:
            return
        self.browser.quit()

    def __del__(self):
        self.quit()
