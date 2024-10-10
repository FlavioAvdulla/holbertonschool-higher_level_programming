#!/usr/bin/python3
"""
This is a Flask application for
demonstrating authentication using
HTTP Basic Auth and JWT. The script
requires Python 3 interpreter.
"""


from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

auth = HTTPBasicAuth()

users = {
    "user1": generate_password_hash("password1"),
    "admin1": generate_password_hash("password2")
}


@auth.verify_password
def verify_password(username, password):
    """
    Verifies the password for a given username.
    """
    if username in users and check_password_hash
    (users.get(username), password):
        return username


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """
    Endpoint protected by Basic Authentication.
    """
    return "Basic Auth: Access Granted"


app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

users_data = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password1"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password2"),
        "role": "admin"
    }
}


@app.route('/login', methods=['POST'])
def login():
    """
    Login endpoint to authenticate users
    and generate a JWT token.
    """
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = users_data.get(username, None)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"msg": "Bad username or password"}), 401

    token = create_access_token(identity=user)
    return jsonify(token=token)


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    Endpoint protected by JWT Authentication.
    """
    current_user = get_jwt_identity()
    return jsonify(msg="JWT Auth: Access Granted"), 200


def role_required(role):
    """
    Decorator to protect endpoints and ensure
    user has the required role.
    """
    def wrapper(fn):
        @jwt_required()
        def decorated(*args, **kwargs):
            current_user = get_jwt_identity()
            if current_user["role"] != role:
                return jsonify({"msg": "Access denied"}), 403
            return fn(*args, **kwargs)
        return decorated
    return wrapper


@app.route('/admin-only', methods=['GET'])
@role_required('admin')
def admin_only():
    """
    Endpoint only accessible to users with the 'admin' role.
    """
    return jsonify(msg="Admin Access: Granted")


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run(debug=True)
