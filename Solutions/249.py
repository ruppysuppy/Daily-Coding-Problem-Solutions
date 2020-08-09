"""
Problem:

Given an array of integers, find the maximum XOR of any two elements.
"""

from sys import maxsize


def get_max_xor(arr):
    max_xor = -maxsize
    for index, elem1 in enumerate(arr):
        for elem2 in arr[index + 1 :]:
            max_xor = max(max_xor, elem1 ^ elem2)
    return max_xor


# DRIVER CODE
print(get_max_xor([1, 2, 3, 4]))
