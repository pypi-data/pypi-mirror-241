#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/12/8 21:21
# @Author : xiang
# @File : dicts
# @Project : caishengxiang
"""
描述：各种字典
"""
from collections import OrderedDict
from collections import defaultdict


def ordereddict_example():
    """
    排序字典
    OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。
每次当一个新的元素插入进来的时候， 它会被放到链表的尾部。
对于一个已经存在的键的重复赋值不会改变键的顺序。

需要注意的是，一个 OrderedDict 的大小是一个普通字典的两倍，
因为它内部维护着另外一个链表。
所以如果你要构建一个需要大量 OrderedDict 实例的数据结构的时候
（比如读取 100,000 行 CSV 数据到一个 OrderedDict 列表中去），
那么你就得仔细权衡一下是否使用 OrderedDict 带来的好处要大过额外内存消耗的影响。
    :return:
    """
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    # Outputs "foo 1", "bar 2", "spam 3", "grok 4"
    print(d)
    for key in d:
        print(key, d[key])


def defaultdict_example():
    """
    默认值字典
    defaultdict是Python内建dict类的一个子类，第一个参数为default_factory属性提供初始值，默认为None。
    它覆盖一个方法并添加一个可写实例变量。它的其他功能与dict相同，但会为一个不存在的键提供默认值，从而避免KeyError异常。
    :return:
    """
    def default_value():
        return '默认值'

    a = defaultdict(list)
    a['a'].append(1)
    a['a'].append(2)
    a['b'].append(4)

    d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(2)
    d['b'].add(4)

    print(a)
    print(d)

    e = defaultdict(default_value)
    print(e['zz'])
    print(e)




if __name__ == '__main__':
    ordereddict_example()
    defaultdict_example()
