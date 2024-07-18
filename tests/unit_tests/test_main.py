"""
This module contains unit tests for the main program logic.
"""

import pytest
from unittest.mock import patch
from app.user_interactions import get_user_choice, get_numbers
from app.operations import add, multiply

def test_get_user_choice_valid():
    with patch('builtins.input', return_value='1'):
        assert get_user_choice() == '1'
    
    with patch('builtins.input', return_value='2'):
        assert get_user_choice() == '2'
    
    with patch('builtins.input', return_value='q'):
        assert get_user_choice() == 'q'

def test_get_user_choice_invalid():
    with patch('builtins.input', side_effect=['3', '1']):
        assert get_user_choice() == '1'
    
    with patch('builtins.input', side_effect=['invalid', '2']):
        assert get_user_choice() == '2'


def test_get_numbers_invalid(capsys):
    # Adding more elements to the side_effect list to handle additional input calls
    with patch('builtins.input', side_effect=['abc', '5', 'def', '3']):
        result = get_numbers()
        captured = capsys.readouterr()
        
        # Check the output to ensure the invalid inputs were handled
        assert "Invalid input. Please enter valid numbers." in captured.out
        # Add any other relevant assertions based on your function's behavior
        assert result == (5.0, 3.0)  # Adjust based on the expected result of valid inputs

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0