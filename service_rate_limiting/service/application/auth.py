from flask import Blueprint, render_template, redirect, url_for, request, flash, make_response, jsonify
from flask_bcrypt import Bcrypt
from flask_login import login_user, logout_user, login_required
from application.models import User
from . import db

auth = Blueprint('auth', __name__)
bcrypt = Bcrypt()


@auth.route('/login', methods=['POST'])
def login_post():
    user_name = request.form.get('user_name')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(user_name=user_name).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        return make_response(jsonify(error="Please check your login details and try again."), 401)

    login_user(user, remember=remember)
    return "Logged in successfully"


@auth.route('/signup', methods=['POST'])
def signup_post():

    user_name = request.form.get('user_name')
    password = request.form.get('password')
#TODO: special checks for password
    if password == '':
        return make_response("password cannot be empty", 400)
    user = User.query.filter_by(user_name=user_name).first()

    if user:
        return make_response("Username already exists", 409)

    new_user = User(user_name=user_name, password=(bcrypt.generate_password_hash(password)).decode('utf-8'))

    db.session.add(new_user)
    db.session.commit()

    return "sign up successful"


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return make_response("logged out successfully", 200)
