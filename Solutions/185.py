"""
Problem:

Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.

Example:

rectangle1 = {
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
rectangle2 = {
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
Output = 6
"""

# FUNCTION TO PERFORM THE OPERATION
def intersection(rectangle1, rectangle2):
    # segregating the rectangles by x-axis
    if rectangle1["top_left"][0] < rectangle2["top_left"][0]:
        left = rectangle1
        right = rectangle2
    else:
        left = rectangle2
        right = rectangle1

    # segregating the rectangles by y-axis
    if rectangle1["top_left"][1] > rectangle2["top_left"][1]:
        top = rectangle1
        bottom = rectangle2
    else:
        top = rectangle2
        bottom = rectangle1

    # getting the length of overlap on x-axis
    if (left["top_left"][0] + left["dimensions"][0]) < right["top_left"][0]:
        span_x = 0
    else:
        span_x = (left["top_left"][0] + left["dimensions"][0]) - right["top_left"][0]

    # getting the length of overlap on y-axis
    if (top["top_left"][1] - top["dimensions"][1]) > bottom["top_left"][1]:
        span_y = 0
    else:
        span_y = bottom["top_left"][1] - (top["top_left"][1] - top["dimensions"][1])

    # returning the overlapped area
    return span_x * span_y


# DRIVER CODE
rectangle1 = {"top_left": (1, 4), "dimensions": (3, 3)}  # width, height
rectangle2 = {"top_left": (0, 5), "dimensions": (4, 3)}  # width, height

print(intersection(rectangle1, rectangle2))
