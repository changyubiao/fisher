#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/12 16:26
@File    : trade.py.py
@Author  : frank.chang@shoufuyou.com
"""


class TradeInfo:

    def __init__(self, books):
        self.total = 0
        self.trades = []

        self.__parse(books)

    def __parse(self, books):
        self.total = len(books)

        self.trades = [self.__deal_book(book) for book in books]

    def __deal_book(self, single):
        return dict(
            id=single.id,
            create_time=single.create_datetime.strftime('%Y-%m-%d'),
            nickname=single.user.nickname

        )


if __name__ == '__main__':
    pass
