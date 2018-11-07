#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: hello.py
@time: 2018/11/1 下午3:14

"""

"""




Flask 

Request 



APPContext


ResponseContext



"""

from flask import Flask, current_app

from flask import Request

"""
应用上下文 对象 Flask
请求上下文 对象 Request
Flask AppContext
Request RequestContext
离线应用、单元测试


ctx = app.app_context()
ctx.push()
a = current_app
d = current_app.config['DEBUG']
ctx.pop()

"""

app = Flask(__name__)
# ctx = app.app_context()

# 手动 入栈. 如果没有requestContext 入栈, 自己要手动入栈..
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# print(d)
# ctx.pop()


# with
with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']
    print(d)

    #  实现  了 上下文协议 的对象 可以时候用 with
    #  上下文管理器       __enter__   __exit__
    #  __enter__   __exit__   实现这两个魔术方法.
    # with  后面的上下文表达式 必须 返回一个上下文管理器对象


    # 数据库连接, 管理

    # 1 连接数据库
    # 2 exectue  sql
    # 3 释放连接 con.close()

    # try
    #     pass
    # except:pass
    # finally:pass

    # 文件读写  也可以用上下文管理器
    # as  -->后面 是 __enter__ 返回的东西.
    # with open('/tmp/1.sql') as f
    #     pass


class MyResource:

    def __enter__(self):
        print('connect  resource...')
        return self
        # return 'frank'

    def __exit__(self, exc_type, exc_value, tb):
        """

        :param exc_type:
        :param exc_value:
        :param tb:
        :return: true or false   , true , 则不抛出异常, 自己处理 .
        false   不处理, 会向外抛出异常..
        """

        print('close  resource connection ...')


        return True

    def query(self):
        print('query data')


with MyResource() as r:
    pass
    1/0
    r.query()










if __name__ == '__main__':
    pass
