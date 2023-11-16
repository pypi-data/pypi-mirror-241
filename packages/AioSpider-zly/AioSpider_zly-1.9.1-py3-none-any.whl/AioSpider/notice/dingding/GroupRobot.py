import json
import base64
from typing import Union
from datetime import datetime

import requests


class Robot:
    """
        钉钉群机器人
        @document: https://open.dingtalk.com/document/group/message-types-and-data-format
    """

    def __init__(self, token):
        self.token = token
        self._key_word = None
        self._tpl = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\t\t'

    @property
    def key_word(self):
        return self._key_word

    def set_token(self, token: Union[str, list] = None):
        if isinstance(token, str):
            self._token = [token]
        elif isinstance(token, list):
            self._token = token
        else:
            raise Exception(f'token错误: {token}')

    def set_key_word(self, key_word: Union[str, list] = None):
        if isinstance(key_word, str):
            self._key_word = [key_word]
        elif isinstance(key_word, list):
            self._key_word = key_word
        else:
            print('key_word错误', key_word)

    def get_key_word(self, index: int):
        if index > len(self._key_word):
            raise Exception('关键词索引错误，超出范围')
        return self._key_word[index]

    def set_tpl(self, tpl: str = None):
        if isinstance(tpl, str):
            self._tpl = tpl

    def send_request(self, data: dict):

        url = 'https://oapi.dingtalk.com/robot/send?access_token=' + self.token
        res = requests.post(
            url, data=json.dumps(data), headers={"Content-Type": "application/json;charset=utf-8"}
        )

        if res.json()['errcode'] == 0:
            print('钉钉发送成功')
        else:
            print('钉钉发送失败')
            print(res.json())

    def send_text(
            self, text: str, at_all: bool = False, at_user_ids: list = None, at_mobiles: list = None, index: int = 0
    ):

        if at_user_ids is None:
            at_user_ids = []

        if at_user_ids is None:
            at_mobiles = []

        data = {
            "msgtype": "text",
            "text": {"content": self._tpl + self.get_key_word(index) + '\n' + text},
            'at': {"atMobiles": at_mobiles, "atUserIds": at_user_ids, 'isAtAll': at_all}
        }
        self.send_request(data)

    def send_link(self, title: str, text: str, link: str, pic_url: str = None, index: int = 0):

        if text is None:
            text = ''

        if pic_url is None:
            pic_url = ''

        data = {
            "msgtype": "link",
            "link": {
                "text": self._tpl + self.get_key_word(index) + '\n' + text,
                "title": title,
                "picUrl": pic_url,
                "messageUrl": link
            }
        }
        self.send_request(data)

    def send_markdown(
            self, title: str, text: str, at_all: bool = False, at_user_ids: list = None,
            at_mobiles: list = None, index: int = 0
    ):
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": self._tpl + self.get_key_word(index) + '\n' + text
            },
            "at": {
                "atMobiles": at_mobiles,
                "atUserIds": at_user_ids,
                "isAtAll": at_all
            }
        }
        self.send_request(data)

    def send_overall_card(self, title: str, text: str, link: str, single_title: str = '全文阅读', index: int = 0):
        data = {
            "msgtype": "actionCard",
            "actionCard": {
                "title": title,
                "text": self._tpl + self.get_key_word(index) + '\n' + text,
                "singleTitle": single_title,
                "singleURL": link
            }
        }
        self.send_request(data)

    def send_dependent_card(self, title: str, text: str, buttons: list = None, index: int = 0):
        """
        Args:
            title:
            text:
            index:
            buttons: [
                    {
                        "title": "内容不错",
                        "actionURL": "https://www.dingtalk.com/"
                    },
                    {
                        "title": "不感兴趣",
                        "actionURL": "https://www.dingtalk.com/"
                    }
                ]

        Returns:

        """
        data = {
            "msgtype": "actionCard",
            "actionCard": {
                "title": title,
                "text": self._tpl + self.get_key_word(index) + '\n' + text,
                "btnOrientation": "0",
                "btns": buttons
            }
        }
        self.send_request(data)

    def send_feed_card(self, title_list: list, message_url_list: list, pic_url_list: list, index: int = 0):

        links = []
        for t, m, p in zip(title_list, message_url_list, pic_url_list):
            links.append({
                "title": self._tpl + self.get_key_word(index) + '\n' + t,
                "messageURL": m,
                "picURL": p
            })

        data = {
            "msgtype": "feedCard",
            "feedCard": {
                "links": links
            }
        }
        self.send_request(data)
