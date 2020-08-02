from flask import Flask, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_limiter import Limiter, HEADERS
from flask_limiter.util import get_remote_address
import os
import redis


db = SQLAlchemy()
limiter = Limiter(app=None, headers_enabled=True, key_func=get_remote_address, default_limits=["200 per day"],
                  storage_uri="redis://redis:6379", key_prefix=os.getenv("KEY_PREFIX"))
limiter.header_mapping = {
    HEADERS.LIMIT: "X-My-Limit",
    HEADERS.RESET: "X-My-Reset",
    HEADERS.REMAINING: "X-My-Remaining"
}
r = redis.Redis(host="redis", port="6379")

def create_app():
    app = Flask(__name__)
    #TODO: shift all this to config
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager = LoginManager()

    @login_manager.unauthorized_handler
    def unauthorized():
        return make_response(jsonify(error="login required for this request"), 403)

    login_manager.init_app(app)
    limiter.init_app(app)
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


app = create_app()
