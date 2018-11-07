#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: hello.py
@time: 2018/10/10 上午11:22

"""

from flask import Flask

# from config import DEBUG

app = Flask(__name__)

app.config.from_object('app.setting')
app.config.from_object('app.secure')


# print(app.config['Debug'])

@app.route('/')
def index():
    return 'Index Page'


# 第一种方式
@app.route('/hello')
def hello():
    return 'Hello, World'


# 第二种方式  通过类 注册 函数
#  基于类 的视图
# app.add_url_rule('/hello', view_func=hello)






@app.route('/helloworld')
def hello_world():
    """

    status code
    content_type http  headers


    content-type   application/json     text/plain
    :return:
    """

    headers = {
        'content-type': 'text/plain',
        'location': 'http://www.bing.com'
    }

    # response = make_response('<html> </html>', 301)
    # response.headers = headers
    # return response
    return '<html> </html>', 301, headers

if __name__ == '__main__':
    # 生成环境 nginx  +  uwsgi
    # app.run(host='0.0.0.0', debug=DEBUG)
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])