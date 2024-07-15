"""
This module provides a REPL command-line calculator application.

It imports utility functions and allows the user to perform addition 
and multiplication operations on two numbers of their choice.
"""

from app.utils import print_it
from app.operations import add, multiply

def get_user_choice():
    """
    Prompt the user to choose an operation.
    
    Returns:
    str: The user's choice ('1' for addition, '2' for multiplication, or 'q' to quit)
    """
    while True:
        print_it("\nPlease choose an operation:")
        print_it("1. Addition")
        print_it("2. Multiplication")
        print_it("q. Quit")
        choice = input("Enter your choice (1/2/q): ").lower()
        if choice in ['1', '2', 'q']:
            return choice
        print_it("Invalid choice. Please try again.")

def get_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    
    return num1, num2

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
            result = add(num1, num2)
            message = f'Add {num1} + {num2} is equal to {result}'
        else:  # choice == '2'
            result = multiply(num1, num2)
            message = f'Multiply {num1} * {num2} is equal to {result}'
        
        print_it(message)

if __name__ == '__main__':
    # Execute the main function if this script is run directly
    main()