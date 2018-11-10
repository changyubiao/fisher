#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/9 16:19
@File    : register.py
@Author  : frank.chang@shoufuyou.com
"""

from wtforms import Form, IntegerField, PasswordField
from wtforms import StringField

from wtforms.validators import Length, NumberRange, DataRequired, Email
from wtforms.validators import ValidationError

from app.models.user import User


class RegisterForm(Form):
    pass
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入你的密码'), Length(1, 32)])

    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("邮箱已经存在")

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError("昵称已经存在")


if __name__ == '__main__':
    pass
