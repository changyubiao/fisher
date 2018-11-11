#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/10 15:55
@File    : wish.py
@Author  : frank.chang@shoufuyou.com
"""

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.models.dbbase import Base


class Wish(Base):
    __tablename__ = 'Wish'
    id = Column(Integer, primary_key=True)
    user = relationship('User')

    # 外键关联  注意 ForeignKey 里面  User ,是指 User 的__tablename__ 这个属性
    uid = Column(Integer, ForeignKey('User.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False, comment='是否捐赠成功,true:1,false:0')


if __name__ == '__main__':
    pass
