from app.web.blueprint import web


__author__ = '七月'


@web.route('/')
def index():
    pass
    return 'this is index.'


@web.route('/personal')
def personal_center():
    pass
