from app.operations import add, multiply

def test_add():
    assert add(2,2) == 4

def test_multiplication():
    assert multiply(2,2) == 4
