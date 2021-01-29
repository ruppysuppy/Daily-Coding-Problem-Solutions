"""
Problem:

Given an array of numbers N and an integer k, your task is to split N into k partitions
such that the maximum sum of any partition is minimized. Return this sum.

For example, given N = [5, 1, 2, 7, 3, 4] and k = 3, you should return 8, since the
optimal partition is [5, 1, 2], [7], [3, 4].
"""

from sys import maxsize
from typing import List, Tuple


def minimize_partition_sum_helper(arr: List[int], k: int) -> Tuple[List[int], int]:
    if k == 1:
        return [arr], sum(arr)

    min_value = maxsize
    min_candidate = None
    for i in range(len(arr)):
        arr_1, sum_1 = [arr[:i]], sum(arr[:i])
        arr_2, sum_2 = minimize_partition_sum_helper(arr[i:], k - 1)
        candidate = arr_1 + arr_2, max(sum_1, sum_2)
        if candidate[1] < min_value:
            min_value = candidate[1]
            min_candidate = candidate
    return min_candidate


def minimize_partition_sum(arr: List[int], k: int) -> int:
    _, max_sum = minimize_partition_sum_helper(arr, k)
    return max_sum


if __name__ == "__main__":
    print(minimize_partition_sum([5, 1, 2, 7, 3, 4], 3))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n ^ 2)
"""
