#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/28 11:20
@File    : test_reset_password.py
@Author  : frank.chang@shoufuyou.com
"""

import requests

from itsdangerous import JSONWebSignatureSerializer  as  Serializer
# from ...app.secure import SECRET_KEY
from app.models.user import User

SECRET_KEY = 'fjsaiofias[w]ewq.eq.eqe,qkojfaljiojsni323922jfodsjfspkfpsvn,x.newejejj092nlc[[l.oo;;q'

# url = 'http://0.0.0.0:5000/reset/password'
# token = User.generate_token()

s = Serializer(SECRET_KEY, '600')

# print(s.dumps({'id': 100}).decode('utf-8'))
token = s.dumps({'id': 100}).decode('utf-8')

print(f"token:{token}")

# token=token+'frnak'


s2 = Serializer(SECRET_KEY, '600')

info = s2.loads(token.encode('utf-8'))
print(info)

# print(token)
# url = url+ token
# print(url)
# data = requests.post(url)
# print(data)


if __name__ == '__main__':
    pass
