"""
Problem:

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12
"""

from typing import List

Matrix = List[List[int]]


def unwind_matrix_helper(matrix: Matrix, ring: int, n: int, m: int) -> List[int]:
    current_ring_elems = []
    # 1st row
    for i in range(ring, m - ring):
        current_ring_elems.append(matrix[ring][i])
    # last column
    for i in range(ring + 1, n - ring):
        current_ring_elems.append(matrix[i][m - ring - 1])
    # last row
    if n > 1 and m > 1:
        for i in range(m - ring - 2, ring - 1, -1):
            current_ring_elems.append(matrix[n - ring - 1][i])
    # 1st column
    if n > 1 and m > 1:
        for i in range(n - ring - 2, ring, -1):
            current_ring_elems.append(matrix[i][ring])
    return current_ring_elems


def unwind_matrix(matrix: Matrix) -> List[int]:
    if not matrix:
        return []
    n = len(matrix)
    m = len(matrix[0])
    unwound_matrix = []
    if n > 1 and m > 1:
        for i in range(max(n, m) // 2):
            unwound_matrix.extend(unwind_matrix_helper(matrix, i, n, m))
    else:
        unwound_matrix = unwind_matrix_helper(matrix, 0, n, m)
    return unwound_matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
    ]
    for elem in unwind_matrix(matrix):
        print(elem)

    print()
    matrix = [[1, 2, 3], [4, 5, 6]]
    for elem in unwind_matrix(matrix):
        print(elem)

    print()
    matrix = [[1, 4], [2, 5], [3, 6]]
    for elem in unwind_matrix(matrix):
        print(elem)

    print()
    matrix = [[1], [2], [3], [4], [5], [6]]
    for elem in unwind_matrix(matrix):
        print(elem)

    print()
    matrix = [[1, 2, 3]]
    for elem in unwind_matrix(matrix):
        print(elem)


"""
SPECS:

TIME COMPLEXITY: O(n x m)
SPACE COMPLEXITY: O(n x m)
"""
