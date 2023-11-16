#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/12/8 0:50
# @Author : xiang
# @File : time_type
# @Project : caishengxiang
"""
描述：时间类型转换
"""
import time
from datetime import datetime


def str_to_timestamp(time_str: str, time_format="%Y-%m-%d %H:%M:%S") -> float:
    """字符串转时间戳"""
    stamp = time.mktime(time.strptime(time_str, time_format))
    return stamp


def timestamp_to_str(stamp: float, time_format="%Y-%m-%d %H:%M:%S") -> str:
    """时间戳转字符串"""
    time_str = time.strftime(time_format, time.localtime(stamp))
    return time_str


def datetime_to_str(dtime: datetime, time_format="%Y-%m-%d %H:%M:%S") -> str:
    """datetime转字符串"""
    time_str = dtime.strftime(time_format)
    return time_str


def str_to_datetime(time_str: str, time_format="%Y-%m-%d %H:%M:%S") -> datetime:
    """字符串转datetime"""
    dtime = datetime.strptime(time_str, time_format)
    return dtime


def datetime_to_timestamp(dtime: datetime):
    """datetime转时间戳"""
    stamp = time.mktime(dtime.timetuple())
    return stamp


def timestamp_to_datetime(stamp: float) -> datetime:
    """时间戳转datetime"""
    dtime = datetime.fromtimestamp(stamp)
    return dtime


if __name__ == '__main__':
    print(str_to_timestamp('2018-08-07 15:40:30'))
    print(timestamp_to_str(time.time()))
    print(datetime_to_str(datetime.now()))
    print(str_to_datetime('2018-08-07 15:40:30'))
    print(datetime_to_timestamp(datetime.now()))
    print(timestamp_to_datetime(time.time()))
