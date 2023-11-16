#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/12/8 0:32
# @Author : xiang
# @File : c_date
# @Project : caishengxiang
"""
描述：
"""
from datetime import datetime, timedelta,date
import calendar


def get_previous_day_by_week(dayname, end_date=None):
    """
    查找最后一个星期五的日期。
    算法：
    先将开始日期和目标日期映射到星期数组的位置上(星期一索引为0)， 然后通过模运算计算出目标日期要经过多少天才能到达开始日期。然后用开始日期减去那个时间差即得到结果日期。
    :param dayname:
    :param end_date:
    :return:
    """
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday']

    if end_date is None:
        end_date = datetime.today()
    day_num = end_date.weekday()  # 0~6 一~日
    day_num_target = weekdays.index(dayname)  # 对应list索引
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = end_date - timedelta(days=days_ago)
    return target_date


def get_month_range(start_date=None):
    """获取当前日期范围"""
    print('当前日期:', date.today())
    if start_date is None:
        start_date = date.today().replace(day=1)  # 将日替换成1
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)  # 返回两个整数组成的元组，第一个是该月的第一天是星期几，第二个是该月的天数。
    end_date = start_date + timedelta(days=days_in_month)  # 生成一个时间差
    print('本月1号与下月1号', start_date, end_date)
    return (start_date, end_date)


if __name__ == '__main__':
    print(get_previous_day_by_week('Monday'))
    print(get_previous_day_by_week('Sunday', datetime(2012, 12, 21)))
    print(get_month_range())
