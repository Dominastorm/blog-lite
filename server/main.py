from flask import jsonify, Blueprint, render_template, request
from flask_login import login_required, current_user

from server.helpers import get_feed_details, get_follower_list, get_following_list, get_my_posts_details, get_post_details, get_search_results, get_profile_details

from .models import Posts, User, UserFollows
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

@main.route('/post/<int:post_id>', methods=['GET'])
def get_post(post_id: int):
    post = get_post_details(post_id)
    return jsonify({'post': post}), 200

@main.route('/feed/<int:user_id>', methods=['GET'])
def get_feed(user_id: int):
    post_list = get_feed_details(user_id)
    return jsonify({'posts': post_list}), 200

@main.route('/myposts/<int:user_id>', methods=['GET'])
def get_my_posts(user_id: int):
    post_list = get_my_posts_details(user_id)
    return jsonify({'posts': post_list}), 200

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

@main.route('/createpost/', methods=['POST'])
def create_post():
    user_id = request.form.get('userId')
    title = request.form.get('title')
    caption = request.form.get('caption')
    image = request.form.get('image')
    
    # Create the post
    new_post = Posts(user_id=user_id, title=title, caption=caption, image_url=image)
    db.session.add(new_post)

    # Increment the post count
    user = User.query.filter_by(id=user_id).first()
    user.posts += 1
    
    db.session.commit()
    
    return jsonify({'message': 'Post created successfully.', 'postId' : new_post.id}), 200

@main.route('/editpost/', methods=['POST'])
def edit_post():
    user_id = request.form.get('userId')
    post_id = request.form.get('postId')
    title = request.form.get('title')
    caption = request.form.get('caption')
    image = request.form.get('image')

    # Edit the post if the user is the owner
    post = Posts.query.filter_by(id=post_id).first()
    if post.user_id != int(user_id):
        return jsonify({'message': 'User is not the owner of the post.'}), 403
    
    post.title = title
    post.caption = caption
    post.image_url = image
    db.session.commit()
    
    return jsonify({'message': 'Post edited successfully.'}), 200

@main.route('/deletepost/', methods=['POST'])
def delete_post():
    user_id = request.form.get('userId')
    post_id = request.form.get('postId')

    # Delete the post if the user is the owner
    post = Posts.query.filter_by(id=post_id).first()
    if post.user_id != int(user_id):
        return jsonify({'message': 'User is not the owner of the post.'}), 403
    
    db.session.delete(post)

    # Decrement the post count
    user = User.query.filter_by(id=user_id).first()
    user.posts -= 1

    db.session.commit()
    
    return jsonify({'message': 'Post deleted successfully.'}), 200
