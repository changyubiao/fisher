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


XINYONGFEI_BI_URL = 'mysql+cymysql://root:test1111SFY1024#@47.93.76.136:3306/xinyongfei_fisher?charset=utf8'

# 必须制定 这个URL
SQLALCHEMY_DATABASE_URI = XINYONGFEI_BI_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'fjsaiofias[w]ewq.eq.eqe,qkojfaljiojsni323922jfodsjfspkfpsvn,x.newejejj092nlc[[l.oo;;q'

MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 587

MAIL_USE_SSL = False
MAIL_USE_TLS = True
# MAIL_DEBUG = True
MAIL_USERNAME = '931367095@qq.com'
MAIL_PASSWORD = 'dglbxifgnuppbbcd'  # 授权码
MAIL_SUJECT_PREFIX = '[鱼书]'




# MAIL_SERVER = 'smtp.exmail.qq.com'
# MAIL_PORT = 465
# MAIL_USE_SSL = False
# MAIL_USE_TLS = True
# MAIL_USERNAME = '15769162764@qq.com'
# MAIL_PASSWORD = 'vzkyihdompyrbeai'  # 授权码
