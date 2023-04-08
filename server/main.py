from flask import jsonify, Blueprint, render_template, request
from flask_login import login_required, current_user

from server.helpers import get_follower_list, get_following_list, get_search_results, get_profile_details

from .models import User, UserFollows
from . import db

main = Blueprint('main', __name__)

# GET functions

@main.route('/followers/<int:user_id>', methods=['GET'])
def get_followers(user_id: int):
    follower_list = get_follower_list(user_id)
    return jsonify({'followers': follower_list}), 200

@main.route('/following/<int:user_id>', methods=['GET'])
def get_following(user_id: int):
    following_list = get_following_list(user_id)
    return jsonify({'following': following_list}), 200

@main.route('/search/<int:user_id>/<string:search_query>', methods=['GET'])
def search_users(user_id: int, search_query: str):
    search_results = get_search_results(user_id, search_query)
    return jsonify({'searchResults': search_results}), 200

@main.route('/profile/<int:user_id>', methods=['GET'])
def get_profile(user_id: int):
    profile_details = get_profile_details(user_id)
    return jsonify({'profileDetails': profile_details}), 200

# POST functions

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

    # Increment the following and follower count
    user = User.query.filter_by(id=user_id).first()
    user.following_count += 1

    followed = User.query.filter_by(id=follow_id).first()
    followed.followers_count += 1

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

    # Decrement the following and follower count
    user = User.query.filter_by(id=user_id).first()
    user.following_count -= 1

    unfollowed = User.query.filter_by(id=unfollow_id).first()
    unfollowed.followers_count -= 1

    db.session.commit()
    
    return jsonify({'message': 'User unfollowed successfully.'}), 200
