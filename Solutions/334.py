"""
Problem:

The 24 game is played as follows. You are given a list of four integers, each between 1
and 9, in a fixed order. By placing the operators +, -, *, and / between the numbers,
and grouping them with parentheses, determine whether it is possible to reach the value
24.

For example, given the input [5, 2, 7, 8], you should return True, since
(5 * 2 - 7) * 8 = 24.

Write a function that plays the 24 game.
"""

from typing import List

OPERATORS = set(["+", "-", "*", "/"])


def game_24(arr: List[int]) -> bool:
    if len(arr) == 1:
        return arr[0] == 24
    # checking if 24 can be reached
    possibilities = []
    for si in range(len(arr) - 1):
        # checking all possibilities
        for operator in OPERATORS:
            num_1 = arr[si]
            num_2 = arr[si + 1]
            try:
                possibility = (
                    arr[:si]
                    + [eval("{} {} {}".format(num_1, operator, num_2))]
                    + arr[si + 2 :]
                )
                possibilities.append(possibility)
            except ZeroDivisionError:
                pass
    return any([game_24(x) for x in possibilities])


if __name__ == "__main__":
    print(game_24([5, 2, 7, 8]))
    print(game_24([1, 1, 1, 1]))


"""
SPECS:

TIME COMPLEXITY: O(operations)
SPACE COMPLEXITY: O(operations)
[the passed array contains 4 (constant) numbers, else it would have been
O(operations x (n ^ n)) in time & space]
"""
