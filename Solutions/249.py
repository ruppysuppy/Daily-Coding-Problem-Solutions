"""
Problem:

Given an array of integers, find the maximum XOR of any two elements.
"""

from sys import maxsize
from typing import List


def get_max_xor(arr: List[int]) -> int:
    max_xor = -maxsize
    for index, elem1 in enumerate(arr):
        for elem2 in arr[index + 1 :]:
            max_xor = max(max_xor, elem1 ^ elem2)
    return max_xor


if __name__ == "__main__":
    print(get_max_xor([1, 2, 3, 4]))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(1)
"""
