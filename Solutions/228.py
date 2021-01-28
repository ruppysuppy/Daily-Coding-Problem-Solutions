"""
Problem:

Given a list of numbers, create an algorithm that arranges them in order to form the
largest possible integer. For example, given [10, 7, 76, 415], you should return
77641510.
"""

from __future__ import annotations
from typing import List


class CustomInt:
    def __init__(self, value: int) -> None:
        self.value = str(value)

    def __lt__(self, other: CustomInt) -> bool:
        if self.value == other.value:
            return False
        for c1, c2 in zip(self.value, other.value):
            if c1 > c2:
                return False
            elif c1 < c2:
                return True
        if len(self.value) > len(other.value):
            return True
        return False


def get_largest(arr: List[int]) -> int:
    arr = list(map(CustomInt, arr))
    arr.sort(reverse=True)
    return int("".join(map(lambda x: x.value, arr)))


if __name__ == "__main__":
    print(get_largest([10, 7, 76, 415]))


"""
SPECS:

TIME COMPLEXITY: O(n x log(n))
SPACE COMPLEXITY: O(n)
"""
