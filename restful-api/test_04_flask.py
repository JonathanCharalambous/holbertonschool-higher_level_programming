import requests

BASE_URL = "http://127.0.0.1:5000"

def print_test(name, passed):
    print(f"{name}: {'OK' if passed else 'FAIL'}")

def test_home():
    r = requests.get(f"{BASE_URL}/")
    print_test("Test the home route of the API.", r.status_code == 200 and r.text == "Welcome to the Flask API!")

def test_data_empty():
    r = requests.get(f"{BASE_URL}/data")
    print_test("Test the data route when no users are added.", r.status_code == 200 and r.json() == [])

def test_add_user():
    payload = {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    r = requests.post(f"{BASE_URL}/add_user", json=payload)
    print_test("Test adding a user to the API.", r.status_code == 201 and r.json().get("user", {}).get("username") == "john")

def test_data_after_add():
    r = requests.get(f"{BASE_URL}/data")
    print_test("Test the data route after adding a user.", r.status_code == 200 and "john" in r.json())

def test_get_user():
    r = requests.get(f"{BASE_URL}/users/john")
    json = r.json()
    passed = r.status_code == 200 and json.get("username") == "john"
    print_test("Test getting a user from the API.", passed)

def test_get_nonexistent_user():
    r = requests.get(f"{BASE_URL}/users/doesnotexist")
    print_test("Test getting a user that does not exist.", r.status_code == 404 and r.json().get("error") == "User not found")

def test_status():
    r = requests.get(f"{BASE_URL}/status")
    print_test("Test the status route of the API.", r.status_code == 200 and r.text == "OK")

def test_add_user_without_username():
    payload = {
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    }
    r = requests.post(f"{BASE_URL}/add_user", json=payload)
    print_test("Test adding a user without a username.", r.status_code == 400 and r.json().get("error") == "Username is required")

def test_add_user_duplicate():
    payload = {
        "username": "john",
        "name": "John 2",
        "age": 40,
        "city": "Another City"
    }
    r = requests.post(f"{BASE_URL}/add_user", json=payload)
    print_test("Test adding a user with a duplicate username.", r.status_code == 400 and r.json().get("error") == "Username already exists")

if __name__ == "__main__":
    test_home()
    test_data_empty()
    test_add_user()
    test_data_after_add()
    test_get_user()
    test_get_nonexistent_user()
    test_status()
    test_add_user_without_username()
    test_add_user_duplicate()
