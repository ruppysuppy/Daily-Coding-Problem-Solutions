"""
Problem:

Given an unsorted array, in which all elements are distinct, find a "peak" element in
O(log N) time.

An element is considered a peak if it is greater than both its left and right
neighbors. It is guaranteed that the first and last elements are lower than all others.
"""

from typing import List


def get_peak(arr: List[int]) -> int:
    # implement similar method as binary search [since the element being searched is
    # not a concrete value (unlike binary search), but any value which is greater than
    # its neighbours, it can only be found without sorting]
    mid = len(arr) // 2
    if (
        mid > 0
        and arr[mid - 1] < arr[mid]
        and mid < len(arr)
        and arr[mid + 1] < arr[mid]
    ):
        return arr[mid]
    elif mid > 0 and arr[mid - 1] < arr[mid]:
        return get_peak(arr[mid:])
    return get_peak(arr[: mid + 1])


if __name__ == "__main__":
    print(get_peak([0, 2, 4, -1, 3, 1]))
    print(get_peak([0, 2, 4, 5, 3, 1]))
    print(get_peak([0, 2, 6, 5, 3, 1]))
    print(get_peak([0, 2, 4, 5, 7, 1]))
    print(get_peak([0, 8, 7, 5, 16, 1]))


"""
SPECS:

TIME COMPLEXITY: O(log(n))
SPACE COMPLEXITY: O(1)
"""

