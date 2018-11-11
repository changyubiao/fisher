#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/9 09:26
@File    : gift.py
@Author  : frank.chang@shoufuyou.com


    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('user.id'))
"""

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.models.dbbase import Base, db


class Gift(Base):
    __tablename__='Gift'
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('User.id'))
    isbn = Column(String(15), nullable=False, comment='书籍的isbn编号')

    launched = Column(Boolean, default=False, comment='是否捐赠成功,true:1,false:0')


if __name__ == '__main__':
    pass
