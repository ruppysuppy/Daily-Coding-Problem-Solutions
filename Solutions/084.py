"""
Problem:

Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1
represents land and 0 represents water, so an island is a group of 1s that are
neighboring and their perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""

from typing import List, Tuple

from DataStructures.Queue import Queue

GridShape = Tuple[int, int]
Matrix = List[List[int]]
Position = Tuple[int, int]


def get_neighbours(position: Position, grid_shape: GridShape) -> List[Position]:
    n, m = grid_shape
    i, j = position
    neighbours = []
    position_list = [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
    ]
    for curr_position in position_list:
        y, x = curr_position
        if 0 <= x < m and 0 <= y < n:
            neighbours.append(curr_position)
    return neighbours


def remove_island(matrix: Matrix, position: Position, grid_shape: GridShape) -> None:
    # using bfs to remove the islands
    queue = Queue()
    queue.enqueue(position)

    while not queue.is_empty():
        curr_position = queue.dequeue()
        i, j = curr_position
        if matrix[i][j] == 1:
            matrix[i][j] = 0
            for neighbour in get_neighbours((i, j), grid_shape):
                y, x = neighbour
                if matrix[y][x] == 1:
                    queue.enqueue(neighbour)


def island_count(matrix: Matrix) -> int:
    count = 0
    n, m = len(matrix), len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                remove_island(matrix, (i, j), (n, m))
                count += 1
    return count


if __name__ == "__main__":
    matrix = [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
    ]
    print(island_count(matrix))


"""
SPECS:

TIME COMPLEXITY: O(n x m)
SPACE COMPLEXITY: O(n x m)
"""
