"""
Problem:

Given an array of integers, write a function to determine whether the array could
become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify
the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one
element to get a non-decreasing array.
"""

from typing import List


def check_1_modify_to_sorted(arr: List[int]) -> bool:
    value = arr[0]
    non_increasing_count = 0
    for elem in arr[1:]:
        if elem - value < 0:
            non_increasing_count += 1
            if non_increasing_count > 1:
                return False
        value = elem
    return True


if __name__ == "__main__":
    print(check_1_modify_to_sorted([10, 5, 7]))
    print(check_1_modify_to_sorted([10, 5, 1]))
    print(check_1_modify_to_sorted([1, 10, 5, 7]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
