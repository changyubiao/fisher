#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/9 09:26
@File    : user.py
@Author  : frank.chang@shoufuyou.com
"""

from sqlalchemy import Integer, String, Boolean, Column, Float
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import login_manger
from app.models.dbbase import Base
from app.libs.helper import is_isbn_or_key
from app.models.gift import Gift
# from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook


class User(UserMixin, Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False, comment='别名')
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128), nullable=False)

    email = Column(String(50), nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0, comment='鱼豆数量')
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def check_passwd(self, raw):
        return check_password_hash(self._password, raw)

    def get_id(self):
        return self.id

    def can_save_tolist(self, isbn):
        """
        # 不允许一个用户 同时 赠送多本相同的书
        #  一个用户不可能同时成为 赠送者和索要者
        :param isbn:
        :return:
        """
        pass

        if is_isbn_or_key(isbn) != 'isbn':
            return False

        book = YuShuBook()

        book.search_by_isbn(isbn)

        if not book.first:
            return False

        # 既不在 赠送清单中, 也不在心愿清单中 才能添加这本书
        gift = Gift.query.filter_by(uid=self.id, isbn=isbn, lanched=False).first()
        wish = Wish.query.filter_by(uid=self.id, isbn=isbn, lanched=False).first()
        if not gift and not wish:
            return True
        else:
            return False


@login_manger.user_loader
def get_user(uid):
    return User.query.get(int(uid))


if __name__ == '__main__':
    pass
