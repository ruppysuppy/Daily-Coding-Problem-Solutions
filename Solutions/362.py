"""
Problem:

A strobogrammatic number is a positive number that appears the same after being rotated
180 degrees. For example, 16891 is strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.
"""

from typing import List


def get_strobogrammatic_numbers_helper(N: int) -> List[str]:
    if N == 0:
        return [""]
    if N == 1:
        return ["1", "8", "0"]

    smaller_strobogrammatic_numbers = get_strobogrammatic_numbers_helper(N - 2)
    strob_numbers = []
    for x in smaller_strobogrammatic_numbers:
        strob_numbers.extend(
            ["1" + x + "1", "6" + x + "9", "9" + x + "6", "8" + x + "8",]
        )
    return strob_numbers


def get_strobogrammatic_numbers(N: int) -> List[int]:
    return [int(num) for num in get_strobogrammatic_numbers_helper(N)]


if __name__ == "__main__":
    print(get_strobogrammatic_numbers(1))
    print(get_strobogrammatic_numbers(2))
    print(get_strobogrammatic_numbers(3))


"""
SPECS:

TIME COMPLEXITY: O(4 ^ n)
SPACE COMPLEXITY: O(4 ^ n)
"""
