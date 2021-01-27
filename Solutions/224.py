"""
Problem:

Given a sorted array, find the smallest positive integer that is not the sum of a
subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.
"""

from typing import List


def get_smallest_subset_sum_not_in_arr(arr: List[int]) -> int:
    # NOTE: The array is pre-sorted
    res = 1
    for elem in arr:
        if elem > res:
            break
        res += elem
    return res


print(get_smallest_subset_sum_not_in_arr([1, 2, 3, 10]))
print(get_smallest_subset_sum_not_in_arr([1, 2, 10]))
print(get_smallest_subset_sum_not_in_arr([1, 10]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
