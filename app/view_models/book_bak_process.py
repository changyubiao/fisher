#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: book.py
@time: 2018/11/3 下午3:27


view_model 层


统一结构, 调整数据 .




返回缺少的数据, 添加数据,
组合 数据
转换数据

"""

from urllib.parse import unquote


class BookViewModel:
    """
    描述 特征   类变量,实例变量
    行为  (方法)


    面向过程
    """
    #

    #



    @classmethod
    def package_single(cls, data, keyword):
        """

        :param data:  原始数据
        :param keyword: 关键字
        :return:
        """

        returned = {
            'books': [],
            'total': 0,
            'keyword': unquote(keyword)
        }

        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]

        return returned

    @classmethod
    def package_collection(cls, data, keyword):

        returned = {
            'books': [],
            'total': 0,
            'keyword': unquote(keyword)
        }

        if data:
            returned['total'] = len(data['books'])
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]

        return returned

    @classmethod
    def __cut_book_data(cls, data):
        """
        裁剪数据

        处理单本书籍,一本

        :param data: 原始数据
        :return:
        """

        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': ';'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book


if __name__ == '__main__':
    pass

    # q=9787070511209
    # q=红楼梦
