from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_user

from models import Users

auth = Blueprint('auth',__name__)

@auth.rout('/login',methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    user = Users.query.filter_by(email=email).first()

    if not user and not check_password_hash(user.password, password):
        return redirect(url_for('auth.login'))
    
    login_user(user)

    return render_template('login_page.html')

     