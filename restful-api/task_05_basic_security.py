from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "thisIsMySecretKey"
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user
    
@auth.get_user_roles
def get_user_roles(user):
    return user.get("role")


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200

@jwt.unauthorized_loader
def unauthorized_callback(error):
    return "Missing or invalid token", 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return "Invalid token", 401

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return "Token has expired", 401

@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return "Token has been revoked", 401

@jwt.needs_fresh_token_loader
def needs_fresh_token_callback(jwt_header, jwt_payload):
    return "Fresh token required", 401

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        return "Username and password are required", 400

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return "Invalid credentials", 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200

@app.route('/admin-only')
@jwt_required()
def admin_page():
    identity = get_jwt_identity()
    if users[identity]["role"] != "admin":
        return {"error": "Admin access required"}, 403
    return "Admin Access: Granted", 200

@app.route('/user')
@jwt_required()
def user_page():
    identity = get_jwt_identity()
    if users[identity]["role"] != "user":
        return {"error": "User access required"}, 403
    return "User Access: Granted", 200

if __name__ == '__main__':
    app.run()