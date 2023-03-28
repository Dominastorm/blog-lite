from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':'*'}})

# Hello World route
@app.route('/', methods=['GET'])
def greetings():
    return "Hello World!"

# Shark routes
@app.route('/shark', methods=['GET'])
def shark():
    return "Shark 🦈!"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
