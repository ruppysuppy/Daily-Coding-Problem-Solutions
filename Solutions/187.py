"""
Problem:

You are given given a list of rectangles represented by min and max x- and y-coordinates. 
Compute whether or not a pair of rectangles overlap each other. If one rectangle completely covers another, it is considered overlapping.

Example:

Rectangles = [{
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
}]
Output = true (as the first and third rectangle overlap each other)
"""

# helper function to calculate the area under 2 rectangles (Used in problem 185)
def intersection(rect1, rect2):
    # segregating the rectangles by x-axis
    if rect1["top_left"][0] < rect2["top_left"][0]:
        left = rect1
        right = rect2
    else:
        left = rect2
        right = rect1

    # segregating the rectangles by y-axis
    if rect1["top_left"][1] > rect2["top_left"][1]:
        top = rect1
        bottom = rect2
    else:
        top = rect2
        bottom = rect1

    # getting the length of overlap on x-axis
    if (left["top_left"][0] + left["dimensions"][0]) < right["top_left"][0]:
        return 0
    else:
        span_x = (left["top_left"][0] + left["dimensions"][0]) - right["top_left"][0]

    # getting the length of overlap on y-axis
    if (top["top_left"][1] - top["dimensions"][1]) > bottom["top_left"][1]:
        return 0
    else:
        span_y = bottom["top_left"][1] - (top["top_left"][1] - top["dimensions"][1])

    # returning the overlapped area
    return span_x * span_y


# FUNCTION TO PERFORM THE OPERATION
def check_rectangles_intersection(rectangles):
    # storing the number of rectangles
    length = len(rectangles)

    # checking for intersection for each pair of rectangles
    for i in range(length - 1):
        for j in range(i + 1, length):
            if intersection(rectangles[i], rectangles[j]) != 0:
                return True

    return False


# DRIVER CODE
rectangles = [
    {"top_left": (1, 4), "dimensions": (3, 3)},
    {"top_left": (-1, 3), "dimensions": (2, 1)},
    {"top_left": (0, 5), "dimensions": (4, 3)},
]

print(check_rectangles_intersection(rectangles))

rectangles.pop(2)

print(check_rectangles_intersection(rectangles))
