import pytest
#@pytest.fixture()
@pytest.yield_fixture()
def setup():
    print("once before each method")#yeild fixture works before and after each method
    yield
    print("once after each method")
def testMethod(setup):
    print("method 1")
def testMethod2(setup):
    print("method 2")