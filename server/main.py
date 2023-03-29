from flask import Flask, jsonify, request
from flask_cors import CORS

import sqlite3

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':'*'}})

# Get all followers from sqlite3 database
@app.route('/followers/<int:user_id>', methods=['GET', 'POST'])
def get_followers(user_id):
    response_object = {'status': 'success'}
    conn = sqlite3.connect('../database/db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT * FROM followers")
    rows = c.fetchall()
    followers = [{'id': r[0], 'username': r[1], 'followed': bool(r[2])} for r in rows]
    conn.close()
    response_object['followers'] = followers
    return jsonify(response_object)



# Run the app
if __name__ == '__main__':
    app.run(debug=True)
