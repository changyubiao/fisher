#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/11 16:49
@File    : test_contextmanage.py
@Author  : frank.chang@shoufuyou.com

上下文管理器.理解...OK

假设现在有一个需求,需要在 一本书名 ,加上书名号.
"""

from contextlib import contextmanager


@contextmanager
def make_mark():
    print('< ', end='')
    yield
    print(' >', end='')


def test1():
    with make_mark():
        print('精通Python', end='')


# 正常的上下文管理器
class MyResource:

    # def __enter__(self):
    #     print('open connect database')
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     pass
    #     print('close connection.')

    def query(self):
        print('query data')


# with MyResource() as r:
#     r.query()


@contextmanager
def make_resource():
    print('connect database')
    yield MyResource()
    print('close connection.')


with make_resource() as r:
    r.query()








if __name__ == '__main__':
    pass
