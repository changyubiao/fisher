from flask import flash, redirect, url_for, render_template

from app.models.gift import Gift
from app.setting import BEANS_UPLOAD_ONE_BOOK
from app.view_models.gift import MyGifts
from app.web.blueprint import web

from flask_login import login_required, current_user

from app.models.book import db

__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    """
    我的赠送清单
    :return:
    """

    cid = current_user.id

    my_gifts = Gift.get_user_gifts(uid=cid)

    isbn_list = [gift.isbn for gift in my_gifts]

    wish_count_list = Gift.get_wish_counts(isbn_list)

    wish_model = MyGifts(my_gifts, wish_count_list)
    return render_template('my_gifts.html', gifts=wish_model.gifts)

    # return 'MY gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    """
    赠送 礼物, 书籍
    :param isbn:
    :return:

    # 数据库事务 sqlalchemy  事务操作


    回滚
    rollback



    """

    if current_user.can_save_tolist(isbn):

        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id

            # xxxxerror
            current_user.beans += BEANS_UPLOAD_ONE_BOOK
            db.session.add(gift)
    else:

        flash("这本书已经添加到你的赠送清单里面了. Sorry,can't save isbn:{}".format(isbn))
        # return "sorry,can't save isbn:{}".format(isbn)

    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    """
    撤销赠送 数据

    :param gid:

    wish 表里面删除记录
    :return:
    """
    pass
    print(' redraw_from_gifts ')

    Gift.redraw_from_gift(id=gid)

    print(url_for('web.my_gifts'))
    return  redirect(url_for('web.my_gifts'))
