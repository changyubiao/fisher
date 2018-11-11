#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/10 14:56
@File    : test_model.py
@Author  : frank.chang@shoufuyou.com
"""
from sqlalchemy import Integer, String, Boolean, Column, Float
from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manger
from app.models.dbbase import Base
from app.models.dbbase import db


class Test(Base):
    __tablename = 'TestTable'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False, comment='别名')
    phone_number = Column(String(18), unique=True)

    id_card_number = Column(String(length=64), comment='姓名')
    pass


if __name__ == '__main__':
    db.create_all()
    pass



