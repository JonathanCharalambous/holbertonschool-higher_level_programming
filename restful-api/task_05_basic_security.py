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

    "vega": generate_password_hash("claw"),
    "balrog": generate_password_hash("rose")
}

@auth.verify_password
def verify_password(username, password):
    if username in users_dict and \
        check_password_hash(users_dict.get(username), password):
        return username

@app.route('/hope')
@auth.login_required
def hope():
    return ("Please add Vega to SF6"), 200

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
    
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route('/begging', methods=['GET'])
@jwt_required()
def begging():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run()