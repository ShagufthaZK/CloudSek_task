from flask import Blueprint, make_response, jsonify
from flask_login import login_required, current_user
from . import limiter, r
import requests
import os

main = Blueprint('main', __name__)


@main.route('/call_api')
@login_required
@limiter.limit("5 per minute;"+os.getenv("HOUR_LIMIT")+" per hour", key_func=lambda: current_user.user_name)
def call_api():
    return requests.get("http://api_a:8000/get_rand_num").content


@main.errorhandler(429)
def ratelimit_handler(e):
    return make_response(jsonify(error="ratelimit exceeded %s" % e.description), 403)


@main.route('/see_remaining_limit')
@login_required
def see_remaining_limit():
    key = "LIMITER/"+os.getenv("KEY_PREFIX")+"/"+current_user.user_name+"/main.call_api/"+os.getenv("HOUR_LIMIT")+"/1/hour"
    y = r.get(key)
    return str(int(os.getenv("HOUR_LIMIT"))-int(y.decode()))






