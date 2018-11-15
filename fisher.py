#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: fisher.py
@time: 2018/10/10 下午3:03


程序入口


from flask import make_response
from  yushu_book import YuShuBook
from app.web import book

# from flask import url_for
from flask import request
# import  requests

"""

from app import create_app

app = create_app()


# @app.route('/index')
# @app.route('/')
# def index():
#     return 'this is index \n'


def test_main():
    # 生成环境 nginx  +  uwsgi

    print('id:{}  app启动'.format(id(app)))
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])


if __name__ == '__main__':
    print('id:{}  app启动'.format(id(app)))
    # app.run(host='0.0.0.0',port=5000, debug=False,threaded=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
    """
    单进程 .但线程, 10个 请求
    """
