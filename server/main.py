from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':'*'}})

# Followers
FOLLOWERS = [
        {
          'id': 1,
          'username': 'exampleuser1',
          'followed': False
        },
        {
          'id': 2,
          'username': 'exampleuser2',
          'followed': False
        }
      ]

# Get all followers
@app.route('/followers', methods=['GET', 'POST'])
def get_followers():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        FOLLOWERS.append({
            'id': post_data.get('id'),
            'username': post_data.get('username'),
            'followed': post_data.get('followed')
            })
        response_object['message'] = 'Follower added!'
    else:
        response_object['followers'] = FOLLOWERS
    return jsonify(response_object) 


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
