"""
Problem:

Given a circular array, compute its maximum subarray sum in O(n) time.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where
the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.
"""

from typing import List


def kadane(arr: List[int]) -> int:
    max_sum, curr_sum = 0, 0
    for elem in arr:
        curr_sum += elem
        curr_sum = max(curr_sum, 0)
        max_sum = max(max_sum, curr_sum)
    return max_sum


def max_circular_subarr(arr: List[int]) -> int:
    length = len(arr)
    max_kadane = kadane(arr)
    # generating the maximum sum using the corner elements
    max_wrap = 0
    for i in range(length):
        max_wrap += arr[i]
        arr[i] = -arr[i]
    max_wrap += kadane(arr)
    return max(max_wrap, max_kadane)


if __name__ == "__main__":
    print(max_circular_subarr([-4, 5, 1, 0]))
    print(max_circular_subarr([8, -1, 3, 4]))
    print(max_circular_subarr([-8, -1, -3, -4]))
    print(max_circular_subarr([8, -1, 300, -1, 4]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
