#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: test.py
@time: 2018/10/31 下午4:24

"""

from flask import request


def parse_request():
    a = request

    print(a)
    print(type(a))


if __name__ == '__main__':
    # parse_request()
    pass
