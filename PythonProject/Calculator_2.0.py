import math

from Python_function_checkpoint import calculator

'''    EXERCICE  Creating a calculator
Create a new file called "calculator_2.0.py"
Create a class called "Calculator" that contains the following:
A dictionary attribute to store the available mathematical operations and their corresponding functions
A method called "init" that initializes the dictionary with the basic mathematical operations (+, -, *, /) and corresponding functions
A method called "add_operation" that takes in two arguments: the operation symbol and the corresponding function. This method should add the new operation and function to the dictionary.
A method called "calculate" that takes in three arguments: the first number, the operation symbol, and the second number. This method should use the dictionary to determine the appropriate function to perform the calculation. It should also include error handling to check if the operation symbol is valid and if the input values are numbers. If an error is encountered, the method should print an error message and raise an exception.
Create separate functions for the advanced mathematical operations (exponentiation, square root, logarithm) and use the "add_operation" method to add them to the calculator's dictionary.
In the main program, create an instance of the Calculator class, and use a while loop that allows the user to continue performing calculations until they choose to exit.
Use the input() function to get input from the user for the numbers and operation symbol.Use the math library for advanced mathematical operations
Use the isinstance() function to check if the input is a number.'''

class Calculator:
    def __init__(self):
        # to initialize the basics math functions
        self.operations={
            '+': self.add,
            '-': self.substract,
            '*': self.multiply,
            '/': self.divide
        }
    # basics operations
    def add(self,num1, num2):
        return num1 + num2

    def substract(self,num1, num2):
        return num1 - num2

    def multiply(self,num1, num2):
        return num1 * num2

    def divide(self,num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return 'error!! can not divide by 0'

    def add_operation(self, symbol, function):
        self.operations[symbol]= function

    def calculate(self, num1,operation,num2):
        if operation not in self.operations:
            print(f'Error'
                  f': {operation}is not valide')
            raise ValueError(f'invalid operation:{operation}')
        if not (isinstance(num1,(int,float)) or not isinstance(num2,(int,float))):
            print ('Error: you must input numbers')
            raise TypeError('input must be number')
        return self.operations[operation](num1,num2)

#adding advanced mathematical operations
def exponentiation(num1,num2):
    return num1 ** num2
def square_root(num1):
    if num1 <0:
        raise ValueError('Error, we can not take negative number')
    return math.sqrt(num1)
def logarithm (num1,base=math.e):
    if num1 <= 0:
        raise ValueError("num1 must be positive")
    return math.log(num1, base)

Calculator=Calculator()
Calculator.add_operation('^',exponentiation)
Calculator.add_operation('sqrt',square_root)
Calculator.add_operation('log',logarithm)

while True:
    print('Choose from available operations:','\nBasics: + , - , * , /', '\nAdvanced: Exponetiation ^, SquareRoot sqrt, logarithm log')
    operation =input('choose operation or exit:')
    if operation=='exit' :
        print('exiting the calculator')
        break
    if operation in ['sqrt', 'log']:
        num1 = isinstance(input("Enter the first number: "),(int,float))
        if operation == 'log':
            base = float(input("Enter the base (default is e): ") or math.e)
            try:
                result = Calculator.calculate(num1, operation, base)
                print(f"The result is: {result}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            try:
                result = Calculator.calculate(num1, operation, None)
                print(f"The result is: {result}")
            except Exception as e:
                print(f"Error: {e}")
    else:
        try:
            num1 = isinstance(input("Enter the first number: "),(int,float))
            num2 = isinstance(input("Enter the second number: "),(int,float))
            result = Calculator.calculate(num1, operation, num2)
            print(f"The result is: {result}")
        except Exception as e:
            print(f"Error: {e}")
