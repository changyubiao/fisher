#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/9 09:26
@File    : dbbase.py
@Author  : frank.chang@shoufuyou.com
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from flask_sqlalchemy import BaseQuery
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


class Query(BaseQuery):

    def filter_by(self, **kwargs):
        if 'status' not in kwargs:
            kwargs['status'] = 1

        return super().filter_by(**kwargs)


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    _invalid_key = {'id', }
    status = Column(SmallInteger, default=1, comment='状态判断,如果是1 代表记录存在,0记录不存在,用做软删除.')
    create_time = Column(Integer,comment='创建时间,时间戳,整型')

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())



    @property
    def create_datetime(self):
        """
        把 时间戳 转换成 datetime 类型.
        :return:
        """
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None


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

    from flask_sqlalchemy import BaseQuery


    class Query(BaseQuery):

        def filter_by(self, **kwargs):
            if 'status' not in kwargs:
                kwargs['status'] = 1

            return super().filter_by(**kwargs)




    b = BaseQuery()