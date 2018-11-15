#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: yushu_book.py
@time: 2018/10/28 上午7:38

"""
from app.libs.httper import HTTP

# 第一种方式
# from app.setting import PER_PAGE


# 第二种方式
from flask import current_app


class YuShuBook:
    """
    类:  是   数据 +  方法  (行为)
    """
    # Model 层
    # 模型层 MVC M层
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)

        self.__fill_single(result)
        # return self

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    def search_by_keyword(self, keyword, page):
        per_page = current_app.config['PER_PAGE']

        url = self.keyword_url.format(keyword, per_page, self.calculate_start(page))
        # print(url)
        result = HTTP.get(url)

        self.__fill_collection(result)

    def calculate_start(self, page):
        return (page - 1) * current_app.config['PER_PAGE']

    # 给外面暴露更好用的接口
    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None


if __name__ == '__main__':
    pass
