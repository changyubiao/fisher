#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: book.py
@time: 2018/10/28 上午7:51


把视图函数单独放在一个文件里面.
"""

import json
from urllib.parse import quote

from app.spider.yushu_book import YuShuBook
from flask import jsonify
from flask import request
from flask import render_template

from app.view_models.book import BookCollection
from app.web.blueprint import web
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key





"""
request  只能在  请求中使用, 如果脱离了请求使用,  则不能用, .

因为 request  实际上是一个代理..




4-5  验证参数. 
    
    # q 至少一个字符, 长度限制,  
    # page  是一个正整数, 最大值限制.


"""


@web.route('/book/search/')
def search():
    """
    v1  /book/search/<q>/<page>  http://0.0.0.0:5000/book/search/9787501524044/1



    Request    Response

    http  请求信息,
    查询参数 POST 参数. remote  ip

    v2    调整 URL 传参数,  ?q=xxx&page=xxxx  http://0.0.0.0:5000/book/search?q=9787501524044&page=1
         http://0.0.0.0:5000/book/search?q=9787501524044&page=1


    /book/search/


    Response    make_response()

    # request.args.to_dict()
    request.args   里面就是参数了.

    # 参数 这样就可以拿到了.
    # q = request.args['q']
    # page = request.args['page']

    :param q:  普通关键字 isbn
    :param page:
    :return:

    app.add_url_rule

    # return jsonify(bookcollection)
    # return jsonify(bookcollection.__dict__)

    """

    # 验证参数, URL 中的参数.
    # 验证层
    form = SearchForm(request.args)

    yushubook = YuShuBook()

    bookcollection = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)

        if isbn_or_key == 'isbn':
            yushubook.search_by_isbn(q)
        else:
            # 中文转码
            q = quote(q)
            yushubook.search_by_keyword(q, page)

        bookcollection.fill_books(yushubook, q)

        return json.dumps(bookcollection, default=lambda o: o.__dict__)

    else:
        # return jsonify({"msg": '参数校验失败'})
        return jsonify(form.errors)






@web.route('/test')
def  test():


    r = {
        'name':'frank',
        'age':18
    }


    r2 ={
        'name':'frank11',
        'age':11
    }

    return render_template('test.html',data=r)









@web.route('/test2')
def test2():
    from flask import request

    from app.libs.nolocal import n

    print(n.v)
    n.v = n.v + 1
    print('---' * 19)

    print(getattr(request, 'v', 'unkonw v value'))
    setattr(request, 'v', 2)
    print('---' * 19)
    return 'test'


def __valide_param(p, page):
    """
    验证参数
    :param p:
    :param page:
    :return:
    """
    pass


if __name__ == '__main__':
    pass
