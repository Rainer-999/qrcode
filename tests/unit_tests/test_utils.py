# Import the print_it function from the app.utils module
# This assumes there's a directory named 'app' with a file named 'utils.py'
# that contains the print_it function
from app.utils import print_it


# Define a test function named test_print_it
# The 'capsys' parameter is a pytest fixture that captures stdout and stderr
def test_print_it(capsys):
    print_it("Test message")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Test message"
