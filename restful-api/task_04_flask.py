#!/usr/bin/python3
"""
Flask API Example
This script sets up a simple Flask API with
multiple endpoints to manage user data.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    }
}


@app.route('/')
def home():
    """
    Root endpoint returns a welcome message.
    """
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    """
    Status endpoint returns OK to indicate the API is running.
    """
    return "OK"


@app.route('/data')
def data():
    """
    Data endpoint returns a list of all usernames stored in the API.
    """
    return jsonify(list(users.keys()))


@app.route('/users/<username>')
def get_user(username):
    """
    User endpoint returns the full object
    corresponding to the provided username.
    If the user does not exist, returns an error message.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Add User endpoint accepts POST requests toadd
    a new user.
    Parses the incoming JSON data and adds
    the new user to the users dictionary.
    Returns a confirmation message with the
    added user’s data.
    """
    new_user = request.get_json()
    username = new_user.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user})


if __name__ == "__main__":
    app.run(debug=True)
