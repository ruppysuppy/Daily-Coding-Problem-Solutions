"""
Problem:

You are given a list of N points (x1, y1), (x2, y2), ..., (xN, yN) representing a
polygon. You can assume these points are given in order; that is, you can construct the
polygon by connecting point 1 to point 2, point 2 to point 3, and so on, finally
looping around to connect point N to point 1.

Determine if a new point p lies inside this polygon. (If p is on the boundary of the
polygon, you should return False).
"""

from typing import List, Tuple

Point = Tuple[int, int]


def is_inside(points: List[Point], p: Point) -> bool:
    # Using the following concept:
    # if a stright line in drawn from the point p to its right (till infinity), the
    # drawn line will intersect the lines connecting the points odd number of times
    # (if p is enclosed by the points) else the the number of intersections will be
    # even (implying its outside the figure created by the points)

    # Details:
    # https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon

    if len(points) in (0, 1, 2):
        return False

    x, y = p
    last = points[0]
    intersections = 0
    same_height = set()

    for point in points[1:]:
        x1, y1 = last
        x2, y2 = point
        if min(y1, y2) <= y <= max(y1, y2) and x <= min(x1, x2):
            if y2 == y and point not in same_height:
                intersections += 1
                same_height.add(point)
            elif y1 == y and last not in same_height:
                intersections += 1
                same_height.add(last)
        last = point

    point = points[0]
    x1, y1 = last
    x2, y2 = point
    if max(y1, y2) >= y >= min(y1, y2) and x <= min(x1, x2):
        if y2 == y and point not in same_height:
            intersections += 1
            same_height.add(point)
        elif y1 == y and last not in same_height:
            intersections += 1
            same_height.add(last)
    if intersections % 2 == 1:
        return True
    return False


if __name__ == "__main__":
    print(is_inside([(4, 3), (5, 4), (6, 3), (5, 2)], (3, 3)))
    print(is_inside([(4, 3), (5, 4), (6, 3), (5, 2)], (5, 3)))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
