"""
Problem:

Given a 2-D matrix representing an image, a location of a pixel in the screen and a
color C, replace the color of the given pixel and all adjacent same colored pixels
with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for
green:

B B W
W W W
W W W
B B B
Becomes

B B G
G G G
G G G
B B B
"""

from typing import List, Set, Tuple
from numpy import array

Matrix = List[List[int]]
Position = Tuple[int, int]


def generate_neighbours(position: Position, rows: int, cols: int) -> List[Position]:
    i, j = position
    valid_neighbours = []
    neighbours = [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j + 1),
        (i + 1, j + 1),
        (i + 1, j),
        (i + 1, j - 1),
        (i, j - 1),
    ]
    for neighbour in neighbours:
        y, x = neighbour
        if (0 <= x < cols) and (0 <= y < rows):
            valid_neighbours.append(neighbour)
    return valid_neighbours


def update_color_dfs_helper(
    matrix: Matrix,
    position: Position,
    new_color: str,
    prev_color: str,
    visited: Set[Position],
    rows: int,
    cols: int,
) -> None:
    i, j = position
    matrix[i][j] = new_color
    visited.add(position)

    neighbours = generate_neighbours(position, rows, cols)
    for neighbour in neighbours:
        y, x = neighbour
        if neighbour not in visited and matrix[y][x] == prev_color:
            update_color_dfs_helper(
                matrix, neighbour, new_color, prev_color, visited, rows, cols
            )


def update_color(matrix: Matrix, position: Position, new_color: str) -> Matrix:
    rows = len(matrix)
    cols = len(matrix[0])
    i, j = position

    update_color_dfs_helper(
        matrix, position, new_color, matrix[i][j], set(), rows, cols
    )
    return matrix


if __name__ == "__main__":
    print("Initial Matrix:")
    matrix = [
        ["B", "B", "W"],
        ["W", "W", "W"],
        ["W", "W", "W"],
        ["B", "B", "B"]
    ]
    print(array(matrix))
    print("Updated Matrix:")
    print(array(update_color(matrix, (2, 2), "G")))
    print()

    print("Initial Matrix:")
    matrix = [
        ["B", "B", "W"],
        ["W", "W", "W"],
        ["W", "W", "W"],
        ["B", "B", "B"]
    ]
    print(array(matrix))
    print("Updated Matrix:")
    print(array(update_color(matrix, (3, 2), "G")))
    print()

    print("Initial Matrix:")
    matrix = [
        ["B", "B", "W"],
        ["W", "W", "W"],
        ["W", "W", "W"],
        ["B", "B", "B"]
    ]
    print(array(matrix))
    print("Updated Matrix:")
    print(array(update_color(matrix, (0, 0), "G")))


"""
SPECS:

TIME COMPLEXITY: O(n x m)
SPACE COMPLEXITY: O(n x m)
"""
