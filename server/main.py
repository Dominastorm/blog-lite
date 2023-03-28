from flask import Flask, jsonify
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
@app.route('/followers', methods=['GET'])
def get_followers():
    return jsonify({
        'followers': FOLLOWERS,
        'message': 'success'
    })

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
