"""
Problem:

Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]

Follow-up: What if you couldn't use any extra space?
"""

from numpy import array
from typing import List

Matrix = List[List[int]]


def rotate_matrix(matrix: Matrix) -> Matrix:
    num_layers = len(matrix) // 2
    max_index = len(matrix) - 1
    # rotating the matrix
    for layer in range(num_layers):
        for index in range(layer, max_index - layer):
            (
                matrix[layer][index],
                matrix[max_index - index][layer],
                matrix[max_index - layer][max_index - index],
                matrix[index][max_index - layer],
            ) = (
                matrix[max_index - index][layer],
                matrix[max_index - layer][max_index - index],
                matrix[index][max_index - layer],
                matrix[layer][index],
            )
    return matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(array(matrix))
    print(array(rotate_matrix(matrix)))
    print()

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print(array(matrix))
    print(array(rotate_matrix(matrix)))


"""
SPECS:

TIME COMPLEXITY: O(n x m)
SPACE COMPLEXITY: O(1)
"""
