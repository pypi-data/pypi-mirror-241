__all__ = [
    'AioSpiderPath', 'LoggingConfig', 'SpiderRequestConfig', 'ConcurrencyStrategyConfig',
    'ConnectPoolConfig', 'RequestProxyConfig', 'MIDDLEWARE', 'DataFilterConfig', 
    'RequestFilterConfig', 'BrowserConfig', 'DataBaseConfig', 'MessageNotifyConfig'
]


from AioSpider.constants import *


# ---------------------------------- 系统相关配置 ---------------------------------- #

AioSpiderPath = Path(__file__).parent                   # 工作路径


class LoggingConfig:
    """日志配置"""

    Console = {
        'engine': True,                                 # 是否打印到控制台
        'format': Formater.A,                           # 日志格式
        'time_format': TimeFormater.A,                  # 时间格式
        'level': LogLevel.DEBUG                         # 日志等级
    }
    File = {
        'engine': True,                                 # 是否写文件
        'path': AioSpiderPath / "log",                  # 日志存储路径
        'format': Formater.A,                           # 日志格式
        'time_format': TimeFormater.A,                  # 时间格式
        'level': LogLevel.DEBUG,                        # 日志等级
        'mode': WriteMode.A,                            # 写文件的模式
        'size': 50 * 1024 * 1024,                       # 每个日志文件的默认最大字节数
        'encoding': 'utf-8',                            # 日志文件编码
        'retention': '1 week',                          # 日志保留时间
        'compression': True                             # 是否将日志压缩
    }


class ServerConfig:
    
    master = {
        'enabled': False,
        'protocal': 'http',
        'host': '127.0.0.1',
        'port': 10087
    }
    slaver = {
        'protocal': 'http',
        'host': '0.0.0.0',
        'port': 10086
    }
    

# -------------------------------------------------------------------------------- #


# ---------------------------------- 爬虫相关配置 ---------------------------------- #

class SpiderRequestConfig:
    """爬虫请求配置"""

    REQUEST_USE_SESSION = False                     # 使用会话
    REQUEST_USE_METHOD = RequestWay.aiohttp         # 使用 aiohttp 库进行请求

    REQUEST_CONCURRENCY_SLEEP = {
        'strategy': SleepStrategy.fixed,
        'sleep': 1
    }                                               # 单位秒，每 task_limit 个请求休眠n秒
    PER_REQUEST_SLEEP = {
        'strategy': SleepStrategy.fixed,
        'sleep': 0
    }                                               # 单位秒，每并发1个请求时休眠1秒
    REQUEST_TIMEOUT = 5 * 60                        # 请求最大超时时间
    
    # 请求报错重试
    REQUEST_ERROR_RETRY_TIMES = 3                   # 请求报错重试次数
    REQUEST_ERROR_RETRY_SLEEP = 1                   # 请求报错重试间隔

    # 请求状态码异常重试
    MAX_STATUS_RETRY_TIMES = 3                      # 请求状态码异常最大重试次数
    RETRY_STATUS = [400, 403, 404, 500, 503]        # 请求状态码异常重试状态码列表
    
    # 请求失败重试
    MAX_FAILURE_RETRY_TIMES = 3                     # 请求失败最大重试次数

    DepthPriority = True                            # 深度优先

    RANDOM_HEADERS = True                           # 随机UserAgent
    # 默认请求头，优先级：spider headers > 默认headers > random headers
    HEADERS = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    # 字符串类型或可迭代对象，值为chrome, ie, opera, firefox, ff, safari，若指定RANDOM_HEADERS为True时则不生效
    USER_AGENT_TYPE = UserAgent.CHROME


class ConcurrencyStrategyConfig:
    """
    爬虫并发策略. auto 自动模式，系统不干预；random 随机模式，并发速度随机于最大和最
    小并发速度之间；smart 智能模式，系统自动调节
    """

    auto = {
        'enabled': False,                       # 是否启用
        'reference_limit': 20,                  # 基准并发数量 单位：个/秒
        'wave': 5,                              # 在基准上上下波动5分之一
    }
    random = {
        'enabled': False,                       # 是否启用
        'min_limit': 10,                        # 最小并发数量 单位：个/秒
        'max_limit': 30,                        # 最小并发数量 单位：个/秒
    }
    speed = {
        'enabled': False,                       # 是否启用
        'avg_speed': 20,                        # 平均并发速度 单位：个
    }
    time = {
        'enabled': True,                       # 是否启用
        'second': 3 * 60,                       # 运行时间
        'min_limit': 10,                        # 最小并发数量 单位：个/秒
        'max_limit': 30,                        # 最小并发数量 单位：个/秒
    }
    fix = {
        'enabled': False,                        # 是否启用
        'task_limit': 50                        # 任务并发数
    }


class ConnectPoolConfig:
    """连接池"""

    MAX_CONNECT_COUNT = 10                  # 请求最大连接数，指定为 True 时无限制
    USE_DNS_CACHE = True                    # 使用内部DNS映射缓存，用来查询DNS，使建立连接速度更快
    TTL_DNS_CACHE = 10                      # 查询过的DNS条目的失效时间，None表示永不失效
    FORCE_CLOSE = False                     # 连接释放后关闭底层网络套接字
    VERIFY_SSL = True                       # ssl证书验证
    LIMIT_PER_HOST = 0                      # 同一端点并发连接总数，同一端点是具有相同 host、port、ssl 信息，如果是0则不做限制


class RequestProxyConfig:
    """代理配置"""

    proxy_type = ProxyType.none                             # 代理类型
    config = {
        'appoint': {
            'address': None                                 # 手动代理地址，支持 str、list、tuple。未加协议自动补齐成http协议，None表示不适用代理
        },
        'pool': {
            'firstVerifySite': ProxyVerifySource.baidu,     # 代理首次验证源
            'strategy': ProxyPoolStrategy.balance           # 代理池分配策略
        },
    }

# -------------------------------------------------------------------------------- #


# ---------------------------------- 中间件相关配置 --------------------------------- #

MIDDLEWARE = {
    "AioSpider.middleware.download.FirstMiddleware": 100,           # 优先中间件
    "AioSpider.middleware.download.HeadersMiddleware": 101,         # 请求头中间件
    "AioSpider.middleware.download.LastMiddleware": 102,            # 最后中间件
    "AioSpider.middleware.download.RetryMiddleware": 103,           # 请求重试中间件
    "AioSpider.middleware.download.ProxyPoolMiddleware": 104,       # 代理池中间件
    "AioSpider.middleware.download.ExceptionMiddleware": 105,       # 异常中间件
}

# -------------------------------------------------------------------------------- #


# ---------------------------------- 去重相关配置 ---------------------------------- #

class DataFilterConfig:
    """数据去重"""

    TASK_LIMIT = 20                                          # 数据提交并发数
    COMMIT_SIZE = 1000                                       # 数据每批提交保存的数量
    MODEL_NAME_TYPE = 'smart'                                # lower / upper / smart，处理表名的方式

    ENABLED = False                                          # 是否启用数据去重
    LoadDataFromDB = False                                   # 从数据库加载含有唯一索引数据作为种子数据去重
    FILTER_METHOD = DataFilterMethod.dqset                   # 数据去重方式
    CACHED_ORIGIN_DATA = False                               # 是否启用缓存原始数据 数据量大的时候建议设置为True，每次启动将会自动去重
    BLOOM_INIT_CAPACITY = 10000                              # 布隆过滤器数据容量
    BLOOM_ERROR_RATE = 0.001                                 # 布隆过滤器误判率
    BLOOM_MAX_CAPACITY = 5000 * 10000                        # 布隆过滤器数据容量


class RequestFilterConfig:
    """URL去重"""

    Enabled = True,                                          # 是否缓存爬过的请求 将爬过的请求缓存到本地
    LoadSuccess = True                                       # 将CACHED_REQUEST缓存中成功的请求加载到队列
    ExpireTime = 60 * 60 * 24                                # 缓存时间 秒
    CachePath = AioSpiderPath / "cache"                      # 数据和资源缓存路径
    FilterForever = True                                     # 是否永久去重，配置此项 CACHED_EXPIRE_TIME 无效

    IgnoreStamp = True                                       # 去重忽略时间戳
    ExcludeStamp = ['_']                                     # 时间戳字段名，一般指请求中params、data中的参数

# -------------------------------------------------------------------------------- #


# ---------------------------------- 浏览器相关配置 ---------------------------------- #

class BrowserConfig:
    """浏览器配置"""

    class Chromium:

        enabled = False                                      # 是否开启浏览器
        LogLevel = 3                                         # 日志等级
        Proxy = None                                         # 代理
        headless = False                                     # 是否无头模式
        Options = None                                       # 启动参数
        UserAgent = None                                     # user_agent
        ProfilePath = None                                   # 用户数据路径
        ExtensionPath = None                                 # 拓展应用路径
        DisableImages = False                                # 禁用图片
        DisableJavaScript = False                            # 禁用js
        ExecutePath = Browser.CHROMIUM_DRIVER_PATH           # chrome webdriver 路径
        BinaryPath = Browser.CHROMIUM_BINARY_PATH            # 浏览器路径
        DownloadPath = AioSpiderPath / "download"            # 下载路径
        ImplicitlyWait = 0                                   # 隐式等待时间

    class Firefox:

        enabled = False                                      # 是否开启浏览器
        LogLevel = 3                                         # 日志等级
        Proxy = None                                         # 代理
        headless = False                                     # 是否无头模式
        Options = None                                       # 启动参数
        UserAgent = None                                     # user_agent
        ProfilePath = None                                   # 用户数据路径
        ExtensionPath = None                                 # 拓展应用路径
        DisableImages = False                                # 禁用图片
        DisableJavaScript = False                            # 禁用js
        ExecutePath = Browser.FIREFOX_DRIVER_PATH            # chrome webdriver 路径
        BinaryPath = Browser.FIREFOX_BINARY_PATH             # 浏览器路径
        DownloadPath = AioSpiderPath / "download"            # 下载路径
        ImplicitlyWait = 0                                   # 隐式等待时间

# -------------------------------------------------------------------------------- #


# --------------------------------- 数据库相关配置 --------------------------------- #

class DataBaseConfig:
    """数据库配置"""

    Csv = {
        'enabled': False,
        'CONNECT': {
            'DEFAULT': {
                'CSV_PATH': AioSpiderPath / 'data',		     # 数据目录
                'ENCODING': 'utf-8',					     # 文件写入编码
            },
        },
        'installs': {
            'DEFAULT': []
        },                                                   # 注册内置模型
    }

    Sqlite = {
        'enabled': False,
        'CONNECT': {
            'DEFAULT': {
                'SQLITE_PATH': AioSpiderPath / 'data',	     # 数据库目录
                'SQLITE_DB': "aioSpider",			 	     # 数据库名称
                'CHUNK_SIZE': 20 * 1024 * 1024,		  	     # 每批允许写入最大字节数
                'SQLITE_TIMEOUT': 10						 # 连接超时时间
            },
        },
        'installs': {
            'DEFAULT': []
        },                                                   # 注册内置模型
    }

    Mysql = {
        'enabled': False,
        'CONNECT': {
            'DEFAULT': {
                'MYSQL_HOST': "127.0.0.1",		             # 域名
                'MYSQL_PORT': 3306,						     # 端口
                'MYSQL_DB': "",							     # 数据库名
                'MYSQL_USER_NAME': "",				         # 用户名
                'MYSQL_USER_PWD': "",		                 # 密码
                'MYSQL_CHARSET': "utf8mb4",		             # 数据库字符集
                'MYSQL_CONNECT_TIMEOUT': 10,                 # 连接超时时间
                'MYSQL_TIME_ZONE': '+8:00',	                 # 时区
                'MYSQL_MIN_CONNECT_SIZE': 10,                # 连接池最小连接数
                'MYSQL_MAX_CONNECT_SIZE': 20,                # 连接池最大连接数
            }
        },
        'installs': {
            'DEFAULT': []
        },                                                   # 注册内置模型
    }

    Mongodb = {
        'enabled': False,
        'CONNECT': {
            'DEFAULT': {
                'MONGO_HOST': "",	                         # 域名
                'MONGO_PORT': 27017,		                 # 端口
                'MONGO_DB': "",			                     # 存储数据库名
                'MONGO_AUTH_DB': "admin",	                 # 用于验证的数据库名称，通常是存储用户名和密码的数据库 默认 admin
                'MONGO_USERNAME': "",				         # 用户名
                'MONGO_PASSWORD': "",				         # 密码
                'MONGO_MIN_CONNECT_SIZE': 0,				 # 连接池的最小连接数
                'MONGO_MAX_CONNECT_SIZE': 100,	             # 连接池的最大连接数
                'MONGO_MAX_IDLE_TIME': 0,				     # 一个连接在连接池中空闲多久后会被关闭，单位秒 0: 不关闭
            }
        },
        'installs': {
            'DEFAULT': []
        },                                                   # 注册内置模型
    }

    File = {
        'enabled': False,
        'CONNECT': {
            'DEFAULT': {
                'FILE_PATH': AioSpiderPath / 'data',         # 数据目录
                'ENCODING': 'utf-8',					     # 文件写入编码
                'WRITE_MODE': WriteMode.WB			         # 文件写入模式
            },
        },
        'installs': {
            'DEFAULT': []
        },                                                   # 注册内置模型
    }

    Redis = {
        'enabled': False,
        'CONNECT': {
            'DEFAULT': {
                'host': '127.0.0.1',  			             # 域名
                'port': 6379,					             # 端口
                'username': None,				             # 用户名
                'password': None,				             # 密码
                'db': 0,						             # 数据库索引
                'encoding': 'utf-8', 			             # 编码
                'max_connections': 1 * 10000                 # 最大连接数
            }
        },
        'installs': {
            'DEFAULT': []
        },                                                   # 注册内置模型
    }

# -------------------------------------------------------------------------------- #


# ---------------------------------- 消息通知配置 ---------------------------------- #

class MessageNotifyConfig:
    system = {
        'enabled': False,                                   # 是否开启
        'type': NoticeType.wechat,                          # 机器人类型
        'token': '',                                        # 企业微信机器人token
        'sender': "",                                       # 通知人
        'receiver': [],                                     # 接收者 将会在群内@此人
        'interval': 60,                                     # 相同报警的报警时间间隔，防止刷屏
        'level': LogLevel.WARNING,                          # 报警级别， DEBUG / ERROR
    }
    robot1 = {
        'enabled': False,
        'type': NoticeType.dingding,
        'api': '',                                          # 钉钉机器人api
        'token': '',                                        # 钉钉机器人token
        'sender': "",                                       # 通知人
        'receiver': [],                                     # 接收者 将会在群内@此人, 支持列表，可指定多人
        'interval': 60,                                     # 相同报警的报警时间间隔，防止刷屏
        'level': LogLevel.WARNING,                          # 报警级别， DEBUG / ERROR
    }
    robot2 = {
        'enabled': False,
        'type': NoticeType.email,
        'smtp': "smtp.qq.com",                              # 邮件服务器 默认为qq邮箱
        'port': 587,                                        # 端口号
        'sender': "",                                       # 发件人
        'token': "",                                        # 授权码
        'receiver': [],                                     # 接收者
        'interval': 60,                                     # 相同报警的报警时间间隔，防止刷屏
        'level': LogLevel.WARNING,                          # 报警级别， DEBUG / ERROR
    }

# -------------------------------------------------------------------------------- #
