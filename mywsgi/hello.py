#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: hello.py
@time: 2018/11/3 上午9:17

"""


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')

    # body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]


def cal_rate():
    water_candy = 200

    candy = (water_candy / 25) * 1
    water = (water_candy / 25) * 24
    # water = 192
    # candy = 8.0

    print(f'candy:{candy},water: {water}')
    candy = candy + 8

    rate = candy / (candy + water)
    print('rate: {}'.format(rate))


if __name__ == '__main__':
    pass

    cal_rate()