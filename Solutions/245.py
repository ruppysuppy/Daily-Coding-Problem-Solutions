'''
Problem:

You are given an array of integers, where each element represents the maximum number of steps that can be jumped going forward from that element.
Write a function to return the minimum number of jumps you must take in order to get from the start to the end of the array.

Example:

Input = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]
Output = 2 (as the optimal solution involves jumping from 6 to 5, and then from 5 to 9)
'''

from sys import maxsize


def get_min_jumps(arr):
    length = len(arr)
    # using dynamic programming to reduce O(n ^ n) problem to O(n ^ 2)
    dp = [0 for _ in range(length)]
    for i in range(length-2, -1, -1):
        # updating the minimum hops for each position
        if arr[i]:
            dp[i] = min(dp[i+1 : i+arr[i]+1]) + 1
        else:
            dp[i] = maxsize
    return dp[0]


# DRIVER CODE
print(get_min_jumps([6, 2, 4, 0, 5, 1, 1, 4, 2, 9]))