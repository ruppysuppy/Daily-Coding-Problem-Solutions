"""
Problem:

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear
time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4
(the index of 8 in the array).

You can assume all the integers in the array are unique.
"""

from typing import List


def find_pivot_helper(arr: List[int], start: int, end: int, length: int) -> int:
    if end < start:
        return 0

    mid = (start + end) // 2
    if mid > 0 and arr[mid - 1] > arr[mid]:
        return mid
    elif mid < length - 1 and arr[mid + 1] < arr[mid]:
        return mid + 1
    elif arr[start] < arr[mid]:
        return find_pivot_helper(arr, mid + 1, end, length)
    elif arr[end] > arr[mid]:
        return find_pivot_helper(arr, start, mid - 1, length)


def binary_search(arr: List[int], low: int, high: int, element: int) -> int:
    if high < low:
        return -1

    mid = (low + high) // 2
    if element == arr[mid]:
        return mid
    if element > arr[mid]:
        return binary_search(arr, (mid + 1), high, element)
    else:
        return binary_search(arr, low, (mid - 1), element)


def pivoted_binary_search(arr: List[int], element: int) -> int:
    length = len(arr)
    pivot = find_pivot_helper(arr, 0, length - 1, length)

    if arr[pivot] == element:
        return pivot
    if arr[pivot] < element:
        element_position = binary_search(arr, pivot + 1, length - 1, element)
        if element_position != -1:
            return element_position
        element_position = binary_search(arr, 0, pivot - 1, element)
        if element_position != -1:
            return element_position
        return -1
    return -1


if __name__ == "__main__":
    arr = [13, 18, 25, 2, 8, 10]

    print(pivoted_binary_search(arr, 8))
    print(pivoted_binary_search(arr, 10))
    print(pivoted_binary_search(arr, 15))
    print(pivoted_binary_search(arr, 2))

    arr = [25, 2, 8, 10, 13, 18]

    print(pivoted_binary_search(arr, 8))

    arr = [8, 10, 13, 18, 25, 2]

    print(pivoted_binary_search(arr, 8))


"""
SPECS:

TIME COMPLEXITY: O(log(n))
SPACE COMPLEXITY: O(log(n)) [recursion depth]
"""
