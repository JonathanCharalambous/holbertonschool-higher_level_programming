from flask import Flask, jsonify, request

app = Flask(__name__)

users_dict = {
        "jane": {
            "name": "Jane Doe",
            "age": 28,
            "city": "Los Angeles"
        },
    }

@app.route('/')

def home():
    return "Welcome to the Flask API!"

@app.route('/data')
    
def data():
    
    return jsonify(users)

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def users(username):
    return jsonify(users_dict.get(username))

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    
    username = data.get('username')
    name = data.get('name')
    age = data.get('age')
    city = data.get('city')

    users_dict[username] = {

        "name": name,
        "age": age,
        "city": city

    }

    return jsonify({
        "message": "User added",
        "user": users_dict[username]
    })



if __name__ == '__main__':
    app.run()