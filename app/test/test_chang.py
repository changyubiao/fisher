#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/8 15:50
@File    : test_chang.py
@Author  : frank.chang@shoufuyou.com
"""

import json

import json

r = {
    'name': 'frank',
    'sex': 1,
    'hobby': 'swimming'

}


class Person:

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex





class  MyJsonEncoder(json.JSONEncoder):
    pass

    def default(self, o):

        if isinstance(o,Person):
            return {"name": o.name, "sex": o.sex}

        return super(MyJsonEncoder, self).default(o)


p1 = Person('frank',1)

p2 = Person('xiaoqi',7)


l1 = [r,p1]
m = json.dumps(l1)

print(m)

if __name__ == '__main__':
    pass
