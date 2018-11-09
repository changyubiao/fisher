#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/9 09:26
@File    : user.py
@Author  : frank.chang@shoufuyou.com
"""

from app.models.dbbase import db
from sqlalchemy import Integer, String, Boolean, Column, Float
from app.models.dbbase import Base

from werkzeug.security import generate_password_hash


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False, comment='别名')
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128), nullable=False)

    email = Column(String(50), nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)


if __name__ == '__main__':
    pass
