from flask import render_template

from app.models.gift import Gift
from app.view_models.book import BookViewModel
from app.web.blueprint import web

__author__ = '七月'


@web.route('/')
@web.route('/index')
def index():
    pass

    recent_gifts = Gift.recent()

    books = [BookViewModel(gift.book) for gift in recent_gifts]

    # for g in recent_gifts:
    #     print(g)

    return render_template('index.html', recent=books)
    # return 'this is index.'


@web.route('/personal')
def personal_center():
    pass
