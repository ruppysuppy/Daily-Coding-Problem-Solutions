"""
Problem:

Given an array of integers in which two elements appear exactly once and all other
elements appear exactly twice, find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does
not matter.

Follow-up: Can you do this in linear time and constant space?
"""

from typing import List, Tuple


def get_uniques(arr: List[int]) -> Tuple[int, int]:
    xor_result = 0
    for val in arr:
        xor_result = xor_result ^ val
    # using the rightmost set bit as mask to segregate the array of numbers into 2 sets
    # performing xor for num1 and num2 based on the set to which they belong to (the 2
    # sets are based on whether a number has rightmost_set_bit of the xor result 1 or 0)
    rightmost_set_bit = xor_result & ~(xor_result - 1)
    num1, num2 = 0, 0
    for val in arr:
        if val & rightmost_set_bit:
            num1 = num1 ^ val
        else:
            num2 = num2 ^ val
    return num1, num2


if __name__ == "__main__":
    print(get_uniques([2, 4, 6, 8, 10, 2, 6, 10]))
    print(get_uniques([2, 4, 8, 8, 10, 2, 6, 10]))
    print(get_uniques([2, 3, 8, 8, 10, 2, 1, 10]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
