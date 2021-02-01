"""
Problem:

A wall consists of several rows of bricks of various integer lengths and uniform
height. Your goal is to find a vertical line going from the top to the bottom of the
wall that cuts through the fewest number of bricks. If the line goes through the edge
between two bricks, this does not count as a cut.

For example, suppose the input is as follows, where values in each row represent the
lengths of bricks in that row:

[[3, 5, 1, 1],
 [2, 3, 3, 2],
 [5, 5],
 [4, 4, 2],
 [1, 3, 3, 3],
 [1, 1, 6, 1, 1]]
The best we can we do here is to draw a line after the eighth brick, which will only
require cutting through the bricks in the third and fifth row.

Given an input consisting of brick lengths for each row such as the one above, return
the fewest number of bricks that must be cut to create a vertical line.
"""

from typing import List


def get_min_cut_position(wall: List[List[int]]) -> int:
    rows = len(wall)
    if rows == 1:
        cols = len(wall[0])
        if cols > 1:
            return wall[0][0]
        return wall[0][0] - 1
    # generating a hash map containing the positions with no bricks at any row
    no_brick_loaction = {}
    for i in range(rows):
        curr = 0
        for j in range(len(wall[i]) - 1):
            curr += wall[i][j]
            if curr not in no_brick_loaction:
                no_brick_loaction[curr] = 0
            no_brick_loaction[curr] += 1
    # the position with minimum bricks is returned
    if no_brick_loaction:
        key, _ = max(no_brick_loaction.items(), key=lambda x: x[1])
        return key
    # if all the rows contain 1 brick its cut from the length - 1 position
    return wall[0][0] - 1


if __name__ == "__main__":
    wall = [
        [3, 5, 1, 1],
        [2, 3, 3, 2],
        [5, 5],
        [4, 4, 2],
        [1, 3, 3, 3],
        [1, 1, 6, 1, 1],
    ]
    print(get_min_cut_position(wall))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
[n = number of elements in the matrix]
"""
