"""
Problem:

Given a string of parentheses, write a function to compute the minimum number of
parentheses to be removed to make the string valid (i.e. each open parenthesis is
eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(",
you should return 2, since we must remove all of them.
"""

from copy import deepcopy

from DataStructures.Stack import Stack


def get_min_parentheses_remove(
    expression: str, stack: Stack = Stack(), num_removed: int = 0
) -> int:
    if not expression and stack.is_empty():
        return num_removed
    elif not expression:
        return len(stack) + num_removed
    if (expression[0] == ")") and (not stack.is_empty() and stack.peek() == "("):
        stack.pop()
        return get_min_parentheses_remove(expression[1:], stack, num_removed)
    # calulating the modifications for parenthesis added to stack
    stack_copy = deepcopy(stack)
    stack_copy.push(expression[0])
    modifications_parenthesis_added_to_stack = get_min_parentheses_remove(
        expression[1:], stack_copy, num_removed
    )
    # calulating the modifications for parenthesis removed
    modifications_parenthesis_ignored = get_min_parentheses_remove(
        expression[1:], stack, num_removed + 1
    )
    return min(
        modifications_parenthesis_added_to_stack, modifications_parenthesis_ignored
    )


if __name__ == "__main__":
    print(get_min_parentheses_remove("()())()"))
    print(get_min_parentheses_remove(")("))


"""
SPECS:

TIME COMPLEXITY: O(2 ^ n)
SPACE COMPLEXITY: O(n)
"""
