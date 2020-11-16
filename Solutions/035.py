"""
Problem:

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of
the array so that all the Rs come first, the Gs come second, and the Bs come last. You
can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become
['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""

from typing import List


def segregate(arr: List[str]) -> None:
    length = len(arr)
    pos = 0
    # pass for segregating "R"s
    for i in range(length):
        if arr[i] == "R":
            arr[i], arr[pos] = arr[pos], arr[i]
            pos += 1
    # pass for segregating "G"s
    for i in range(pos, length):
        if arr[i] == "G":
            arr[i], arr[pos] = arr[pos], arr[i]
            pos += 1


if __name__ == "__main__":
    arr = ["G", "B", "R", "R", "B", "R", "G"]
    segregate(arr)
    print(arr)


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
