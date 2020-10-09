"""
Problem:

Consider the following scenario: there are N mice and N holes placed at integer points
along a line. Given this, find a method that maps mice to holes such that the largest
number of steps any mouse takes is minimized.

Each move consists of moving one mouse one unit to the left or right, and only one
mouse can fit inside each hole.

For example, suppose the mice are positioned at [1, 4, 9, 15], and the holes are
located at [10, -5, 0, 16]. In this case, the best pairing would require us to send the
mouse at 1 to the hole at -5, so our function should return 6.
"""

from typing import List


def get_max_mouse_dist(mouse_position: List[int], hole_position: List[int]) -> int:
    # sorting the mice and holes to match them up
    mouse_position.sort()
    hole_position.sort()
    max_distance = 0
    # calculating the max distance
    for mouse, hole in zip(mouse_position, hole_position):
        max_distance = max(max_distance, abs(mouse - hole))
    return max_distance


if __name__ == "__main__":
    print(get_max_mouse_dist([1, 4, 9, 15], [10, -5, 0, 16]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
