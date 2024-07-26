import pytest
from unittest.mock import patch
from app.user_interactions import get_user_choice
from app.calculator import Calculator
from app.user_interactions import perform_calculation


def test_get_user_choice_valid():
    with patch("builtins.input", side_effect=["1"]):
        assert get_user_choice() == "1"

    with patch("builtins.input", side_effect=["2"]):
        assert get_user_choice() == "2"

    with patch("builtins.input", side_effect=["3"]):
        assert get_user_choice() == "3"

    with patch("builtins.input", side_effect=["4"]):
        assert get_user_choice() == "4"

    with patch("builtins.input", side_effect=["q"]):
        assert get_user_choice() == "q"


def test_get_user_choice_invalid():
    with patch("builtins.input", side_effect=["5", "1"]):
        assert get_user_choice() == "1"

    with patch("builtins.input", side_effect=["z", "2"]):
        assert get_user_choice() == "2"


@pytest.mark.parametrize(
    "operation, a, b, expected_result, expected_operation",
    [
        ("1", 1, 2, 3, "Addition"),
        ("2", 2, 3, 6, "Multiplication"),
        ("3", 5, 3, 2, "Subtraction"),
        ("4", 8, 2, 4, "Division"),
    ],
)
def test_perform_calculation(operation, a, b, expected_result, expected_operation):
    result, operation_name = perform_calculation(operation, a, b)
    assert result == expected_result
    assert operation_name == expected_operation


def test_perform_calculation_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        perform_calculation("4", 4, 0)


@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, 3), (-1, 1, 0), (0, 0, 0), (3.5, 2.5, 6.0)]
)
def test_calculator_add(a, b, expected):
    assert Calculator.add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected", [(2, 3, 6), (-1, 1, -1), (0, 5, 0), (3.5, 2, 7.0)]
)
def test_calculator_multiply(a, b, expected):
    assert Calculator.multiply(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected", [(3, 2, 1), (-1, -1, 0), (0, 0, 0), (5.5, 2.5, 3.0)]
)
def test_calculator_subtract(a, b, expected):
    assert Calculator.subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected", [(6, 3, 2), (-4, 2, -2), (5, 2.5, 2), (7.5, 2.5, 3)]
)
def test_calculator_divide(a, b, expected):
    assert Calculator.divide(a, b) == expected


def test_calculator_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(1, 0)
