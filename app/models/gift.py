#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/9 09:26
@File    : gift.py
@Author  : frank.chang@shoufuyou.com


    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('user.id'))
"""
from flask import current_app
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, desc, asc
from sqlalchemy.orm import relationship
from app.models.dbbase import Base

# from werkzeug
from app.spider.yushu_book import YuShuBook


class Gift(Base):
    __tablename__ = 'Gift'
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('User.id'))
    isbn = Column(String(15), nullable=False, comment='书籍的isbn编号')
    launched = Column(Boolean, default=False, comment='是否捐赠成功,true:1,false:0')

    def __str__(self):
        return "base:{},isbn:{}".format(self.create_time, self.isbn)

    @property
    def book(self):
        yushubook = YuShuBook()
        yushubook.search_by_isbn(self.isbn)
        # print(yushubook.first)
        return yushubook.first

    @classmethod
    def recent(cls):
        q = Gift.query.filter_by(launched=False).group_by(Gift.isbn).order_by(desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct()

        print(q)

        recent_gifts = Gift.query.filter_by(launched=False).group_by(Gift.isbn).order_by(desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gifts


if __name__ == '__main__':
    pass

    query = Gift.query.filter_by(uid=1, isbn='9787111185239')
    ret = query.all()
    print(ret)

    # q = session.query(Flow.timestamp).filter(trace_id == 1).order_by(desc(Flow.timestamp))

    ret = Gift.query.distinct(Gift.isbn).order_by(desc(Gift.create_time)).all()

    print(ret)
