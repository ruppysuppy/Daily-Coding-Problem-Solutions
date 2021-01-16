"""
Problem:

You are given an array of nonnegative integers. Let's say you start at the beginning of
the array and are trying to advance to the end. You can advance at most, the number of
steps that you're currently on. Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices
0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
"""

from typing import List


def can_reach_end(arr: List[int]) -> bool:
    length = len(arr)
    dp = [False for _ in range(length)]
    dp[length - 1] = True
    # generating the dp lookup
    for i in range(length - 2, -1, -1):
        for j in range(i + 1, min(length, i + arr[i] + 1)):
            if dp[j]:
                dp[i] = True
                break
    return dp[0]


if __name__ == "__main__":
    print(can_reach_end([1, 3, 1, 2, 0, 1]))
    print(can_reach_end([1, 2, 1, 0, 0]))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n)
"""
