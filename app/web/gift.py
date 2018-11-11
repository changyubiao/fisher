from app.models.gift import Gift
from app.setting import BEANS_UPLOAD_ONE_BOOK
from app.web.blueprint import web

from flask_login import login_required, current_user

from app.models.dbbase import db

from app.models.user import  User

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
    """

    if current_user.can_save_tolist(isbn):

        gift = Gift()
        gift.isbn = isbn
        gift.uid = current_user.id


        #xxxxerror
        current_user.beans += BEANS_UPLOAD_ONE_BOOK

        db.session.add(gift)
        db.session.commit()
    else:

        pass




@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
