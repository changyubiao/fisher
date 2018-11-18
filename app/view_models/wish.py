#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/18 09:06
@File    : gift.py
@Author  : frank.chang@shoufuyou.com
"""
from app.view_models.book import BookViewModel


class MyWishes:
    """
    将原始数据， 改成  页面需要展示的数据。
    """

    def __init__(self, my_gifts, wish_count_list):
        self.gifts = []
        self.__mygifts = my_gifts
        self.__wish_count_list = wish_count_list

        self.gifts = self.__parse()

        pass

    def __parse(self):
        tmp_gifts = []
        for gift in self.__mygifts:
            # 代码优化大全 ，对于循环的嵌套的优化，
            # 需要修改 内层循环变成一个方法
            gift = self.__matching(gift)
            tmp_gifts.append(gift)
        return tmp_gifts

    def __matching(self, gift):
        count = 0
        for wish in self.__wish_count_list:
            if gift.isbn == wish['isbn']:
                count = wish['count']

        # gift = MyGift(gift.id, BookViewModel(gift.book), count)
        # 当然这里也可以返回一个字典
        gift = {
            'id': gift.id,
            'book': BookViewModel(gift.book),
            'wishes_count': count
        }
        return gift


class MyWish:
    def __init__(self, id, book, wishes_count):
        """
        展示一本书， 要展示

        礼物的id ,  book , 心愿数量
        :param id:
        :param book:
        :param wishes_count:
        """
        self.id = id
        self.book = book
        self.wishes_count = wishes_count


if __name__ == '__main__':
    pass
