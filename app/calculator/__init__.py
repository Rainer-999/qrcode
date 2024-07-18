from app.operations import add, multiply

class Calculator:

    @staticmethod
    def add(a,b):
        return add(a,b)
    
    @staticmethod
    def multiply(a,b):
        return multiply(a,b)