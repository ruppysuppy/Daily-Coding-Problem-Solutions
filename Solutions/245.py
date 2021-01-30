"""
Problem:

You are given an array of integers, where each element represents the maximum number of
steps that can be jumped going forward from that element. Write a function to return
the minimum number of jumps you must take in order to get from the start to the end of
the array.

For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, as the optimal
solution involves jumping from 6 to 5, and then from 5 to 9.
"""

from sys import maxsize
from typing import List


def get_min_jumps(arr: List[int]) -> int:
    length = len(arr)
    dp = [0 for _ in range(length)]
    for i in range(length - 2, -1, -1):
        if arr[i]:
            dp[i] = min(dp[i + 1 : i + arr[i] + 1]) + 1
        else:
            dp[i] = maxsize
    return dp[0]


if __name__ == "__main__":
    print(get_min_jumps([6, 2, 4, 0, 5, 1, 1, 4, 2, 9]))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n)
"""
