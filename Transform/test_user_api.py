import pytest
import requests

base_url = "https://reqres.in/api"

def test_create_user_response(create_and_delete_user):
    user = create_and_delete_user
    assert "id" in user
    assert "createdAt" in user
    assert user["name"] == "Sushil"
    assert user["job"] == "Principal QA"

def test_get_existing_user():
    response = requests.get(f"{base_url}/users/2")
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["id"] == 2
    assert "email" in data
    assert "first_name" in data
