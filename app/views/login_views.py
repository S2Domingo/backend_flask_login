import os

from flask import Blueprint, render_template, request, session, flash, url_for, g
from flask_jwt_extended import jwt_required

from werkzeug.security import check_password_hash
from werkzeug.utils import redirect

from app import db 
from app.models import UserModel
from app.forms import UserLoginForm

bp = Blueprint('user', __name__, url_prefix='/user')

SERVER_REDIRECT='http://www.naver.com/'

@bp.route('/login', methods=['GET', 'POST'])
def login():

    form = UserLoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        error = None 
        user =  UserModel.query.filter_by(user_id=form.user_id.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            print(user)
            session['id'] = user.id
            return render_template('login.html', form=form)

        flash(error)
    
    return render_template('login.html', form=form)


@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(SERVER_REDIRECT)