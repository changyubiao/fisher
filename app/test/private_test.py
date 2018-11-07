#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: private_test.py
@time: 2018/11/3 上午11:45

"""


class User:
    __slots__ = ('__local', '__dict__', '__name__', '__passwd__')

    def __init__(self, name, passwd):
        self.name = name

        self.__passwd = passwd

    def __release_local__(self):
        self.name = None
        # self.__storage__.pop(self.__ident_func__(), None)


user = User('frank', 'passwd')

print(user.name)

user.__release_local__()

print(user.name)

# print(user.__dict__)
# print(user._User__passwd)


if __name__ == '__main__':
    pass
