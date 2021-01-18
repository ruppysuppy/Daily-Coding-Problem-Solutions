"""
Problem:

You are given an array of arrays of integers, where each array corresponds to a row in
a triangle of numbers. For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

  1
 2 3
1 5 1
We define a path in the triangle to start at the top and go down one row at a time to
an adjacent value, eventually ending with an entry on the bottom row. For example,
1 -> 3 -> 5. The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.
"""

from typing import List


def get_maximum_weight_path(triangle: List[List[int]]) -> List[int]:
    rows = len(triangle)

    if rows == 0:
        return []
    elif rows == 1:
        return triangle[0]

    # using dynamic programming to get the maximum weight
    # elements stored as (weight, path)
    dp = [list(row) for row in triangle]
    for i in range(len(dp[-2])):
        dp[-2][i] = (
            (max(dp[-1][i], dp[-1][i + 1]) + dp[-2][i]),
            [max(dp[-1][i], dp[-1][i + 1]), dp[-2][i]],
        )
    for i in range(rows - 3, -1, -1):
        for j in range(i + 1):
            dp[i][j] = (
                (max(dp[i + 1][j][0], dp[i + 1][j + 1][0]) + dp[i][j]),
                max((dp[i + 1][j], dp[i + 1][j + 1]), key=lambda elem: elem[0])[1]
                + [dp[i][j]],
            )
    return dp[0][0][1][::-1]


if __name__ == "__main__":
    print(get_maximum_weight_path([[1], [2, 3], [1, 5, 1]]))
    print(get_maximum_weight_path([[1], [2, 3], [7, 5, 1]]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
[n = number of items in the triangle]
"""
