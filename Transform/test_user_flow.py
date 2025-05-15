def test_user_creation_and_auth(create_and_cleanup_user):
    user = create_and_cleanup_user
    assert "id" in user
    assert user["name"] == "Sushil QA"
    assert user["email"] == "sushil.qa@example.com"
