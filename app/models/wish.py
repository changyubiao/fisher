#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/10 15:55
@File    : wish.py
@Author  : frank.chang@shoufuyou.com
"""

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, func
from sqlalchemy.orm import relationship
from app.models.dbbase import Base, db
from app.models.gift import Gift
from app.spider.yushu_book import YuShuBook


class Wish(Base):
    __tablename__ = 'Wish'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = relationship('User')

    # 外键关联  注意 ForeignKey 里面  User ,是指 User 的__tablename__ 这个属性
    uid = Column(Integer, ForeignKey('User.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False, comment='是否捐赠成功,true:1,false:0')

    @classmethod
    def get_user_wishes(cls, uid):
        query = Wish.query.filter_by(uid=uid, launched=False).order_by(Wish.create_time.desc())
        # print(query)
        mysishes = query.all()
        return mysishes

    @classmethod
    def get_gift_counts(cls, isbn_list):
        gift_counts = db.session.query(func.count(Gift.id), Gift.isbn).filter(
            Gift.status == 1, Gift.launched == False,
            Gift.isbn.in_(isbn_list)).group_by(Gift.isbn).all()

        # print(gift_counts)
        # 转化成字典的格式
        gifts = [{'count': count, 'isbn': isbn} for count, isbn in gift_counts]
        return gifts
        pass

    @property
    def book(self):
        yushubook = YuShuBook()
        yushubook.search_by_isbn(self.isbn)
        return yushubook.first

    @classmethod
    def redraw_from_wish(cls, uid, isbn):
        wish = Wish.query.filter_by(uid=uid, isbn=isbn, status=1).first()

        if wish:
            # 删除 书籍
            db.session.delete(wish)
            # 不要忘记 commit 操作了。
            db.session.commit()
        pass


if __name__ == '__main__':
    pass
