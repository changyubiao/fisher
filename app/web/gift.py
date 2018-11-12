from flask import flash, redirect, url_for

from app.models.gift import Gift
from app.setting import BEANS_UPLOAD_ONE_BOOK
from app.web.blueprint import web

from flask_login import login_required, current_user

from app.models.book import db


__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'MY gifts'


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
    pass
