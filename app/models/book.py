#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: book.py
@time: 2018/10/31 下午8:23

pipenv install   Flask-SQLAlchemy

pipenv install   Flask-SQLAlchemy


# sqlalchemy
# sqlalchemy

#  Flask_SqLAlchemy

# Flask

# werkzeug

"""

from sqlalchemy import Column, Integer, String
from app.models.dbbase import Base


class Book(Base):
    # 指定数据库里面的表名
    __tablename__ = 'Book'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='自增ID')

    title = Column(String(length=64), nullable=False, comment='标题')
    author = Column(String(length=64), nullable=True, default='未名', comment='作者')

    binding = Column(String(20), comment='精装,平装')
    publisher = Column(String(50), comment='出版社')
    price = Column(String(20), comment='价格')
    pages = Column(Integer, comment='页数')
    pubdate = Column(String(20), comment='出版日期')
    isbn = Column(String(15), nullable=False, unique=True, comment='isbn号')
    summary = Column(String(1000), comment='摘要')
    image = Column(String(50), comment='图片')

    # MVC M Model 只有数据 = 数据表
    # ORM 对象关系映射 Code First
    def fun(self): pass


if __name__ == '__main__':
    pass


    # db.create_all()
