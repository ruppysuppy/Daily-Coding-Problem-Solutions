"""
Problem:

You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it. You start from the first
point.

Example: Input: [(0, 0), (1, 1), (1, 2)] Output: 2 It takes 1 step to move from (0, 0)
to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
"""

from typing import List, Tuple


def get_min_steps(sequence: List[Tuple[int, int]]) -> int:
    length = len(sequence)
    if length in [0, 1]:
        return 0

    curr_position = sequence[0]
    total_distance = 0
    for next_position in sequence[1:]:
        i, j = curr_position
        y, x = next_position
        total_distance += max((abs(y - i)), abs(x - j))
        curr_position = next_position
    return total_distance


if __name__ == "__main__":
    print(get_min_steps([]))
    print(get_min_steps([(0, 0)]))
    print(get_min_steps([(0, 0), (1, 1), (1, 2)]))
    print(get_min_steps([(0, 0), (1, 1), (1, 2), (3, 4)]))
    print(get_min_steps([(0, 0), (1, 1), (1, 2), (3, 6)]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
