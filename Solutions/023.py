"""
Problem:

You are given an M by N matrix consisting of booleans that represents a board. Each
True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number
of steps required to reach the end coordinate from the start. If there is no possible
path, then return null. You can move up, left, down, and right. You cannot move through
walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
 [t, t, f, t],
 [f, f, f, f],
 [f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of
steps required to reach the end is 7, since we would need to go through (1, 2) because
there is a wall everywhere else on the second row.
"""

from numpy import array
from sys import maxsize
from typing import List, Tuple, Union


Matrix_str = List[List[str]]
Matrix = List[List[Union[int, str]]]


def get_neighbours(pos: Tuple[int, int], n: int, m: int) -> List[Tuple[int, int]]:
    i, j = pos
    neighbours = [
        (i - 1, j),
        (i + 1, j),
        (i, j + 1),
        (i, j - 1),
    ]
    valid_neighbours = []
    for neighbour in neighbours:
        y, x = neighbour
        if 0 <= y < n and 0 <= x < m:
            valid_neighbours.append(neighbour)
    return valid_neighbours


def transform_matrix(matrix: Matrix_str, n: int, m: int) -> None:
    # helper function to transform Matrix_str to Matrix type
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "f":
                matrix[i][j] = 0


def get_min_steps_helper(matrix: Matrix, pos: Tuple[int, int], n: int, m: int) -> None:
    # helper function to calculate the distance of position from the source
    i, j = pos
    unexplored_positions = []
    neighbours = get_neighbours(pos, n, m)
    # calculate the distance for the neighbours
    for neighbour in neighbours:
        y, x = neighbour
        if matrix[y][x] != "t":
            if matrix[y][x] != 0:
                curr_value = matrix[y][x]
            else:
                curr_value = maxsize
                unexplored_positions.append(neighbour)
            matrix[y][x] = min(curr_value, matrix[i][j] + 1)
    # exploring unexplored positions
    for position in unexplored_positions:
        get_min_steps_helper(matrix, position, n, m)


def get_min_steps(
    matrix: Matrix_str, start: Tuple[int, int], end: Tuple[int, int]
) -> int:
    n = len(matrix)
    m = len(matrix[0])
    transform_matrix(matrix, n, m)
    # offseting start by 1 (as 0 represents unvisited positions)
    i, j = start
    matrix[i][j] = 1
    # calculating the distance for each position from the start
    neighbours = get_neighbours(start, n, m)
    # updating the value of neighbours (hard-coded to 2 as the starting position value
    # is 1)
    for neighbour in neighbours:
        y, x = neighbour
        if matrix[y][x] == 0:
            matrix[y][x] = 2
    # using helper to calculate the distance for the rest of the matrix
    for neighbour in neighbours:
        y, x = neighbour
        if matrix[y][x] == 2:
            get_min_steps_helper(matrix, neighbour, n, m)
    # matrix[y][x] - 1 is returned as initially the value was offsetted by +1
    y, x = end
    if matrix[y][x] == "t" or matrix[y][x] == 0:
        return None
    return matrix[y][x] - 1


if __name__ == "__main__":
    mat = [
        ["f", "f", "f", "f"],
        ["t", "t", "f", "t"],
        ["f", "f", "f", "f"],
        ["f", "f", "f", "f"],
    ]
    start = (3, 0)
    end = (0, 0)

    print(array(mat))
    print(get_min_steps(mat, start, end))


"""
SPECS:

TIME COMPLEXITY: O(n x m)
SPACE COMPLEXITY: O(n x m) [unexplored_positions can have at most 2 entries (repeated
n x m times)]
"""
