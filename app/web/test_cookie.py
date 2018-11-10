#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/9 22:45
@File    : test_cookie.py
@Author  : frank.chang@shoufuyou.com
"""
from flask import make_response

from app.web.blueprint import web



@web.route('/set/cookie')
def set_cookie():
    response = make_response('hello frank')

    response.set_cookie('frank', 'hello,frank', 20)

    return response


if __name__ == '__main__':
    pass
    
