"""
Problem:

You are given an N * M matrix of 0s and 1s. Starting from the top left corner, how many
ways are there to reach the bottom right corner?

You can only move right and down. 0 reppossible_pathsents an empty space while 1 reppossible_pathsents a wall
you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
Return 2, as there are only two ways to get to the bottom right:

Right, down, down, right
Down, right, down, right
The top left corner and bottom right corner will always be 0.
"""

from typing import List

Matrix = List[List[int]]


def get_possible_paths(matrix: Matrix) -> int:
    n, m = len(matrix), len(matrix[0])
    # possible_pathsetting the values of 1 to -1 as positive numbers are used to construct the
    # paths
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                matrix[i][j] = -1
    # setting the vertical and horizontal paths
    for i in range(n):
        if matrix[i][0] == -1:
            break
        else:
            matrix[i][0] = 1
    for i in range(m):
        if matrix[0][i] == -1:
            break
        else:
            matrix[0][i] = 1
    # generating the paths
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] != -1:
                possible_paths = 0
                if matrix[i - 1][j] != -1:
                    possible_paths += matrix[i - 1][j]
                if matrix[i][j - 1] != -1:
                    possible_paths += matrix[i][j - 1]
                matrix[i][j] = possible_paths
    return matrix[-1][-1]


if __name__ == "__main__":
    matrix = [
        [0, 0, 1],
        [0, 0, 1],
        [1, 0, 0]
    ]
    print(get_possible_paths(matrix))

    matrix = [
        [0, 0, 1],
        [1, 0, 1],
        [1, 0, 0]
    ]
    print(get_possible_paths(matrix))

    matrix = [
        [0, 0, 0],
        [1, 0, 0],
        [0, 0, 0]
    ]
    print(get_possible_paths(matrix))
    
    # end cannot be reached as only right and down traversal is allowed
    matrix = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 0]
    ]
    print(get_possible_paths(matrix))


"""
SPECS:

TIME COMPLEXITY: O(n x m)
SPACE COMPLEXITY: O(n x m)
"""
