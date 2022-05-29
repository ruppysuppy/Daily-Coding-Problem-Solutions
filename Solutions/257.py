"""
Problem:

Given an array of integers out of order, determine the bounds of the smallest window
that must be sorted in order for the entire array to be sorted. For example, given
[3, 7, 5, 6, 9], you should return (1, 3).
"""

from time import perf_counter
from random import randint
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


def get_sort_range_optimized(arr: List[int]) -> Tuple[int, int]:
    # Find rightmost possible index of left bound
    left = 0
    while left < len(arr) - 1 and arr[left] < arr[left + 1]:
        left += 1

    # Check if sorted
    if left == len(arr) - 1:
        return -1, -1

    # Find leftmost possible index of right bound
    right = len(arr) - 1
    while right > 0 and arr[right] > arr[right - 1]:
        right -= 1

    # Find the minimum and the maximum of the current window
    i = left + 1
    min_val = max_val = arr[left]
    while i <= right:
        if arr[i] < min_val:
            min_val = arr[i]
        if arr[i] > max_val:
            max_val = arr[i]
        i += 1

    # Expand the window leftwards to include all elements greater than the min,
    # so that everything remaining to the left is less than the smallest element to the right
    while left > 0 and arr[left - 1] > min_val:
        left -= 1

    # Expand the window rightwards to include all elements less than the max,
    # so that everything remaining to the right is greater than the largest element to the left
    while right < len(arr) - 1 and arr[right + 1] < max_val:
        right += 1

    return left, right


def print_both(arr: List[int]) -> None:
    for f in [get_sort_range, get_sort_range_optimized]:
        start = perf_counter()
        result = f(arr)
        end = perf_counter()
        print(f"{result} ({end - start:.3} sec)")


if __name__ == "__main__":
    print_both([3, 5, 6, 7, 9])
    print_both([3, 7, 5, 6, 9])
    print_both([5, 4, 3, 2, 1])
    print_both([0, 1, 3, 4, 2, 7, 5, 6, 8, 9])
    print_both(
        [0] + list([randint(1, 10**7 - 1) for _ in range(10**7 - 1)]) + [10**7]
    )  # Expecting (1, 9999999)


"""
SPECS:

get_sort_range:
TIME COMPLEXITY: O(n x log(n))
SPACE COMPLEXITY: O(n)

get_sort_range_optimized:
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1) (auxiliary)
"""
