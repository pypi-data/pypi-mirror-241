#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/12/8 21:45
# @Author : xiang
# @File : classs
# @Project : caishengxiang
"""
描述：
"""


def slots_example():
    """
    当一个类需要创建大量实例时，可以通过__slots__声明实例所需要的属性，

例如，class Foo(object): __slots__ = ['foo']。这样做带来以下优点：

更快的属性访问速度
减少内存消耗

    默认情况下，访问一个实例的属性是通过访问该实例的__dict__来实现的。如访问a.x就相当于访问a.__dict__['x']
       1 a.x 2. a.__dict__ 3. a.__dict__['x'] 4. 结果
    定义了__slots__的类会为每个属性创建一个描述器。访问属性时就直接调用这个描述器。在这里我将它拆分为三步：
      1 b.x 2. member decriptor 3. 结果
    :return:
    """

    class Member:
        """生成限定属性的对象"""
        __slots__ = ['name', 'value']

    m = Member()
    m.name = 'csx'
    print(m.name)
    try:
        m.xx = 'xx'
    except Exception as e:
        print('报错就对了')


from abc import ABCMeta, abstractmethod


class Father(metaclass=ABCMeta):

    @abstractmethod
    def hello(self, name):
        pass


class Sub(Father):
    pass


def abc_example():
    try:
        Sub()
    except Exception as e:
        print('会提示必须要hello方法:{}'.format(e))


if __name__ == '__main__':
    slots_example()
    abc_example()
