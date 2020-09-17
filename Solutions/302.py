"""
Problem:

You are given a 2-d matrix where each cell consists of either /, \, or an empty space.
Write an algorithm that determines into how many regions the slashes divide the space.

For example, suppose the input for a three-by-six grid is the following:

\    /
 \  /
  \/
Considering the edges of the matrix as boundaries, this divides the grid into three
triangles, so you should return 3.
"""

from typing import Set, Tuple


def explore_region(
    position: Tuple[int, int], empty_spaces: Set, nrows: int, ncols: int
) -> None:
    # dfs helper to remove all adjoining empty spaces for each region
    if position not in empty_spaces:
        return
    # travelling to the adjoining spaces
    empty_spaces.remove(position)
    x, y = position
    if x > 0:
        explore_region((x - 1, y), empty_spaces, nrows, ncols)
    if x < nrows - 1:
        explore_region((x + 1, y), empty_spaces, nrows, ncols)
    if y > 0:
        explore_region((x, y - 1), empty_spaces, nrows, ncols)
    if y < ncols - 1:
        explore_region((x, y + 1), empty_spaces, nrows, ncols)


def get_region_count(matrix: str) -> int:
    nrows, ncols = len(matrix), len(matrix[0])
    empty_spaces = set()
    for row in range(nrows):
        for col in range(ncols):
            if matrix[row][col] == " ":
                empty_spaces.add((row, col))
    # traversing through the empty spaces
    regions = 0
    while empty_spaces:
        # random position selection
        for pos in empty_spaces:
            position = pos
            break
        explore_region(position, empty_spaces, nrows, ncols)
        regions += 1
    return regions


if __name__ == "__main__":
    matrix = [
        list(r"\    /"),
        list(r" \  / "),
        list(r"  \/  ")
    ]
    print(get_region_count(matrix))

    matrix = [
        list(r"     /"),
        list(r" \  / "),
        list(r"  \/  ")
    ]
    print(get_region_count(matrix))

    matrix = [
        list(r"     /"),
        list(r" \  / "),
        list(r"  \   ")
    ]
    print(get_region_count(matrix))


"""
SPECS:

TIME COMPLEXITY: O(row x column)
SPACE COMPLEXITY: O(row x column)
"""
