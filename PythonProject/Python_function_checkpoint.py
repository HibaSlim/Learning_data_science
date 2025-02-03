# Create a calculator program that allows the user to perform mathematical operations on two numbers using basic functions and a dictionary to store the operations. The program should also have the ability to continue calculations with the result of previous calculations.


# Create four basic mathematical functions: 'add', 'subtract', 'multiply', and 'divide' that take in two numbers and return the result of the operation.
def add(num1,num2):
    return num1 + num2
def substract(num1 , num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    if num2 != 0:
        return num1/num2
    else:
        return 'error!! can not divide by 0'

# Create a dictionary 'operations' that assigns the functions to their corresponding operation symbols.
operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide,
}

# Create a function 'calculator' that prompts the user to input the first number.
def calculator():
    num1= float(input('input the first number :'))
    should_continue = True  #to check if the user want to continue calculating
    while should_continue: # Create a while loop that will continue to run until the user chooses to end the current calculation.
        # Use a for loop to print the available operation symbols.
        print('available operations :')
        for symbol in operations:
            print(symbol)
        operation_symbol = input('choose an operation: ')  #Inside the while loop, prompt the user to select an operation symbol.
        num2= float(input('input the second number :'))  #Prompt the user to input the second number

         # Use the dictionary to retrieve the function that corresponds to the selected operation symbol and store it in a variable 'calculation_function'
        calculation_function= operations.get(operation_symbol)
         # Perform the calculation by calling the 'calculation_function' on the two input numbers and store the result in a variable 'answer'.
        if calculation_function:
            answer = calculation_function(num1,num2)
            print(f'{num1}{operation_symbol}{num2} = {answer}' ) #Print the equation and the result of the calculation.
            #Ask the user if they would like to continue using the result as the first number for further calculations
            continue_calc= input('do yo want to use the result for further calculating? (yes/no): ')
            #If the user chooses to continue, update the 'num1' variable to the value of 'answer'
            if continue_calc== 'yes':
                num1 = answer
            # If the user chooses to start a new calculation, set the 'should_continue' variable to false
            else:
                should_continue = False
        # call the 'calculator' function to start a new calculation.
        else :
            print('invalid operation , please choose a valid symbol:')
    print('calculation ended')
calculator()



