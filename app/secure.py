#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: setting.py
@time: 2018/10/10 下午2:34


生产环境, 测试环境不一样的配置....




"""


# 不能上传git 私密的信息...


XINYONGFEI_BI__URL = 'mysql+cymysql://root:test1111SFY1024#@47.93.76.136:3306/xinyongfei_fisher?charset=utf8'

# 必须制定 这个URL
SQLALCHEMY_DATABASE_URI = XINYONGFEI_BI__URL
SQLALCHEMY_TRACK_MODIFICATIONS = True


SECRET_KEY='fjsaiofiasjfaljiojsni323922newejejj092nlc[[l.oo;;q'





