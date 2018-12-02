#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: __init__.py
@time: 2018/10/28 上午8:55

"""

import logging

from flask import Flask
from app.models.dbbase import db

from flask_mail import Mail
from flask_login import LoginManager

login_manger = LoginManager()

from app.libs.log import configure_logging

# 日志配置模块
configure_logging('./app/logs/')

logger = logging.getLogger(__name__)

mail = Mail()


def create_app():
    app = Flask(__name__, static_folder='static')
    logger.info('id:{}  app实例化'.format(id(app)))

    # app.config.from_object('config')
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    register_blueprint(app)
    # db 初始化
    db.init_app(app)

    login_manger.init_app(app)
    login_manger.login_view = 'web.login'
    login_manger.login_message = '请先登录or注册'

    mail.init_app(app)
    with app.app_context():
        db.create_all()

    # db.create_all(app=app)
    return app


def register_blueprint(app):
    """
    注册蓝图

    给app 注册蓝图 .
    :param app:
    :return:
    """
    from app.web.book import web
    app.register_blueprint(web)
    pass


if __name__ == '__main__':
    pass
