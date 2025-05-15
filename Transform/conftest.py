import pytest
import requests
import json


BASE_URL = "https://reqres.in/api"
headers = {
    "Content-Type": "application/json"
}
TOKEN = "abc123securetoken"  # Ideally store securely via env vars

@pytest.fixture(scope="function")
def create_and_cleanup_user():
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    with open("test_data.json", "r") as f:
        payload = json.load(f)["user"]

    # Setup: create user
    response = requests.post(f"{BASE_URL}/users", headers=headers, json=payload)
    assert response.status_code == 201
    user = response.json()
    user_id = user["id"]

    yield user  # Provide user info to test

    # Teardown: delete user
    del_response = requests.delete(f"{BASE_URL}/users/{user_id}", headers=headers)
    assert del_response.status_code in [200, 204]
    print(f"Deleted user ID {user_id}")
