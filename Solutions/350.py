"""
Problem:

Write a program that determines the smallest number of perfect squares that sum up to
N.

Here are a few examples:

Given N = 4, return 1 (4)
Given N = 17, return 2 (16 + 1)
Given N = 18, return 2 (9 + 9)
"""

from math import ceil, sqrt


def get_min_squares_sum(N: int) -> int:
    dp = [0, 1, 2, 3]
    for i in range(4, N + 1):
        dp.append(i)
        for x in range(1, int(ceil(sqrt(i))) + 1):
            square = pow(x, 2)
            if square > i:
                break
            dp[i] = min(dp[i], 1 + dp[i - square])
    return dp[N]


if __name__ == "__main__":
    print(get_min_squares_sum(4))
    print(get_min_squares_sum(17))
    print(get_min_squares_sum(18))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 1.5)
SPACE COMPLEXITY: O(n)
"""
