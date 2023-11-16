from .translate.baidu import BaiduTranslate


def translate(query):
    """翻译"""
    return BaiduTranslate(query).translate()
