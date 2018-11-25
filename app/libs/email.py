#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/25 11:04
@File    : email.py
@Author  : frank.chang@shoufuyou.com
"""

from app import mail

from flask_mail import Message


# def send_email(to=None, subject=None, template=None):
def send_email():
    pass
    msg = Message('测试邮件', body='this is test', sender='931367095@qq.com', recipients=['931367095@qq.com'])
    mail.send(message=msg)


if __name__ == '__main__':
    pass

    send_email()