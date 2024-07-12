"""
This module demonstrates the use of arithmetic operations and printing.

It imports utility functions and performs addition and multiplication
operations, then prints the results.
"""

from app.utils import print_it
from app.operations import add, multiply


def main():
    """
    Execute the main program logic.

    This function performs addition and multiplication operations,
    formats the results into strings, and prints them using the print_it function.
    """
    # Perform addition and format the result into a string
    add_result = add(2, 2)
    add_message = f'Add 2 + 2 is equal to {add_result}'

    # Perform multiplication and format the result into a string
    multiply_result = multiply(2, 2)
    multiply_message = f'Multiply 2 * 2 is equal to {multiply_result}'

    # Print the formatted addition message
    print_it(add_message)

    # Print the formatted multiplication message
    print_it(multiply_message)


if __name__ == '__main__':
    # Execute the main function if this script is run directly
    main()