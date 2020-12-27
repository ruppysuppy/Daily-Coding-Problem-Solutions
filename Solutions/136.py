"""
Problem:

Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle
containing only 1's and return its area.

For example, given the following matrix:

[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]
Return 4.
"""

from typing import List

Matrix = List[List[int]]


def is_row_extendable(matrix: Matrix, erow: int, scol: int, ecol: int) -> bool:
    return all(matrix[erow][scol:ecol])


def is_column_extendable(matrix: Matrix, ecol: int, srow: int, erow: int) -> bool:
    for row in range(srow, erow):
        if not matrix[row][ecol]:
            return False
    return True


def area_helper(
    matrix: Matrix,
    num_rows: int,
    num_cols: int,
    srow: int,
    erow: int,
    scol: int,
    ecol: int,
) -> int:
    current_area = (erow - srow) * (ecol - scol)
    row_ex_area, col_ex_area = 0, 0
    # checking if the area can be extended
    can_extend_row = erow < num_rows and is_row_extendable(matrix, erow, scol, ecol)
    if can_extend_row:
        row_ex_area = area_helper(
            matrix, num_rows, num_cols, srow, erow + 1, scol, ecol
        )
    can_extend_col = ecol < num_cols and is_column_extendable(matrix, ecol, srow, erow)
    if can_extend_col:
        col_ex_area = area_helper(
            matrix, num_rows, num_cols, srow, erow, scol, ecol + 1
        )
    return max(current_area, row_ex_area, col_ex_area)


def get_max_rect(matrix: Matrix) -> int:
    if not matrix:
        return 0
    # generating the maximum area
    max_area = 0
    num_rows, num_cols = len(matrix), len(matrix[0])
    for i in range(num_rows):
        for j in range(num_cols):
            upper_bound_area = (num_rows - i) * (num_cols - j)
            if matrix[i][j] and upper_bound_area > max_area:
                area = area_helper(matrix, num_rows, num_cols, i, i + 1, j, j + 1)
                max_area = max(area, max_area)
    return max_area


if __name__ == "__main__":
    matrix = [
        [1, 0, 0, 0],
        [1, 0, 1, 1],
        [1, 0, 1, 1],
        [0, 1, 0, 0]
    ]
    print(get_max_rect(matrix))

    matrix = [
        [1, 0, 0, 0],
        [1, 0, 1, 1],
        [1, 0, 1, 1],
        [0, 1, 1, 1]
    ]
    print(get_max_rect(matrix))

    matrix = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    print(get_max_rect(matrix))

    matrix = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    print(get_max_rect(matrix))

    matrix = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0],
        [0, 0, 0, 0]
    ]
    print(get_max_rect(matrix))

    matrix = [
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0]
    ]
    print(get_max_rect(matrix))


"""
SPECS:

TIME COMPLEXITY: O((n x m) ^ 2)
SPACE COMPLEXITY: O(n + m)
"""
