from flask import render_template, redirect, flash, url_for
from flask_login import current_user, login_required

from app import db
from app.models.wish import Wish
from app.view_models.wish import MyWishes
from app.web.blueprint import web


@web.route('/my/wish')
@login_required
def my_wish():
    cid = current_user.id

    my_gifts = Wish.get_user_wishes(uid=cid)
    isbn_list = [wish.isbn for wish in my_gifts]
    wish_count_list = Wish.get_gift_counts(isbn_list)
    # view model层
    wish_model = MyWishes(my_gifts, wish_count_list)
    return render_template('my_wish.html', wishes=wish_model.gifts)
    pass


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_tolist(isbn):

        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            db.session.add(wish)
    else:

        flash("这本书已经添加到你的赠送清单里面了. Sorry,can't save isbn:{}".format(isbn))
        # return "sorry,can't save isbn:{}".format(isbn)

    return redirect(url_for('web.book_detail', isbn=isbn))

    # return 'save isbn:{} into wish'.format(isbn)


@web.route('/satisfy/wish/<int:wid>')
@login_required
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
@login_required
def redraw_from_wish(isbn):
    pass

    uid = current_user.id

    Wish.redraw_from_wish(uid=uid, isbn=isbn)
    return redirect(url_for('web.my_wish'))
