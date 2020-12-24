"""
Problem:

You are given a 2-d matrix where each cell represents number of coins in that cell.
Assuming we start at matrix[0][0], and can only move right or down, find the maximum
number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
"""

from typing import List


def get_max_coins(matrix: List[List[int]]) -> int:
    n = len(matrix)
    m = len(matrix[0])
    # generating the maximum number of coins using dynamic programming
    for i in range(1, n):
        for j in range(1, m):
            matrix[i][j] += max(matrix[i - 1][j], matrix[i][j - 1])
    return matrix[n - 1][m - 1]


if __name__ == "__main__":
    matrix = [
        [0, 3, 1, 1],
        [2, 0, 0, 4],
        [1, 5, 3, 1]
    ]
    print(get_max_coins(matrix))

    matrix = [
        [0, 3, 1, 1],
        [2, 8, 9, 4],
        [1, 5, 3, 1]
    ]
    print(get_max_coins(matrix))


"""
SPECS:

TIME COMPLEXITY: O(n x m)
SPACE COMPLEXITY: O(1) [modifying the matrix in place]
"""
