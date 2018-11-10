#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/9 22:27
@File    : login.py
@Author  : frank.chang@shoufuyou.com
"""

from wtforms import Form, IntegerField, PasswordField
from wtforms import StringField

from wtforms.validators import Length, NumberRange, DataRequired, Email
from wtforms.validators import ValidationError


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入你的密码'), Length(0, 32)])



if __name__ == '__main__':
    pass
