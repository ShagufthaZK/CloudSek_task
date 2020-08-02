from flask import Blueprint, g, make_response, jsonify
from flask_login import login_required
from . import limiter
import requests

main = Blueprint('main', __name__)
shared_limit = limiter.shared_limit("300 per hour", scope="hello")


@main.route('/call_api')
@login_required
@limiter.limit("5 per minute;300 per hour")
@shared_limit
def call_api():
    return requests.get("http://api_a:8000/get_rand_num").content


@main.errorhandler(429)
def ratelimit_handler(e):
    return make_response(jsonify(error="ratelimit exceeded %s" % e.description), 403)


@main.route('/see_remaining_limit')
@login_required
@shared_limit
def see_remaining_limit():
    window = limiter.limiter.get_window_stats(*getattr(g, 'view_rate_limit', None))
    return str(window[1])





