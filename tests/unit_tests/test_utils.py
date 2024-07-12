# Import the pytest library, which is used for writing and running tests
import pytest

# Import the print_it function from the app.utils module
# This assumes there's a directory named 'app' with a file named 'utils.py'
# that contains the print_it function
from app.utils import print_it

# Define a test function named test_print_it
# The 'capsys' parameter is a pytest fixture that captures stdout and stderr
def test_print_it(capsys):
    # Define a test string that will be passed to the print_it function
    test_text = "Hello, world!"
    
    # Call the print_it function with the test string
    # This is the function we're testing
    print_it(test_text)
    
    # Use the capsys fixture to capture the output that was printed
    # readouterr() returns a named tuple with 'out' and 'err' attributes
    captured = capsys.readouterr()
    
    # Assert that the captured output, with whitespace stripped from the ends,
    # is equal to our original test string
    # This verifies that print_it correctly printed the string we provided
    assert captured.out.strip() == test_text