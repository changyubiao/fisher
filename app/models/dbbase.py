#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/9 09:26
@File    : dbbase.py
@Author  : frank.chang@shoufuyou.com
"""

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Integer, Float, Column, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    _invalid_key = {'id'}
    status = Column(SmallInteger, default=1, comment='状态判断,如果是1 代表记录存在,0记录不存在,用做软删除.')

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
