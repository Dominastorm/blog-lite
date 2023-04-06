from flask import jsonify, Blueprint, render_template
from flask_login import login_required, current_user

from sqlalchemy import select, text

from .models import User, UserFollows
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/followers/<int:user_id>', methods=['GET'])
def get_followers(user_id: int):
    print(user_id)
    query = """
        SELECT * 
        FROM users 
        WHERE id IN (
            SELECT follower_id 
            FROM user_follows 
            WHERE following_id = :user_id
        )
    """
    result = db.session.execute(text(query), {'user_id': user_id})
    follower_list = [{'id': row.id, 'name': row.name} for row in result]
    print(follower_list)
    return jsonify({'followers': follower_list}), 200
