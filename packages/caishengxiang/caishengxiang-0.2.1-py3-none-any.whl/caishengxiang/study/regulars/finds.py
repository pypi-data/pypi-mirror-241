# ---encoding:utf-8---
# @Time    : 2023/7/9 19:12
# @Author  : caishengxiang
# @Email   : 383301857@qq.com
# @File    : finds.py
# @Project : caishengxiang

import re


def find_email(strs):
    pattern = re.compile(r"[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(?:\.[a-zA-Z0-9_-]+)")
    result = pattern.findall(strs)
    return result


def find_id_card(strs):
    pattern = re.compile(
        r"[1-9]\d{5}(?:18|19|(?:[23]\d))\d{2}(?:(?:0[1-9])|(?:10|11|12))(?:(?:[0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]")
    result = pattern.findall(strs)
    return result


def find_china_phone(strs):
    pattern = re.compile(r"1[356789]\d{9}")
    result = pattern.findall(strs)
    return result


def find_domain(strs):
    """查找域名"""
    pattern = re.compile(r"(?:(?:http:\/\/)|(?:https:\/\/))?(?:[\w](?:[\w\-]{0,61}[\w])?\.)+[a-zA-Z]{2,6}(?:\/)")
    result = pattern.findall(strs)
    return result


def find_ipv4(strs):
    pattern = re.compile(r"((?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d))")
    result = pattern.findall(strs)
    return result


def find_date(strs):
    pattern = re.compile(r"\d{4}(?:-|\/|.)\d{1,2}(?:-|\/|.)\d{1,2}")
    result = pattern.findall(strs)
    return result


if __name__ == '__main__':
    print(find_email(strs='我的私人邮箱是zhuwjwh@outlook.com，公司邮箱是123456@qq.org，麻烦登记一下？'))
    print(find_id_card(strs='小明的身份证号码是342623198910235163，手机号是13987692110'))
    print(find_china_phone(strs='小明的手机号是13987692110，你明天打给他'))
    print(find_domain(strs='Python官网的网址是https://www.python.org/'))
    print(find_ipv4(
        strs="""请输入合法IP地址，非法IP地址和其他字符将被过滤！
增、删、改IP地址后，请保存、关闭记事本！
192.168.8.84
192.168.8.85
192.168.8.86
0.0.0.1
256.1.1.1
192.256.256.256
192.255.255.255
aa.bb.cc.dd"""
    ))
    print(find_date(strs='今天是2020/12/20，去年的今天是2019.12.20，明年的今天是2021-12-20'))
