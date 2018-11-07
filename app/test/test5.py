#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: test5.py
@time: 2018/11/2 下午6:04

"""

import threading
import time

from werkzeug.local import Local


class A:
    a = 10

    def __str__(self):
        return "A: <{}>".format(self.a)


# 主线程
my_obj = Local()
my_obj.a = 10




def worker():
    my_obj.a = 20
    print('in  the new  thread t1 is : {}'.format(my_obj.a))
    print("in the workder, get_indent(): {}".format(threading.get_ident()))


t1 = threading.Thread(target=worker, name='t1_thread')

t1.start()

t1.join()
print("in the MainThread, get_indent(): {}".format(threading.get_ident()))

time.sleep(2)

# 主线程
print("in the main thread my_obj.a: {}".format(my_obj.a))
my_obj.a = 2000

print("in the main thread my_obj.a: {}".format(my_obj.a))

if __name__ == '__main__':
    pass
