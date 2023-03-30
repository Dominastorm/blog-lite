from flask import jsonify, Blueprint
from . import db

import sqlite3

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Index'

@main.route('/profile')
def profile():
    return 'Profile'

# Get all followers
@main.route('/followers/<int:user_id>', methods=['GET', 'POST'])
def get_followers(user_id):
    response_object = {'status': 'success'}
    conn = sqlite3.connect('../database/blog-lite.sqlite3')
    c = conn.cursor()
    c.execute("select * from users where id in (select follower_id from user_follows where following_id = ?)", (user_id,))
    rows = c.fetchall()
    followers = [{'id': r[0], 'username': r[1], 'followed': bool(r[2])} for r in rows]
    conn.close()
    response_object['followers'] = followers
    return jsonify(response_object)
