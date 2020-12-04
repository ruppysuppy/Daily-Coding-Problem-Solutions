"""
Problem:

Given an array of numbers, find the length of the longest increasing subsequence in
the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
"""

from typing import List


def longest_increasing_subsequence(arr: List[int]) -> int:
    length = len(arr)
    arr_dp = [1 for i in range(length)]
    for i in range(1, length):
        for j in range(i):
            if arr[i] > arr[j]:
                # increasing subsequence
                arr_dp[i] = max(arr_dp[i], arr_dp[j] + 1)
    return max(arr_dp)


if __name__ == "__main__":
    print(
        longest_increasing_subsequence(
            [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        )
    )


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n)
"""
