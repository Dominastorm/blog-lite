from flask import jsonify, Blueprint, render_template
from flask_login import login_required, current_user

from sqlalchemy import text

from .models import User
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    print("helr")
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/followers/<int:user_id>', methods=['GET'])
def get_followers(user_id):
    print('h9i')
    query = text("""
        SELECT * from users
    """)
    result = db.session.execute(query, {'user_id': user_id})
    follower_list = [{'id': row.id, 'name': row.name} for row in result]
    print(follower_list)
    return jsonify({'followers': follower_list}), 200

