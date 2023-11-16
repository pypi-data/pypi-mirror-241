from urllib import parse


def extract_params(url: str) -> dict:
    """
    从 url 中提取参数
    Args:
        url: url
    Return:
        从 url 中提取的参数
    """

    params_query = parse.urlparse(url).query
    return {i[0]: i[-1] for i in parse.parse_qsl(params_query)}


def extract_url(url: str) -> str:
    """
    从url中提取接口
    Args:
        url: url
    Return:
        接口
    """

    url_parse = parse.urlparse(url)
    return f'{url_parse.scheme}://{url_parse.netloc}{url_parse.path}'


def extract_path(url: str) -> str:
    """
    从url中提取接口路径
    Args:
        url: url
    Return:
        接口路径
    """
    return parse.urlparse(url).path


def format_cookies(cookies: str) -> dict:
    """
    格式化cookies
    Args:
        cookies: cookies文本字符串，可以是浏览器请求头中复制出来的
    Return:
        返回格式化的cookies
    """

    return {
        i.split('=')[0].strip(): i.split('=')[-1].strip()
        for i in cookies.split(';') if i.split('=')[0].strip() and i.split('=')[-1].strip()
    }


def quote_params(params: dict) -> str:
    """
    转换并压缩 params 参数
    Args:
        params: 待转换数据
    Return:
        转换后可拼接到 url 的字符串
    """
    return parse.urlencode({i: params[i] for i in sorted(params.keys())})


def quote_url(url: str, params: dict) -> str:
    """
    拼接 params 参数到 url
    Args:
        url: url
        params: 待转换数据
    Return:
        拼接的 url
    """
    return url + '?' + quote_params(params)