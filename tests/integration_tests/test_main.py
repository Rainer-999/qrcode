"""
This module contains integration tests for the main program logic.

It tests the integration of arithmetic operations, string formatting,
and printing functionality.
"""

import pytest
from unittest.mock import patch
from app.main import main

def test_main_integration(capsys):
    """
    Test the integration of the main function.

    This test ensures that the main function correctly integrates
    the add, multiply, and print_it functions, producing the expected output.
    """
    # Mock the input function to simulate user input
    with patch('builtins.input', side_effect=['1', '2', '3', 'q']):
        main()

    # Capture the printed output
    captured = capsys.readouterr()

    # Define the expected output
    expected_output = (
        "\nPlease choose an operation:\n"
        "1. Addition\n"
        "2. Multiplication\n"
        "q. Quit\n"
        "Add 2.0 + 3.0 is equal to 5.0\n"
        "\nPlease choose an operation:\n"
        "1. Addition\n"
        "2. Multiplication\n"
        "q. Quit\n"
        "Thank you for using the calculator. Goodbye!\n"
    )

    # Assert that the captured output matches the expected output
    assert captured.out == expected_output

@pytest.mark.integration
def test_main_integration_multiplication(capsys):
    with patch('builtins.input', side_effect=['2', '4', '6', 'q']):
        main()
    captured = capsys.readouterr()
    assert "Multiply 4.0 * 6.0 is equal to 24.0" in captured.out

@pytest.mark.integration
def test_main_integration_invalid_choice(capsys):
    with patch('builtins.input', side_effect=['3', '1', '2', '3', 'q']):
        main()
    captured = capsys.readouterr()
    assert "Invalid choice. Please try again." in captured.out
    assert "Add 2.0 + 3.0 is equal to 5.0" in captured.out

@pytest.mark.integration
def test_main_integration_invalid_number(capsys):
    with patch('builtins.input', side_effect=['1', 'abc', '2', '3', '4', 'q']):
        main()
    captured = capsys.readouterr()
    assert "Invalid input. Please enter valid numbers." in captured.out
    assert "Add 2.0 + 3.0 is equal to 5.0" in captured.out