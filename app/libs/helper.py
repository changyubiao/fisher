#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: helper.py
@time: 2018/10/28 上午7:41

帮助函数或者类


"""


def is_isbn_or_key_old(q):
    if q == '111':
        return 'isbn'
    else:
        return 'keyword'


def is_isbn_or_key(word):
    """
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'
    return isbn_or_key


if __name__ == '__main__':
    pass
