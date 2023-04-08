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

@main.route('/followers/<int:user_id>', methods=['GET'])
def get_followers(user_id: int):
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
    return jsonify({'followers': follower_list}), 200

@main.route('/following/<int:user_id>', methods=['GET'])
def get_following(user_id: int):
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
    following_list = [{'id': row.id, 'name': row.name} for row in result]
    return jsonify({'following': following_list}), 200

@main.route('/follow/', methods=['POST'])
def follow_user():
    user_id = request.form.get('userId')
    follow_id = request.form.get('followerId')
    
    new_follow = UserFollows(follower_id=user_id, following_id=follow_id)
    db.session.add(new_follow)
    db.session.commit()
    
    return jsonify({'message': 'User followed successfully.'}), 200

@main.route('/unfollow/', methods=['POST'])
def unfollow_user():
    user_id = request.form.get('userId')
    unfollow_id = request.form.get('followerId')
    
    unfollow = UserFollows.query.filter_by(follower_id=user_id, following_id=unfollow_id).first()
    db.session.delete(unfollow)
    db.session.commit()
    
    return jsonify({'message': 'User unfollowed successfully.'}), 200
