# from werkzeug.exceptions import HTTPException

import logging

from flask import render_template, url_for, flash
from flask import request
from flask import redirect

from flask_login import login_user
from flask_login import logout_user

from app.forms.forget_passwd import EmailForm, ResetPasswordForm
from app.forms.login import LoginForm
from app.forms.register import RegisterForm
from app.models.user import User
from app.web.blueprint import web
from app.models.dbbase import db
from app.libs.email import send_email

logger = logging.getLogger(__name__)

# from werkzeug.security import generate_password_hash, check_password_hash

"""
http://0.0.0.0:5000/register


http://0.0.0.0:5000/login?next=www.qq.com


http://0.0.0.0:5000/my/gifts


"""


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

        # logger.info(form)
        if form.validate():

            with db.auto_commit():
                user = User()
                user.set_attrs(form.data)

                # 这样是不好..
                # user.password = generate_password_hash(form.password.data)
                db.session.add(user)

            return redirect(url_for('web.login'))
        else:
            logger.info(form.errors)
            return render_template('auth/register.html', form=form)
    elif request.method == 'GET':
        pass
        return render_template('auth/register.html', form={'data': {}})


@web.route('/login', methods=['GET', 'POST'])
def login():
    pass
    # from datetime import timedelta
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        #  检查  user ,和密码

        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_passwd(form.password.data):
            # check password
            # 一次性cookie
            login_user(user, remember=True)
            # login_user(user,remember=True,duration=timedelta(seconds=10))
            logger.info('login  success.')

            next = request.args.get('next')
            logger.info(f"next: {next}")

            if not next or next.startswith('wwww'):
                return redirect(url_for('web.index'))

            return redirect(next)
        else:
            flash('用户名或密码错误!')
            pass
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)

    if request.method == 'POST' and form.validate():
        email = form.email.data

        user = User.query.filter_by(email=email).first_or_404()
        token = user.generate_token()

        logger.info(f"token：{token}")
        logger.info(f"{form.email.data}")

        account_email = form.email.data

        send_email(to=form.email.data, subject='请重置你的密码', template='email/reset_password.html', user=user,
                   token=token)
        flash('一封邮件已发送到邮箱' + account_email + '，请及时查收')
    return render_template('auth/forget_password_request.html', form=form)


# 单元测试 环节
@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    form = ResetPasswordForm(request.form)

    if request.method == 'POST' and form.validate():
        pass
        # 业务逻辑

        success = User.reset_passwd(token, form.password1.data)
        if success:
            flash('更新密码成功了,请重新登录')
            # 更新用户密码
            return redirect(url_for('web.login'))
        else:

            flash('重置密码失败！')

    return render_template('auth/forget_password.html', form=form)


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    logout_user()

    return redirect(url_for('web.index'))
