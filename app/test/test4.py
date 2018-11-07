#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: test4.py
@time: 2018/11/2 下午2:17



python多线程到底是不是鸡肋
GIL node.js 单进程 单线程
10 线程 非常严重的依赖CPU计算 CPU密集型程序  , 圆周率计算,视频解码.

IO密集型的程序 ,查询数据库、请求网络资源、读写文件

IO密集型 等待

flask web框架
请求 线程
10请求 flask开启多少个线程来处理请求
webserver
Java、PHP nginx Apache tomcat IIS


"""


"""
flask  web   frame 


请求线程,    

10 个请求     --->  flask  开启多少个线程处理请求  ??


webserver    

nginx , apache ,tomcat  java, IIS , PHP ,IIS 微软服务器


"""





if __name__ == '__main__':
    pass
