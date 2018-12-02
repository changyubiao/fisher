#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/25 11:04
@File    : email.py
@Author  : frank.chang@shoufuyou.com
"""
from flask import current_app, render_template
from app import mail

from flask_mail import Message
import threading

import logging

logger = logging.getLogger(__name__)


def send_email_rsync(to=None, subject=None, template=None, **kwargs):
    pass
    """
    同步发邮件 
    """

    msg = Message('[鱼书]' + ' ' + subject, sender=current_app.config['MAIL_USERNAME'], recipients=[to])
    # msg.html = render_template("email/reset_password.html", **kwargs)

    msg.html = render_template(template, **kwargs)
    mail.send(msg)


def send_async_email(app, msg):
    try:
        with app.app_context():
            mail.send(msg)
    except  Exception as  e:
        logging.error(e)
        pass


def send_email(to=None, subject=None, template=None, **kwargs):
    """
    实现 异步发邮件功能

    :param to:
    :param subject:
    :param template:
    :param kwargs:
    :return:
    """
    pass

    msg = Message('[鱼书]' + ' ' + subject, sender=current_app.config['MAIL_USERNAME'], recipients=[to])

    msg.html = render_template(template, **kwargs)

    # 拿到真实的app 对象
    app = current_app._get_current_object()

    t = threading.Thread(target=send_async_email, args=[app, msg])

    t.start()


def test_email():
    msg = Message('测试邮件', body='this is test', sender='931367095@qq.com', recipients=['931367095@qq.com'])
    mail.send(message=msg)


if __name__ == '__main__':
    pass

    send_email()
