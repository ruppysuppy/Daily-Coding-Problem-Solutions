"""
Problem:

In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal
from top left to bottom right are identical.

Here is an example:

1 2 3 4 8
5 1 2 3 4
4 5 1 2 3
7 4 5 1 2
Write a program to determine whether a given input is a Toeplitz matrix.
"""

from typing import List


def is_toeplitz_matrix(matrix: List[List[int]]) -> bool:
    n = len(matrix)
    m = len(matrix[0])
    # checking the diagonals starting from the left edge
    for i in range(n):
        val = matrix[i][0]
        for row, col in zip(range(i, n), range(m)):
            if matrix[row][col] != val:
                return False
    # checking the diagonals starting from the top edge
    for i in range(1, m):
        val = matrix[0][i]
        for row, col in zip(range(n), range(i, m)):
            if matrix[row][col] != val:
                return False
    return True


if __name__ == "__main__":
    print(
        is_toeplitz_matrix(
            [
                [1, 2, 3, 4, 8],
                [5, 1, 2, 3, 4],
                [4, 5, 1, 2, 3],
                [7, 4, 5, 1, 2]
            ]
        )
    )

    print(
        is_toeplitz_matrix(
            [
                [1, 2, 3, 4, 8],
                [5, 1, 2, 3, 4],
                [4, 5, 1, 2, 3],
                [7, 4, 5, 1, 1]
            ]
        )
    )


"""
SPECS:
TIME COMPLEXITY: O(n x m)
SPACE COMPLEXITY: O(1) [as zip and range both are generator functions]
[n = rows, m = columns]
"""
