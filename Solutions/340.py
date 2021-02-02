"""
Problem:

Given a set of points (x, y) on a 2D cartesian plane, find the two closest points. For
example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)],
return [(-1, -1), (1, 1)].
"""

from math import sqrt
from sys import maxsize
from typing import List, Tuple


Point = Tuple[int, int]


def get_distance(pt1: Point, pt2: Point) -> float:
    x1, y1 = pt1
    x2, y2 = pt2
    dist = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    return dist


def get_nearest_points(pts_arr: List[Point]) -> List[Point]:
    length = len(pts_arr)
    dist = maxsize
    pt1, pt2 = None, None
    
    for index_1 in range(length):
        for index_2 in range(index_1 + 1, length):
            pt1_temp, pt2_temp = pts_arr[index_1], pts_arr[index_2]
            dist_temp = get_distance(pt1_temp, pt2_temp)
            if dist_temp < dist:
                dist = dist_temp
                pt1, pt2 = pt1_temp, pt2_temp
    return [pt1, pt2]


if __name__ == "__main__":
    print(get_nearest_points([(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(1)
"""
