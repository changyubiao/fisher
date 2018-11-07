#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: do_wsgi.py
@time: 2018/11/3 上午9:17

"""


from wsgiref.simple_server import make_server

from mywsgi.hello import application

httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')

httpd.serve_forever()
if __name__ == '__main__':
    pass
