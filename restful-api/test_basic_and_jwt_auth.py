import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:5000"

def test_basic_auth():
    print("🔐 Testing Basic Auth...")

    response = requests.get(f"{BASE_URL}/basic-protected", auth=HTTPBasicAuth("vega", "claw"))
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "Access Granted" in response.text

    print("✅ Basic Auth: Passed")

def test_login_get_token():
    print("🔐 Testing JWT Login and Token Retrieval...")

    data = {"username": "vega", "password": "claw"}
    response = requests.post(f"{BASE_URL}/login", json=data)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    token = response.json().get("access_token")
    assert token, "No token received"

    print("✅ JWT Login: Token received")
    return token

def test_jwt_protected(token):
    print("🔒 Testing JWT-Protected Endpoint...")

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/jwt-protected", headers=headers)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "Access Granted" in response.text

    print("✅ JWT Protected: Access Granted")

def test_admin_only(token):
    print("👑 Testing Admin-Only Access...")

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/admin-only", headers=headers)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "Admin Access" in response.text

    print("✅ Admin Access: Passed")

def test_user_only_with_admin_token(token):
    print("🚫 Testing User Access with Admin Token...")

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/user", headers=headers)
    assert response.status_code == 403, f"Expected 403, got {response.status_code}"
    assert "User access required" in response.text

    print("✅ User Endpoint Rejects Admin Token")

if __name__ == "__main__":
    test_basic_auth()
    token = test_login_get_token()
    test_jwt_protected(token)
    test_admin_only(token)
    test_user_only_with_admin_token(token)
