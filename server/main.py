from typing import Dict, List, Union
from flask import jsonify, Blueprint, render_template, request
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

def get_following_list(user_id: int) -> List[Dict[str, Union[str, int, bool]]]:
    query = """
        SELECT * 
        FROM users 
        WHERE id IN (
            SELECT following_id 
            FROM user_follows 
            WHERE follower_id = :user_id
        )
    """
    result = db.session.execute(text(query), {'user_id': user_id})
    following_list = [{'id': row.id, 'name': row.name, 'followed': True} for row in result]
    return following_list

def get_follower_list(user_id: int) -> List[Dict[str, Union[str, int, bool]]]:
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
    following_ids = [row['id'] for row in get_following_list(user_id)]
    follower_list = [{'id': row.id, 'name': row.name, 'followed': True if row.id in following_ids else False} for row in result]
    return follower_list

@main.route('/followers/<int:user_id>', methods=['GET'])
def get_followers(user_id: int):
    follower_list = get_follower_list(user_id)
    return jsonify({'followers': follower_list}), 200

@main.route('/following/<int:user_id>', methods=['GET'])
def get_following(user_id: int):
    following_list = get_following_list(user_id)
    return jsonify({'following': following_list}), 200

@main.route('/follow/', methods=['POST'])
def follow_user():
    user_id = request.form.get('userId')
    follow_id = request.form.get('followerId')
    
    # Handle case where already following user
    already_followed = UserFollows.query.filter_by(follower_id=user_id, following_id=follow_id).first()
    if already_followed:
        return jsonify({'message': 'User already followed.'}), 200
    
    # Follow the user
    new_follow = UserFollows(follower_id=user_id, following_id=follow_id)
    db.session.add(new_follow)
    db.session.commit()
    
    return jsonify({'message': 'User followed successfully.'}), 200

@main.route('/unfollow/', methods=['POST'])
def unfollow_user():
    user_id = request.form.get('userId')
    unfollow_id = request.form.get('followerId')
    
    unfollow = UserFollows.query.filter_by(follower_id=user_id, following_id=unfollow_id).first()

    # Handle case where already not following user
    if not unfollow:
        return jsonify({'message': 'User already unfollowed.'}), 200

    # Unfollow the user
    db.session.delete(unfollow)
    db.session.commit()
    
    return jsonify({'message': 'User unfollowed successfully.'}), 200
