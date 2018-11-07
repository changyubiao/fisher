#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: test6.py
@time: 2018/11/3 上午10:05

"""
import threading
import time

from werkzeug.local import LocalStack

local_stack = LocalStack()

local_stack.push(1)

print(f'in the Main thread after push,  local_stack.top: {local_stack.top}')


def worker():
    print(f'in the  worker,before push . local_stack.top: {local_stack.top}')

    local_stack.push('frank')
    print(f'in the  worker, after push . local_stack.top: {local_stack.top}')


work_thread = threading.Thread(target=worker, name='work_thread')

work_thread.start()

time.sleep(2)


# 主线程
print(f'in the Main thread  local_stack.top: {local_stack.top}')





def test1():

    stack = LocalStack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


if __name__ == '__main__':
    pass
