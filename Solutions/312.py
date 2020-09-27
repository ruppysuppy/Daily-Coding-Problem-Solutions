"""
Problem:

You are given a 2 x N board, and instructed to completely cover the board with the
following shapes:

Dominoes, or 2 x 1 rectangles.
Trominoes, or L-shapes.
For example, if N = 4, here is one possible configuration, where A is a domino, and B
and C are trominoes.

A B B C
A B C C
Given an integer N, determine in how many ways this task is possible.
"""


def count_arragements(N: int) -> int:
    dp = [0 for _ in range(max(3, N + 1))]
    # base cases
    dp[0] = 1  # no domino/trominoes selected
    dp[1] = 1
    dp[2] = 2
    # updating the lookup table
    for i in range(3, N + 1):
        dp[i] = 2 * dp[i - 1] + dp[i - 3]
    # returning the required value
    return dp[N]


if __name__ == "__main__":
    print(count_arragements(0))
    print(count_arragements(1))
    print(count_arragements(2))
    print(count_arragements(3))
    print(count_arragements(4))
    print(count_arragements(5))
