from app.calculator import Calculator
from app.utils import print_it

def get_user_choice():
    """
    Prompt the user to choose an operation.
    
    Returns:
    str: The user's choice ('1' for addition, '2' for multiplication, or 'q' to quit)
    """
    options = "\nPlease choose an operation:\n1. Addition\n2. Multiplication\nq. Quit"
    while True:
        print_it(options)
        choice = input("Enter your choice (1/2/q): ").lower()
        if choice in ['1', '2', 'q']:
            return choice
        print_it("Invalid choice. Please try again.")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print_it("Invalid input. Please enter valid numbers.")

def get_numbers():
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    return num1, num2

def perform_calculation(choice, num1, num2):
    if choice == '1':
        result = Calculator.add(num1, num2)
        operation = "Addition"
    else:
        result = Calculator.multiply(num1, num2)
        operation = "Multiplication"
    return result, operation

def main():
    while True:
        choice = get_user_choice()
        
        if choice == 'q':
            print_it("Thank you for using the calculator. Goodbye!")
            break
        
        num1, num2 = get_numbers()
        result, operation = perform_calculation(choice, num1, num2)
        
        message = f'{operation} of {num1} and {num2} is equal to {result}'
        print_it(message)

if __name__ == "__main__":
    main()
