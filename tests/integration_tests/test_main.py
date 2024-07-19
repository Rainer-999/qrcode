import pytest
from unittest.mock import patch
from app.main import main

@pytest.mark.integration
def test_main_integration_invalid_choice(capsys):
    with patch('builtins.input', side_effect=['5', '1', '2', '3', 'q']):
        main()
    captured = capsys.readouterr()
    assert "Invalid choice. Please try again." in captured.out
    assert "Addition of 2.0 and 3.0 is equal to 5.0" in captured.out

@pytest.mark.integration
def test_main_integration_invalid_number(capsys):
    with patch('builtins.input', side_effect=['1', 'abc', '2', '3', 'q']):
        main()
    captured = capsys.readouterr()
    assert "Invalid input. Please enter valid numbers." in captured.out
    assert "Addition of 2.0 and 3.0 is equal to 5.0" in captured.out

@pytest.mark.integration
def test_main_integration(capsys):
    with patch('builtins.input', side_effect=['1', '2', '3', 'q']):
        main()
    captured = capsys.readouterr()
    assert "Addition of 2.0 and 3.0 is equal to 5.0" in captured.out



@pytest.mark.integration
def test_main_integration_subtraction(capsys):
    with patch('builtins.input', side_effect=['3', '5', '2', 'q']):
        main()
    captured = capsys.readouterr()
    print(f"DEBUG: Captured Output: {captured.out}")
    assert "Subtraction of 5.0 and 2.0 is equal to 3.0" in captured.out

@pytest.mark.integration
def test_main_integration_division(capsys):
    with patch('builtins.input', side_effect=['4', '8', '2', 'q']):
        main()
    captured = capsys.readouterr()
    print(f"DEBUG: Captured Output: {captured.out}")
    assert "Division of 8.0 and 2.0 is equal to 4.0" in captured.out
    assert "Thank you for using the calculator. Goodbye!" in captured.out

@pytest.mark.integration
def test_main_integration_multiplication(capsys):
    with patch('builtins.input', side_effect=['2', '4', '6', 'q']):
        main()
    captured = capsys.readouterr()
    assert "Multiplication of 4.0 and 6.0 is equal to 24.0" in captured.out
