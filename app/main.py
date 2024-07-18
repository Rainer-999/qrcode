"""
This module provides a REPL command-line calculator application.

It imports utility functions and allows the user to perform addition 
and multiplication operations on two numbers of their choice.
"""

from app.calculator import Calculator
from app.user_interactions import get_numbers, get_user_choice
from app.utils import print_it

def main():
    """
    Execute the main program logic.

    This function runs a loop that repeatedly prompts the user to choose
    an operation, input numbers, perform the calculation, and print the results
    using the print_it function.
    """
    while True:
        choice = get_user_choice()
        
        if choice == 'q':
            print_it("Thank you for using the calculator. Goodbye!")
            break
        
        if choice not in ['1', '2']:
            print_it("Invalid choice. Please try again.")
            continue
        
        num1, num2 = get_numbers()
        
        if choice == '1':
            result = Calculator.add(num1, num2)
            message = f'Add {num1} + {num2} is equal to {result}'
        else:  # choice == '2'
            result = Calculator.multiply(num1, num2)
            message = f'Multiply {num1} * {num2} is equal to {result}'
        
        print_it(message)

if __name__ == '__main__':
    # Execute the main function if this script is run directly
    main()