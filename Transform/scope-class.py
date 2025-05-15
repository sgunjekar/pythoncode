import pytest


@pytest.fixture(scope="class")
def setup_class():
    print("\n[Setup] class scope")
    yield
    print("[Teardown] class scope")


class TestAPI:
    def test_1(self, setup_class):
        print("TestAPI.test_1")

    def test_2(self, setup_class):
        print("TestAPI.test_2")
