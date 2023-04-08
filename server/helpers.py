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

