__all__ = [
    'strtime_to_stamp', 'stamp_to_strtime', 'strtime_to_time', 'stamp_to_time', 'time_to_stamp',
    'before_day', 'make_date_range', 'make_timestamp'
]

import re
import time
from typing import Optional, Union, List, Callable
from datetime import datetime, date, timedelta, time as dtime

import pandas as pd


class TimeConverter:
    """
    时间转换器：时间字符串、时间戳、日期时间对象相互转换
        >>> print(TimeConverter.strtime_to_stamp('2022/02/15 10:12:40'))
        >>> print(TimeConverter.stamp_to_strtime(1658220419111))
        >>> print(TimeConverter.strtime_to_time('2022/02/15 10:12:40'))
        >>> print(TimeConverter.stamp_to_time(1658220419111.222))
    """

    DATE_FORMATS = [
        "%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d",
        "%Y%m%d %H:%M:%S.%f", "%Y%m%d %H:%M:%S", "%Y%m%d %H:%M", "%Y%m%d",
        '%H:%M:%S.%f', '%H:%M:%S'
    ]

    @classmethod
    def _find_matching_format(cls, str_time: str) -> Optional[str]:
        for fmt in cls.DATE_FORMATS:
            try:
                datetime.strptime(str_time, fmt)
                return fmt
            except ValueError:
                continue
        return None

    @classmethod
    def _to_datetime(cls, str_time: str, format: str = None) -> Optional[datetime]:

        if not str_time or not isinstance(str_time, str):
            return None

        str_time = str_time.strip()

        if format is not None:
            return datetime.strptime(str_time, format)

        str_time = re.sub('[年月/]', '-', str_time)
        str_time = re.sub('[日]', '', str_time)

        matching_format = cls._find_matching_format(str_time)
        return datetime.strptime(str_time, matching_format) if matching_format else None

    @classmethod
    def strtime_to_stamp(cls, str_time: str, format: str = None, millisecond: bool = False) -> Optional[int]:
        """
        时间字符串转时间戳
        Args:
            str_time: 时间字符串
            format: 时间字符串格式
            millisecond: 默认为Flase，返回类型为秒级时间戳；若指定为True，则返回毫秒级时间戳
        Return:
            时间戳，默认为秒级
        """
        dt = cls._to_datetime(str_time, format)
        return int(dt.timestamp() * 1000) if dt and millisecond else int(dt.timestamp())

    @classmethod
    def stamp_to_strtime(cls, time_stamp: Union[int, float, str], format='%Y-%m-%d %H:%M:%S') -> Optional[str]:
        """
        时间戳转时间字符串，支持秒级（10位）和毫秒级（13位）时间戳自动判断
        Args:
            time_stamp: 时间戳 ex: 秒级：1658220419、1658220419.111222 毫秒级：1658220419111、1658220419111。222
            format: 时间字符串格式
        Return:
            时间字符串, ex: 2022-07-19 16:46:59   东八区时间
        """

        if time_stamp is None or not isinstance(str_time, (int, float, str)):
            return None

        if isinstance(time_stamp, str) and time_stamp.isdigit():
            time_stamp = float(time_stamp)

        if len(str(time_stamp).split('.')[0]) <= len(str(int(time.time()))):
            return time.strftime(format, time.localtime(time_stamp))
        elif len(str(time_stamp).split('.')[0]) <= len(str(int(time.time() * 1000))):
            return time.strftime(format, time.localtime(time_stamp / 1000))
        else:
            return None

    @classmethod
    def strtime_to_time(
            cls, str_time: str, format: str = None, is_date: bool = False, is_time: bool = False
    ) -> Union[datetime, date, dtime, None]:
        """
        时间字符串转日期时间类型
        Args:
            str_time: 时间字符串
            format: 时间格式化字符串
            is_date: 是否返回日期，默认返回日期时间
        Return:
            日期时间
        """
        dt = cls._to_datetime(str_time, format)
        if not dt:
            return dt
        elif is_date:
            return dt.date()
        elif is_time:
            return dt.time()
        else:
            return dt

    @classmethod
    def stamp_to_time(
            cls, time_stamp: Union[int, float, str], tz: str = None, is_date: bool = False, zone: str = '+8:00'
    ) -> Union[datetime, date, None]:
        """
        时间戳转时间字符串，支持秒级（10位）和毫秒级（13位）时间戳自动判断
        Args:
            time_stamp: 时间戳 ex: 秒级：1658220419、1658220419.111222 毫秒级：1658220419111、1658220419111。222
            tz: 时区，默认为中国标准时
            is_date: 是否返回日期，默认返回日期时间
            zone: 时区
        Return:
            日期时间对象
        """

        if time_stamp is None or not isinstance(time_stamp, (int, float, str)):
            return None

        if isinstance(time_stamp, str):
            time_stamp = float(time_stamp)

        if len(str(time_stamp).split('.')[0]) <= len(str(int(time.time()))):
            dt = datetime(1970, 1, 1) + timedelta(seconds=time_stamp)
        elif len(str(time_stamp).split('.')[0]) <= len(str(int(time.time() * 1000))):
            dt = datetime(1970, 1, 1) + timedelta(milliseconds=time_stamp)
        else:
            return None

        dt += timedelta(hours=int(zone.split(':')[0]))
        return dt.date() if is_date else dt

    @classmethod
    def time_to_stamp(cls, time: Union[datetime, date], millisecond: bool = False) -> int:
        """
        时间序列转时间戳，支持秒级和毫秒级时间戳自动判断
        Args:
            time: 时间序列
            millisecond: 是否返回毫秒级时间戳
        Return:
            时间戳
        """

        if not isinstance(time, (datetime, date)):
            return None

        if isinstance(time, date):
            time = datetime(time.year, time.month, time.day)

        return int(time.timestamp() * 1000) if millisecond else int(time.timestamp())


def strtime_to_stamp(str_time: str, format: str = None, millisecond: bool = False) -> Optional[int]:
    """
    时间字符串转时间戳
    Args:
        str_time: 时间字符串
        format: 时间字符串格式
        millisecond: 默认为Flase，返回类型为秒级时间戳；若指定为True，则返回毫秒级时间戳
    Return:
        时间戳，默认为秒级
    """
    return TimeConverter.strtime_to_stamp(str_time, format=format, millisecond=millisecond)


def stamp_to_strtime(time_stamp: Union[int, float, str], format='%Y-%m-%d %H:%M:%S') -> Optional[str]:
    """
    时间戳转时间字符串，支持秒级（10位）和毫秒级（13位）时间戳自动判断
    Args:
        time_stamp: 时间戳 ex: 秒级：1658220419、1658220419.111222 毫秒级：1658220419111、1658220419111。222
        format: 时间字符串格式
    Return:
        时间戳，时间字符串, ex: 2022-07-19 16:46:59   东八区时间
    """
    return TimeConverter.stamp_to_strtime(time_stamp, format=format)


def strtime_to_time(
        str_time: str, format: str = None, is_date: bool = False, is_time: bool = False
) -> Union[datetime, date, dtime, None]:
    """
    时间字符串转日期时间类型
    Args:
        str_time: 时间字符串
        format: 时间格式化字符串
        is_date: 是否返回日期类型，默认为 False
    Return:
        日期时间
    """
    return TimeConverter.strtime_to_time(str_time, format=format, is_date=is_date, is_time=is_time)


def stamp_to_time(
        time_stamp: Union[int, float, str], is_date: bool = False, zone: str = '+8:00'
) -> Union[datetime, date, None]:
    """
    时间戳转时间字符串，支持秒级（10位）和毫秒级（13位）时间戳自动判断
    Args:
        time_stamp: 时间戳 ex: 秒级：1658220419、1658220419.111222 毫秒级：1658220419111、1658220419111。222
        is_date: 是否返回日期类型，默认为 False
        zone: 时区
    Return:
        日期时间对象, ex: 2022-07-19 16:46:59
    """
    return TimeConverter.stamp_to_time(time_stamp, is_date=is_date)


def time_to_stamp(time: Union[datetime, date], millisecond: bool = False) -> int:
    """
    时间序列转时间戳，支持秒级和毫秒级时间戳自动判断
    Args:
        time: 时间序列
        millisecond: 是否返回毫秒级时间戳
    Return:
        时间戳
    """

    return TimeConverter.time_to_stamp(time, millisecond=millisecond)


def before_day(
        now: Optional[datetime] = None, before: int = 0, is_date: bool = False, is_str: bool = False
) -> Union[datetime, date, str]:
    """
    获取时间间隔
    Args:
        now: 时间，默认为 None，表示当前时间
        before: 时间，默认为 None，表示今天，-1 为昨天，1 为明天
        is_date: 是否返回日期对象
    Return:
        时间对象
    """

    if now is None:
        now = datetime.now()

    dt = now - timedelta(days=before)

    if is_date:
        dt = dt.date()

    if is_str:
        dt = str(dt)

    return dt


def make_date_range(
        start: Union[int, str, date] = 0, end: Union[int, str, date] = 0, skip: Union[bool, Callable] = None
) -> List[date]:
    def skip_weekend(date_list):
        return [i for i in date_list if i.weekday() not in [5, 6]]

    if isinstance(start, int):
        start = before_day(is_date=True, before=-start)

    if isinstance(end, int):
        end = before_day(is_date=True, before=-end)

    date_list = [i.date() for i in pd.date_range(start, end).to_list()]

    if skip is None:
        return date_list
    elif skip is True:
        return skip_weekend(date_list)
    else:
        return skip(date_list)


def make_timestamp(millisecond: bool = True, to_string: bool = False) -> Union[int, str]:
    """
    获取时间戳
    Args:
        millisecond: 是否获取毫秒时间戳
        to_string: 结果是否返回字符串类型
    Return:
        时间戳，返回类型和输入参数有关系
    """

    if to_string:
        return str(int(time.time() * 1000) if millisecond else int(time.time()))

    return int(time.time() * 1000) if millisecond else int(time.time())


def get_quarter_end_dates(start_year: int, end_year: int) -> List[str]:
    """
    获取区间内每个季度的最后一天
    Args:
        start_year: 开始年份
        end_year: 结束年份
    Rerutn:
        返回季度最后一天日期列表
    """

    return [
        str(date(year, month, day))
        for year in range(start_year, end_year + 1)
        for quarter, (month, day) in {
            1: (3, 31), 2: (6, 30), 3: (9, 30), 4: (12, 31)
        }.items()
    ]


def get_next_month_same_day(current_date: Union[str, datetime], is_date=False) -> Union[date, datetime]:
    if isinstance(current_date, str):
        current_date = strtime_to_time(current_date)

    year = current_date.year
    month = current_date.month
    day = current_date.day
    time = current_date.time()

    if month == 12:
        next_month = 1
        year += 1
    else:
        next_month = month + 1

    days_in_next_month = 31 if next_month in [1, 3, 5, 7, 8, 10, 12] else (
        30 if next_month != 2 else 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28
    )

    day = min([day, days_in_next_month])

    return date(year, next_month, day) if is_date else datetime(
        year, next_month, day, time.hour, time.minute, time.second
    )

