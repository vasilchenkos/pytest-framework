import pytest

@pytest.fixture()
def setup_teardown_test():
    print("setup")
    yield
    print("teardown")



