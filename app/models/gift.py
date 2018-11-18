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
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, desc, asc, func
from sqlalchemy.orm import relationship
from app.models.dbbase import Base
from app.models.dbbase import db

# from werkzeug
from app.models.wish import Wish
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

    @classmethod
    def get_user_gifts(cls, uid):
        pass
        mygifts = Gift.query.filter_by(uid=uid, launched=False).order_by(desc(Gift.create_time)).all()

        return mygifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        """
        传入一组 isbn ,到 gift 表中 检索相应的 礼物，并计算某个礼物的数量，统计每个礼物的总数。
        :param isbn_list:
        :return:
        """
        pass
        mywishs = db.session.query(func.count(Wish.id), Wish.isbn).filter(
            Wish.launched == 0, Wish.status == 1,
            Wish.isbn.in_(isbn_list)).group_by(
            Wish.isbn).all()

        return [{'count': count, 'isbn': isbn} for count, isbn in mywishs]

    @classmethod
    def redraw_from_gift(cls, id):
        gift = Gift.query.filter_by(id=id).first()

        if gift:
            # 删除 书籍
            db.session.delete(gift)
            # 不要忘记 commit 操作了。
            db.session.commit()
        pass


if __name__ == '__main__':
    pass

    query = Gift.query.filter_by(uid=1, isbn='9787111185239')
    ret = query.all()
    print(ret)

    # q = session.query(Flow.timestamp).filter(trace_id == 1).order_by(desc(Flow.timestamp))

    ret = Gift.query.distinct(Gift.isbn).order_by(desc(Gift.create_time)).all()

    print(ret)
