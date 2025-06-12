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

users_dict = {

    "vega": {
        "username": "vega",
        "password":generate_password_hash("claw"),
        "role" : "admin"
        },

    "balrog": {
        "username": "balrog",
        "password": generate_password_hash("rose"),
        "role" : "user"
    }
}

@auth.verify_password
def verify_password(username, password):
    user = users_dict.get(username)
    if user and check_password_hash(user["password"], password):
        return username

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
    
    user = users_dict.get(username)
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
    if users_dict[identity]["role"] != "admin":
        return "Admin access required", 403
    return "Admin Access: Granted", 200

@app.route('/user')
@jwt_required()
def user_page():
    identity = get_jwt_identity()
    if users_dict[identity]["role"] != "user":
        return "User access required", 403
    return "User Access: Granted", 200

if __name__ == '__main__':
    app.run()