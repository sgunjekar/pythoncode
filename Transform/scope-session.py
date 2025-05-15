import pytest

@pytest.fixture(scope="session")
def setup_session():
    print("\n[Setup] session scope")
    yield
    print("\n[Teardown] session scope")

def test_a(setup_session):
    print("\nRunning test_a")

def test_b(setup_session):
    print("\nRunning test_b")