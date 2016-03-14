# -*- coding: utf-8 -*-
# #  Author: nikang

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views