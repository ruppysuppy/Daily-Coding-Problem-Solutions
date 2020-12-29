"""
Problem:

You're given a string consisting solely of (, ), and *. * can represent either a (, ),
or an empty string. Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.
"""

from copy import deepcopy

from DataStructures.Stack import Stack


def can_balance_parentheses(string: str, stack: Stack = Stack()) -> bool:
    if not string and stack.is_empty():
        return True
    elif not string:
        return False
    # checking if the parentheses can be balanced
    if string[0] == "(":
        stack.push("(")
        return can_balance_parentheses(string[1:], stack)
    elif string[0] == ")":
        if not stack.is_empty() and stack.peek() == "(":
            stack.pop()
            return can_balance_parentheses(string[1:], stack)
        return False
    elif string[0] == "*":
        return (
            can_balance_parentheses("(" + string[1:], deepcopy(stack))
            or can_balance_parentheses(")" + string[1:], deepcopy(stack))
            or can_balance_parentheses(string[1:], deepcopy(stack))
        )


if __name__ == "__main__":
    print(can_balance_parentheses("(()*", Stack()))
    print(can_balance_parentheses("(*)", Stack()))
    print(can_balance_parentheses(")*(", Stack()))


"""
SPECS:

TIME COMPLEXITY: O(3 ^ n)
SPACE COMPLEXITY: O(3 ^ n)
"""
