#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: test2.py
@time: 2018/11/2 上午9:46

"""



import threading
import time

def worker():
    print('I am worker')
    time.sleep(5)

    t = threading.current_thread()
    print(t)

    print('quit worker')


t2 = threading.Thread(target=worker, name='t2')
t2.start()



# 更加充分的利用CPU的性能优势
# 异步编程.

t = threading.current_thread()
print(t)





# 资源是稀缺的
# 计算机资源 竞争计算机的资源
# 进程
# 至少有1个进程
# 进程是竞争计算机资源的基本单位

# 单核CPU 永远只能够执行一个应用程序？
# 在不同的应用程序进程之间切换
# Pycharm、风暴英雄、QQ

# 进程调度
# 算法 挂起 切换到另外一个进程 操作系统原理
# 进程/线程 开销是非常大 上下文

# 4核

# 线程 线程是进程的一部分 1个线程 多个线程
# CPU 粒度太大了 更小的单元 CPU的资源
# 线程

# 进程 分配资源 内存资源
# 线程 利用CPU执行代码

# 代码 指令 CPU来执行 资源
# 访问资源
# 线程属于进程 访问进程资源


# 进程/线程切换  开销是非常大  上下文环境要被保存.


if __name__ == '__main__':
    pass
