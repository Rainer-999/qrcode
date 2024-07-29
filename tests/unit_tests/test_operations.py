import pytest
from app.operations import add, multiply, subtract, divide


# Test for addition
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 2, 4),
        (-1, 1, 0),
        (-2, -2, -4),
        (0, 0, 0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


# Test for multiplication
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 2, 4),
        (-1, 1, -1),
        (-2, -2, 4),
        (0, 10, 0),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


# Test for subtraction
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 2, 0),
        (-1, 1, -2),
        (-2, -2, 0),
        (0, 0, 0),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


# Test for division
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 2, 2),
        (-4, 2, -2),
        (-4, -2, 2),
        (0, 1, 0),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


# Test for handling exceptions
@pytest.mark.parametrize(
    "func, a, b, exception",
    [
        (add, "two", 2, TypeError),
        (multiply, 2, "two", TypeError),
        (subtract, "two", 2, TypeError),
        (divide, 2, "two", TypeError),
    ],
)
def test_operations_exceptions(func, a, b, exception):
    with pytest.raises(exception):
        func(a, b)
