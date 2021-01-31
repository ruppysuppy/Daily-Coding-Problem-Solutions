"""
Problem:

Given an array of integers out of order, determine the bounds of the smallest window
that must be sorted in order for the entire array to be sorted. For example, given
[3, 7, 5, 6, 9], you should return (1, 3).
"""


from typing import List, Tuple


def get_sort_range(arr: List[int]) -> Tuple[int, int]:
    arr_sorted = sorted(arr)
    if arr_sorted == arr:
        return -1, -1
    # getting the start and end of the unsorted part of the array
    start, end = 0, 0
    for i in range(len(arr)):
        if arr[i] != arr_sorted[i]:
            start = i
            break
    for i in range(start, len(arr)):
        if arr[i] != arr_sorted[i]:
            end = i
    return start, end


if __name__ == "__main__":
    print(get_sort_range([3, 5, 6, 7, 9]))
    print(get_sort_range([3, 7, 5, 6, 9]))
    print(get_sort_range([5, 4, 3, 2, 1]))


"""
SPECS:

TIME COMPLEXITY: O(n x log(n))
SPACE COMPLEXITY: O(n)
"""
