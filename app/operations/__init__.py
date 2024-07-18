"""
Using ChatGPT for Coding Assistance

Dear Students,

In this code, I am demonstrating how you can use ChatGPT to assist with coding tasks. I am asking ChatGPT to optimize and enhance our calculator program. The program now includes addition, multiplication, subtraction, and division functions. Each line of the code is commented on verbosely to help you understand its functionality. Additionally, I have added error handling to ensure robustness, particularly focusing on division by zero.

You can use ChatGPT similarly to:
1. Optimize your code: By suggesting improvements to make your code more efficient.
2. Enhance functionality: By adding new features or handling edge cases.
3. Debug and handle errors: By identifying and fixing issues in your code.

Here's the enhanced and commented calculator code:
"""

def add(a: float, b: float) -> float:
    """
    Function to add two numbers.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The sum of a and b.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    return a + b

def multiply(a: float, b: float) -> float:
    """
    Function to multiply two numbers.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The product of a and b.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    return a * b

def subtract(a: float, b: float) -> float:
    """
    Function to subtract the second number from the first number.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The result of a - b.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    return a - b

def divide(a: float, b: float) -> float:
    """
    Function to divide the first number by the second number.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The result of a / b.

    Raises:
    ZeroDivisionError: If b is zero.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
