#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: book.py
@time: 2018/10/31 下午4:34

"""

from wtforms import Form, IntegerField
from wtforms import StringField

from wtforms.validators import Length, NumberRange,DataRequired



class SearchForm(Form):
    """
    验证 search 类 .

    验证器,   DataRequired() , Length () 不同的验证器.
    """
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
