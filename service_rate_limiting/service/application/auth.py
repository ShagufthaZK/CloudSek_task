from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_bcrypt import Bcrypt
from flask_login import login_user, logout_user, login_required
from application.models import User
from . import db

auth = Blueprint('auth', __name__)
bcrypt = Bcrypt()


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    user_name = request.form.get('user_name')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(user_name=user_name).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    #return redirect(url_for('main.profile'))
    return "Logged in successfully"


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():

    user_name = request.form.get('user_name')
    password = request.form.get('password')
#TODO: check for empty password
    user = User.query.filter_by(user_name=user_name).first()

    if user:
        flash('Username already exists')
        return redirect(url_for('auth.signup'))

    new_user = User(user_name=user_name, password=(bcrypt.generate_password_hash(password)).decode('utf-8'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    #return redirect(url_for('main.index'))
    return "logged out successfully"
