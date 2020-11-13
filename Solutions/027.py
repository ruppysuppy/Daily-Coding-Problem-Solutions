"""
Problem:

Given a string of round, curly, and square open and closing brackets, return whether
the brackets are balanced (well-formed).

For example, given the string "([])", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

from typing import Dict

from DataStructures.Stack import Stack


def is_parenthesis_balanced(
    string: str, parenthesis_map: Dict[str, str] = {"{": "}", "[": "]", "(": ")"}
) -> bool:
    open_parenthesis_set = set(parenthesis_map.keys())
    stack = Stack()
    # iterating through the string and checking if its balanced
    for char in string:
        if char in open_parenthesis_set:
            stack.push(char)
        elif not stack.is_empty() and parenthesis_map[stack.peek()] == char:
            stack.pop()
        else:
            return False
    # the string is balanced only if the stack is empty (equal number of opening and
    # closing parenthesis)
    return stack.is_empty()


if __name__ == "__main__":
    print(is_parenthesis_balanced("([])"))
    print(is_parenthesis_balanced("((([{}])))"))
    print(is_parenthesis_balanced("([])[]({})"))
    print(is_parenthesis_balanced("([)]"))
    print(is_parenthesis_balanced("((()"))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
