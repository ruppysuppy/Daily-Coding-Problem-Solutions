'''
Problem:

Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.
The expression is given as a list of numbers and operands. 
You can assume the given expression is always valid.

Example:

Input = [5, 3, '+']
Output = 8 [5 + 3]

Input = [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] 
Output = 5 [((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1))]
'''

# acceptable functions
FUNCTIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b # use // instead of / for integer division
}

# FUNCTION TO PERFORM THE OPERATION
def calculate(expression_list):
    # getting the functions
    global FUNCTIONS
    # delaring a stack
    stack = []

    # iterating through the expressions list
    for expression in expression_list:
        # if the expression is an operation, the operation is performed and the result added to the stack
        if (expression in FUNCTIONS):
            a = stack.pop()
            b = stack.pop()
            stack.append(FUNCTIONS[expression](a, b))
        # if the expression is an operand, its added to the stack
        else:
            stack.append(expression)
    
    # returning the final result
    return stack[0]

# DRIVER CODE
print(calculate([5, 3, '+']))
print(calculate([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']))