from typing import Dict, List, Union
from sqlalchemy import select, text
from . import db

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

def get_search_results(user_id: int, search_query: str) -> List[Dict[str, Union[str, int, bool]]]:
    query = """
        SELECT * 
        FROM users 
        WHERE name LIKE :search_query
    """
    result = db.session.execute(text(query), {'search_query': f'%{search_query}%'})
    following_ids = [row['id'] for row in get_following_list(user_id)]
    search_results = [{'id': row.id, 'name': row.name, 'followed': True if row.id in following_ids else False} for row in result]
    return search_results
    
def get_profile_details(user_id: int) -> Dict[str, Union[str, int, bool]]:
    query = """
        SELECT * 
        FROM users 
        WHERE id = :user_id
    """
    result = db.session.execute(text(query), {'user_id': user_id}).first()
    profile_details = {'totalPosts': result.posts, 'followersCount': result.followers_count, 'followingCount': result.following_count}
    return profile_details

def get_post_details(post_id: int) -> Dict[str, Union[str, int, bool]]:
    query = """
        SELECT * 
        FROM posts 
        WHERE id = :post_id
    """
    result = db.session.execute(text(query), {'post_id': post_id}).first()

    # Get username
    user_query = """
        SELECT name
        FROM users
        WHERE id = :user_id
    """
    user_result = db.session.execute(text(user_query), {'user_id': result.user_id}).first()
    post_details = {'userId': result.user_id, 'title': result.title, 'caption': result.caption, 'image': result.image_url, 'timestamp': result.timestamp, 'username': user_result.name}
    return post_details
    
def get_feed_details(user_id: int) -> List[Dict[str, Union[str, int, bool]]]:
    query = """
        SELECT * 
        FROM posts 
        WHERE user_id IN (
            SELECT following_id 
            FROM user_follows 
            WHERE follower_id = :user_id
        )
        ORDER BY timestamp DESC
    """
    result = db.session.execute(text(query), {'user_id': user_id})

    feed_details = []

    for row in result:
        # Get username
        user_query = """
            SELECT name
            FROM users
            WHERE id = :user_id
        """
        user_result = db.session.execute(text(user_query), {'user_id': row.user_id}).first()
        feed_details.append({'id': row.id, 'userId': row.user_id, 'title': row.title, 'caption': row.caption, 'image': row.image_url, 'timestamp': row.timestamp, 'username': user_result.name})

    return feed_details

def get_my_posts_details(user_id: int) -> List[Dict[str, Union[str, int, bool]]]:
    query = """
        SELECT * 
        FROM posts 
        WHERE user_id = :user_id
        ORDER BY timestamp DESC
    """
    result = db.session.execute(text(query), {'user_id': user_id})

    # Get username
    user_query = """
        SELECT name
        FROM users
        WHERE id = :user_id
    """
    user_result = db.session.execute(text(user_query), {'user_id': user_id}).first()
    feed_details = [{'id': row.id, 'userId': row.user_id, 'title': row.title, 'caption': row.caption, 'image': row.image_url, 'timestamp': row.timestamp, 'username' : user_result.name} for row in result]
    return feed_details

def get_my_latest_post_timestamp(user_id: int) -> Dict[str, Union[str, int, bool]]:
    query = """
        SELECT timestamp 
        FROM posts 
        WHERE user_id = :user_id
        ORDER BY timestamp DESC
        LIMIT 1
    """
    result = db.session.execute(text(query), {'user_id': user_id}).first()
    if result is None:
        return {'timestamp': None}
    return {'timestamp': result.timestamp}
