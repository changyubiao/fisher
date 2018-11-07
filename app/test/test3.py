#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: test3.py
@time: 2018/11/2 上午10:13

"""

import threading
import time


# def worker():
#     print('I am worker')
#     time.sleep(5)
#
#     t = threading.current_thread()
#     print(t)
#
#     print('quit worker')
#
#
# t2 = threading.Thread(target=worker, name='t2')
# t2.start()

# 更加充分的利用CPU的性能优势
# 异步编程.



#  4核    A   B    并行 执行程序 .

# python  不能充分利用 多核 cpu 的优势.


# python  的多线程是 鸡肋


# GIL

# 锁   线程安全


#进程 管理资源 ,内存资源 , 一个进程有多个或一个线程.     多个线程 会共享进程中的资源.


# 线程不安全
# 线程安全



# 锁

# 细粒度锁      程序员  主动加锁

#  粗粒度  解释器  GIL   同一时刻多核 CPU, 一个线程执行,一定程度保证线程安全

# 通常加锁也有2种不同的粒度的锁：
# 1. fine-grained(细粒度)，程序员需要自行加/解锁来保证线程安全
# 2. coarse-grained(粗粒度)，语言层面本身维护着一个全局的锁机制用来保证线程安全
# 前一种方式比较典型的是 Java, Jython 等, 后一种方式比较典型的是 CPython (即Python)。
# ---------------------



# a  += 1
# bytecode  解释器里面


# python 中的不同解释器  cpython ,jpython  不同解释器


# 多进程, 进程通信技术


a = 1


def myadd():
    global a
    a = a + 1
    time.sleep(2)
    print(a)


threadA = threading.Thread(target=myadd, name='threadA')
threadB = threading.Thread(target=myadd, name='threadB')
threadC = threading.Thread(target=myadd, name='threadc')



threadA.start()
threadB.start()
threadC.start()
# print(a)


# t = threading.current_thread()
# print(t)

if __name__ == '__main__':
    pass
