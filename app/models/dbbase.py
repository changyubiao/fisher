#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/9 09:26
@File    : dbbase.py
@Author  : frank.chang@shoufuyou.com
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import Integer, Float, Column, SmallInteger
from contextlib import contextmanager


class SQLAlchemy(_SQLAlchemy):
    """
    继承_SQLAlchemy ,添加自动提交的方法
    """

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    _invalid_key = {'id', }
    status = Column(SmallInteger, default=1, comment='状态判断,如果是1 代表记录存在,0记录不存在,用做软删除.')
    create_time = Column(Integer)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())



    def set_attrs(self, attrs):
        """

        :param attrs: dict
        :return:
        """

        for key, value in attrs.items():
            if hasattr(self, key) and key not in self._invalid_key:
                setattr(self, key, value)


if __name__ == '__main__':
    pass
