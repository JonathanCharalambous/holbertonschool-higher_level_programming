from flask import Flask, jsonify, request

app = Flask(__name__)

users_dict = {}

@app.route('/')

def home():
    return "Welcome to the Flask API!"

@app.route('/data')
    
def data():

    return jsonify(list(users_dict.keys())), 200

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def users(username):
    if username not in users_dict:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify(users_dict.get(username))

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid input"}), 400
    
    username = data.get('username')
    name = data.get('name')
    age = data.get('age')
    city = data.get('city')

    if not username:
        return jsonify({"error": "Username is required"}), 400

    users_dict[username] = {

        "username": username,
        "name": name,
        "age": age,
        "city": city

    }

    return jsonify({
        "message": "User added",
        "user": {
            "username": username,
            "name": name,
            "age": age,
            "city": city
        }
    }), 201



if __name__ == '__main__':
    app.run()