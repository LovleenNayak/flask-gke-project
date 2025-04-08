from flask import Flask, jsonify

# This variable must be named 'app' to match the CMD in your Dockerfile: "app:app"
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Hello from Flask on GKE!'})

# The block below is optional when using gunicorn, but good for local testing.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
