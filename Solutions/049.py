"""
Problem:

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137,
since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take
any elements.

Do this in O(N) time.
"""

from sys import maxsize
from typing import List


def kadanes_algorithm(arr: List[int]) -> int:
    length = len(arr)
    if length == 0:
        return 0
    max_so_far = -maxsize
    max_ending_here = 0
    # generating the largest continuous sum
    for i in range(length):
        max_ending_here = max_ending_here + arr[i]
        max_ending_here = max(max_ending_here, 0)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


if __name__ == "__main__":
    print(kadanes_algorithm([34, -50, 42, 14, -5, 86]))
    print(kadanes_algorithm([-5, -1, -8, -9]))
    print(kadanes_algorithm([5, 1, 8, 9]))
    print(kadanes_algorithm([]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
