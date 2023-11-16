import os
from typing import Union
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from AioSpider.constants import Browser

from .file_tools import mkdir


def firefox_instance(
    executable_path: Union[str, Path] = None,
    binary_path: Union[str, Path] = None,
    headless: bool = False,
    proxy: str = None,
    options: dict = None,
    extension_path: Union[str, Path] = None,
    user_agent: str = None,
    download_path: Union[str, Path] = None,
    profile_path: Union[Path, str] = None,
    disable_images: bool = False,
):

    def to_str(path: Union[str, Path]) -> str:
        return str(path) if path is not None else None

    executable_path = to_str(executable_path)
    binary_path = to_str(binary_path)
    download_path = to_str(download_path)
    extension_path = to_str(extension_path)
    profile_path = to_str(profile_path)

    if options is None:
        options = {}

    if profile_path is None:
        profile_path = str(Path(fr'{os.getenv("AppData")}') / r'Mozilla/Firefox/Profiles/8qrydh7k.default-release-1')
        mkdir(profile_path, auto=False)

    if binary_path is None:
        binary_path = str(Browser.FIREFOX_BINARY_PATH)

    firefox_options = FirefoxOptions()

    firefox_options.binary_location = binary_path
    profile = webdriver.FirefoxProfile(profile_path)

    if headless:
        firefox_options.add_argument("--headless")
    if user_agent is not None:
        firefox_options.add_argument(f'--user-agent={user_agent}')
    if extension_path is not None:
        firefox_options.add_extension(extension_path)
    if disable_images:
        profile.set_preference("permissions.default.image", 2)
    if download_path is not None:
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.dir", download_path)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "binary/octet-stream")

    if proxy is not None:

        if 'http://' in proxy:
            proxy_type = 'http'
            proxy_host, proxy_port = proxy.strip('http://').split(':')
            proxy_port = int(proxy_port)
        elif 'https://' in proxy:
            proxy_type = 'https'
            proxy_host, proxy_port = proxy.strip('https://').split(':')
            proxy_port = int(proxy_port)
        elif 'sock://' in proxy or 'sock4://' in proxy or 'sock5://' in proxy or 'sock5h://' in proxy:
            proxy_type = 'sock'
            proxy_host, proxy_port = proxy.split('://')[-1].split(':')
            proxy_port = int(proxy_port)
        else:
            proxy_type = 'http'
            proxy_host, proxy_port = proxy.split(':')
            proxy_port = int(proxy_port)

        if proxy_type in ("http", "https", "socks"):
            profile.set_preference('network.proxy.type', 1)
            proxy_preferences = {
                "http": {
                    'network.proxy.type': 1, 'network.proxy.http': proxy_host, 'network.proxy.http_port': proxy_port,
                    'network.proxy.ssl': proxy_host,'network.proxy.ssl_port': proxy_port
                },
                "https": {
                    'network.proxy.type': 1, 'network.proxy.https': proxy_host, 'network.proxy.https_port': proxy_port,
                    'network.proxy.ssl': proxy_host,'network.proxy.ssl_port': proxy_port
                },
                "socks": {
                    'network.proxy.type': 1, 'network.proxy.socks': proxy_host, 'network.proxy.socks_port': proxy_port
                }
            }
            for key, value in proxy_preferences[proxy_type].items():
                profile.set_preference(key, value)

    for k in options:
        profile.set_preference(k, options[k])

    profile.set_preference("network.http.use-cache", True)
    profile.set_preference("browser.cache.memory.enable", True)
    profile.set_preference("browser.cache.disk.enable", True)
    profile.update_preferences()

    service = Service(executable_path or Browser.FIREFOX_DRIVER_PATH)
    firefox_options.profile = profile

    driver = webdriver.Firefox(service=service, options=firefox_options)

    return driver


def chromium_instance(
        executable_path: Union[str, Path] = None, binary_path: Union[str, Path] = None, headless: bool = False,
        proxy: str = None, options: list = None, extension_path: Union[str, Path] = None, user_agent: str = None,
        download_path: Union[str, Path] = None, profile_path: Union[Path, str] = None, disable_images: bool = False,
        disable_javascript: bool = False, log_level: int = 3
):

    if options is None:
        options = []

    if profile_path is None:
        profile_path = str(Path(os.getenv("AppData")).parent / r'Local\Google\Chrome\User Data\Default')
        mkdir(profile_path, auto=False)

    chrome_options = ChromeOptions()

    chrome_options.binary_location = str(binary_path or Browser.CHROMIUM_BINARY_PATH)
    download_path = str(download_path or '')

    prefs = {
        'download.default_directory': download_path,
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'safebrowsing.enabled': False,
        'safebrowsing.disable_download_protection': True,
        'profile.default_content_setting_values': {}
    }

    if headless:
        chrome_options.add_argument("--headless")
    if proxy is not None:
        chrome_options.add_argument(f"--proxy-server={proxy}")
    if user_agent is not None:
        chrome_options.add_argument(f'--user-agent={user_agent}')
    if extension_path is not None:
        chrome_options.add_extension(str(extension_path))
    if disable_javascript:
        prefs['profile.default_content_setting_values']['javascript'] = 2
    if disable_images:
        prefs['profile.default_content_setting_values']['images'] = 2

    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

    chrome_options.add_argument(f"log-level={log_level}")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("disable-blink-features=AutomationControlled")
    chrome_options.add_argument(f"user-data-dir={profile_path}")

    for o in options:
        chrome_options.add_argument(o)

    service = Service(str(executable_path or Browser.CHROMIUM_DRIVER_PATH))
    driver = webdriver.Chrome(options=chrome_options, service=service)

    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_path}}
    driver.execute("send_command", params)

    return driver

