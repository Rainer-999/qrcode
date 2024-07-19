import pytest
from app.calculator import Calculator

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (3.5, 2.5, 6.0)
])
def test_add(a, b, expected):
    assert Calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-1, 1, -1),
    (0, 5, 0),
    (3.5, 2, 7.0)
])
def test_multiply(a, b, expected):
    assert Calculator.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 1),
    (-1, -1, 0),
    (0, 0, 0),
    (5.5, 2.5, 3.0)
])
def test_subtract(a, b, expected):
    assert Calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (-4, 2, -2),
    (5, 2.5, 2),
    (7.5, 2.5, 3)
])
def test_divide(a, b, expected):
    assert Calculator.divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(1, 0)
