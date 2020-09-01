"""
Problem:

The skyline of a city is composed of several buildings of various widths and heights,
possibly overlapping one another when viewed from a distance. We can represent the
buildings using an array of (left, right, height) tuples, which tell us where on an
imaginary x-axis a building begins and ends, and how tall it is. The skyline itself can
be described by a list of (x, height) tuples, giving the locations at which the height
visible to a distant observer changes, and each new height.

Given an array of buildings as described above, create a function that returns the
skyline.

For example, suppose the input consists of the buildings
[(0, 15, 3), (4, 11, 5), (19, 23, 4)]. In aggregate, these buildings would create a
skyline that looks like the one below.

     ______  
    |      |        ___
 ___|      |___    |   | 
|   |   B  |   |   | C |
| A |      | A |   |   |
|   |      |   |   |   |
------------------------
As a result, your function should return
[(0, 3), (4, 5), (11, 3), (15, 0), (19, 4), (23, 0)].
"""

from sys import maxsize
from typing import List, Tuple


def get_skyline(arr: List[Tuple[int, int, int]]) -> List[Tuple[int, int]]:
    # getting the bounds of the skyline
    start = maxsize
    end = -maxsize
    for start_curr, end_curr, _ in arr:
        start = min(start, start_curr)
        end = max(end, end_curr)
    # generating the skyline
    skyline = [0 for _ in range(start, end + 1)]
    offset = start
    for start_curr, end_curr, height in arr:
        for i in range(start_curr - offset, end_curr - offset):
            skyline[i] = max(skyline[i], height)
    # generating result from the skyline
    result = []
    for i in range(start - offset, end - offset):
        if i == 0 or skyline[i] != skyline[i - 1]:
            result.append((i + offset, skyline[i]))
    result.append((end, 0))
    return result


if __name__ == "__main__":
    print(get_skyline([(0, 15, 3), (4, 11, 5), (19, 23, 4)]))


"""
SPECS:

TIME COMPLEXITY: O(max(arr) - min(arr))
SPACE COMPLEXITY: O(max(arr) - min(arr))
"""
