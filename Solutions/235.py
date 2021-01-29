"""
Problem:

Given an array of numbers of length N, find both the minimum and maximum using less
than 2 * (N - 2) comparisons.
"""

from typing import List, Tuple


def get_min_max(arr: List[int]) -> Tuple[int, int]:
    if not arr:
        return None, None

    length = len(arr)
    if length % 2 == 0:
        max_elem = max(arr[0], arr[1])
        min_elem = min(arr[0], arr[1])
        start = 2
    else:
        max_elem = min_elem = arr[0]
        start = 1

    # reducing the number of comparisons by comparing the array elements with themselves
    # effective comparisons is 3 for every 2 elements
    for i in range(start, length, 2):
        if arr[i] < arr[i + 1]:
            max_elem = max(max_elem, arr[i + 1])
            min_elem = min(min_elem, arr[i])
            continue
        max_elem = max(max_elem, arr[i])
        min_elem = min(min_elem, arr[i + 1])

    return min_elem, max_elem


if __name__ == "__main__":
    print(get_min_max([1000, 11, 445, 1, 330, 3000]))
    print(get_min_max([1000, 11, 445, 1, -330]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
