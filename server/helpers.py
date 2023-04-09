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
    post_details = {'title': result.title, 'caption': result.caption, 'image': result.image_url, 'timestamp': result.timestamp, 'username': user_result.name}
    return post_details
    