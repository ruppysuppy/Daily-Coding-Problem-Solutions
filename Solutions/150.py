"""
Problem:

Given a list of points, a central point, and an integer k, find the nearest k points
from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point
(1, 2), and k = 2, return [(0, 0), (3, 1)].
"""

from typing import List, Tuple

Position = Tuple[int, int]


def get_distance(point1: Position, point2: Position) -> float:
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


def KNN(arr: List[Position], center: Position, k: int) -> List[Position]:
    return sorted(arr, key=lambda position: get_distance(position, center))[:k]


if __name__ == "__main__":
    print(KNN([(0, 0), (5, 4), (3, 1)], (1, 2), 2))


"""
SPECS:

TIME COMPLEXITY: O(n x log(n))
SPACE COMPLEXITY: O(k)
"""
