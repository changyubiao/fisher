#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: blueprint.py
@time: 2018/10/31 下午3:46

"""
# 使用 创建一个  blueprint  蓝图
from flask import Blueprint

web = Blueprint('web', __name__)

from flask import render_template


@web.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    pass
