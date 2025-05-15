import pytest

@pytest.fixture(scope="module")
def setup_module():
    print("\n[Setup] module scope")
    yield
    print("[Teardown] module scope")

def test_m1(setup_module):
    print("Running test_m1")

class TestGroup:
    def test_m2(self, setup_module):
        print("Running test_m2")
