"""
Problem:

You are given given a list of rectangles represented by min and max x- and
y-coordinates. Compute whether or not a pair of rectangles overlap each other. If one
rectangle completely covers another, it is considered overlapping.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}

return true as the first and third rectangle overlap each other.
"""

from typing import Dict, List, Tuple

Rectangle = Dict[str, Tuple[int, int]]


def get_intersection_area(rect1: List[Rectangle], rect2: List[Rectangle]) -> int:
    if rect1["top_left"][0] < rect2["top_left"][0]:
        left = rect1
        right = rect2
    else:
        left = rect2
        right = rect1
    if rect1["top_left"][1] > rect2["top_left"][1]:
        top = rect1
        bottom = rect2
    else:
        top = rect2
        bottom = rect1
    if (left["top_left"][0] + left["dimensions"][0]) < right["top_left"][0]:
        return 0
    else:
        span_x = (left["top_left"][0] + left["dimensions"][0]) - right["top_left"][0]
    if (top["top_left"][1] - top["dimensions"][1]) > bottom["top_left"][1]:
        return 0
    else:
        span_y = bottom["top_left"][1] - (top["top_left"][1] - top["dimensions"][1])
    return span_x * span_y


def get_covered_area(rect: Rectangle) -> int:
    width, height = rect["dimensions"]
    return width * height


def check_rectangles_intersection(rectangles: List[Rectangle]) -> bool:
    length = len(rectangles)
    # checking for intersection for each pair of rectangles
    for i in range(length - 1):
        for j in range(i + 1, length):
            intersection_area = get_intersection_area(rectangles[i], rectangles[j])
            rect1_area = get_covered_area(rectangles[i])
            rect2_area = get_covered_area(rectangles[j])
            if intersection_area in (rect1_area, rect2_area):
                return True
    return False


if __name__ == "__main__":
    # NOTE: THE QUESTION STATEMENT IS WRONG THE RECTANGLES 1 & 3 DOES NOT OVERLAP BUT
    #       ONLY INTERSECT (SMALL MODIFICATION DONE TO MAKE THEM OVERLAP)
    rectangles = [
        {"top_left": (1, 4), "dimensions": (3, 3)},
        {"top_left": (-1, 3), "dimensions": (2, 1)},
        {"top_left": (0, 5), "dimensions": (4, 4)},  # MODIFICATION
    ]

    print(check_rectangles_intersection(rectangles))

    rectangles.pop()

    print(check_rectangles_intersection(rectangles))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(1)
"""
