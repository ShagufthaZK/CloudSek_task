from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password


