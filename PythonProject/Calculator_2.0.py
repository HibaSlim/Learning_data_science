import math


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
    def add(self,x, y):
        return x + y

    def substract(self,x, y):
        return x - y

    def multiply(self,x, y):
        return x * y

    def divide(self,x, y):
        if y != 0:
            return x / y
        else:
            return 'error!! can not divide by 0'

    def add_operation(self, symbol, function):
        self.operations[symbol]= function

    def calculate(self, x,operation,y=None):
        if operation not in self.operations:
            print(f'Error: {operation}is not valide')
            raise ValueError(f'invalid operation:{operation}')
        elif operation in ('sqrt','log'):
            if not (isinstance(x, (int, float))):
                print ('Error: you must input numbers')
                raise TypeError('input must be number')
            return self.operations[operation](x)
        if not (isinstance(x, (int, float)) or not isinstance(y, (int, float))):
            print ('Error: you must input numbers')
            raise TypeError('input must be number')
        return self.operations[operation](x, y)

#adding advanced mathematical operations
def exponentiate(x,y):
    return x ** y
def sqrt(x):
    if x <0:
        raise ValueError('Error, we can not take negative number')
    return math.sqrt(x)
def log (x,base=math.e):
    if x <= 0:
        raise ValueError("the number must be positive")
    return math.log(x, base)

Calculator=Calculator()
Calculator.add_operation('^',exponentiate)
Calculator.add_operation('sqrt',sqrt)
Calculator.add_operation('log',log)

while True:
    try:
        x = float(input("Enter the first number (or 'exit' to quit): "))
        print('Choose from available operations:','\nBasics: + , - , * , /', '\nAdvanced: Exponetiate ^, SquareRoot sqrt, logarithm log')
        operation =input('choose operation or exit:')
        if operation == 'exit':
            break
        if operation not in ('sqrt','log'):
            y = float(input("Enter the second number (or 'exit' to quit): "))
            result = Calculator.calculate(x, operation, y)
            print(f"The result of{x}{operation}{y if y is not None else ''}is: {result}")
        else :
            result = Calculator.calculate(x, operation)
            print(f"The result of{operation}{x}is: {result}")
    except Exception as e:
        print(e)


if __name__=='__main__':
        main()