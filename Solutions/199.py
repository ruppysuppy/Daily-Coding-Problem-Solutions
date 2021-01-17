"""
Problem:

Given a string of parentheses, find the balanced string that can be produced from it
using the minimum number of insertions and deletions. If there are multiple solutions,
return any of them.

For example, given "(()", you could return "(())". Given "))()(", you could return
"()()()()".
"""

from copy import deepcopy
from typing import Tuple

from DataStructures.Stack import Stack


def get_min_changes_helper(
    string: str, modifications: int, stack: Stack, current: str
) -> Tuple[int, str]:
    if not string and stack.is_empty():
        return modifications, current
    elif not string:
        additions = len(stack)
        return modifications + additions, current + (")" * additions)

    if string[0] == "(":
        stack_added = deepcopy(stack)
        stack_added.push("(")
        modifications1, string1 = get_min_changes_helper(
            string[1:], modifications, stack_added, current + "("
        )  # adding to stack
        modifications2, string2 = get_min_changes_helper(
            string[1:], modifications + 1, stack, current
        )  # removing from string
        return min(
            [(modifications1, string1), (modifications2, string2)],
            key=lambda tup: tup[0],
        )

    if not stack.is_empty():
        stack.pop()
        return get_min_changes_helper(string[1:], modifications, stack, current + ")")
    return get_min_changes_helper(string[1:], modifications + 1, stack, current)


def get_min_changes(string: str) -> str:
    _, res = get_min_changes_helper(string, 0, Stack(), "")
    return res


if __name__ == "__main__":
    print(get_min_changes("(()"))
    print(get_min_changes("))()("))
    print(get_min_changes("()(()"))
    print(get_min_changes("()(()))"))
    print(get_min_changes(")(())"))
    print(get_min_changes("())("))


"""
SPECS:

TIME COMPLEXITY: O(2 ^ n)
SPACE COMPLEXITY: O(2 ^ n)
"""
