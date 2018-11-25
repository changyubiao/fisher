#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/19 22:08
@File    : forget_passwd.py
@Author  : frank.chang@shoufuyou.com
"""

from wtforms import Form, IntegerField, PasswordField
from wtforms import StringField

from wtforms.validators import Length, NumberRange, DataRequired, Email, EqualTo


class ResetPasswordForm(Form):
    password1 = PasswordField(validators=[
        DataRequired(),
        Length(6, 32, message='密码长度至少需要在6到32个字符之间'),
        EqualTo('password2', message='两次输入的密码不相同')])
    password2 = PasswordField(validators=[
        DataRequired(), Length(6, 32)])


class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])


if __name__ == '__main__':
    pass
