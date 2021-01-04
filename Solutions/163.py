"""
Problem:

Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate
it.

The expression is given as a list of numbers and operands. For example: [5, 3, '+']
should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return
5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.
"""

from typing import List, Union

from DataStructures.Stack import Stack

FUNCTIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


def calculate(expression_list: List[Union[int, str]]) -> Union[float, int]:
    stack = Stack()
    # calculating the expression
    for expression in expression_list:
        if expression in FUNCTIONS:
            a = stack.pop()
            b = stack.pop()
            stack.push(FUNCTIONS[expression](a, b))
        else:
            stack.push(expression)
    return stack[0]


if __name__ == "__main__":
    print(calculate([5, 3, "+"]))
    print(calculate([15, 7, 1, 1, "+", "-", "/", 3, "*", 2, 1, 1, "+", "+", "-"]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
