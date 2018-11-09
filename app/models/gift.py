#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/9 09:26
@File    : gift.py
@Author  : frank.chang@shoufuyou.com
"""

from app.models.dbbase import db

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.models.dbbase import Base

class Gift(Base):
    __tablename__ = 'Gift'
    id = Column(Integer, primary_key=True)
    user = relationship('User')

    # 外键关联
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('user.id'))
    launched = Column(Boolean, default=False, comment='是否捐赠成功,true:1,false:0')


if __name__ == '__main__':
    pass
