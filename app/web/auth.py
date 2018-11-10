from app.forms.login import LoginForm
from app.forms.register import RegisterForm
from app.models.user import User
from app.web.blueprint import web
from app.models.dbbase import db

from flask import render_template, url_for, flash
from flask import request
from flask import redirect

from flask_login import login_user

from werkzeug.security import generate_password_hash, check_password_hash

"""
http://0.0.0.0:5000/register


"""

from werkzeug.security import generate_password_hash


@web.route('/register', methods=['GET', 'POST'])
def register():
    """
    验证参数的合法性,提交表单信息
    :return:


    # user.nickname = form.nickname.data
    # user.email = form.email.data
    # user.passwd = form.password.data

    """

    if request.method == 'POST':
        form = RegisterForm(request.form)

        # print(form)
        if form.validate():

            # with db.auto_commit():

            user = User()
            user.set_attrs(form.data)

            # 这样是不好..
            # user.password = generate_password_hash(form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('web.login'))
        else:
            print(form.errors)
            return render_template('auth/register.html', form=form)
    elif request.method == 'GET':
        pass
        return render_template('auth/register.html', form={'data': {}})


@web.route('/login', methods=['GET', 'POST'])
def login():
    pass
    from datetime import timedelta
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        #  检查  user ,和密码

        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_passwd(form.password.data):
            # check password
            #一次性cookie
            login_user(user,remember=True)
            # login_user(user,remember=True,duration=timedelta(seconds=10))
            print('login  success.')
        else:
            flash('用户名或密码错误!')
            pass
    # print(form.errors)
    return render_template('auth/login.html', form=form)

    # if request.method == 'GET':
    #     return render_template('auth/login.html', form=form)

    # print("not support method:{}".format(request.method))


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
