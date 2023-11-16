#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/12/8 0:32
# @Author : xiang
# @File : c_dateutil
# @Project : caishengxiang
"""
描述：
对大多数基本的日期和时间处理问题， datetime 模块已经足够了。
如果你需要执行更加复杂的日期操作，
比如处理时区，模糊时间范围，节假日计算等等， 可以考虑使用 dateutil模块

许多类似的时间计算可以使用 dateutil.relativedelta() 函数代替。 但是，有一点需要注意的就是，
它会在处理月份(还有它们的天数差距)的时候填充间隙。看例子最清楚：
"""

try:
    from dateutil.relativedelta import relativedelta
except:
    print("pip install python-dateutil")
import datetime


def my_dateutil():
    a = datetime.datetime(2012, 9, 23)
    # print(a + timedelta(months=1))
    print(a + relativedelta(months=+1))
    print(a + relativedelta(months=+4))

    b = datetime.datetime(2012, 12, 21)
    d = b - a
    print(d)
    d = relativedelta(b, a)
    print(d)
    print(type(d))
    print(d.months)
    print(d.days)


if __name__ == '__main__':
    my_dateutil()
