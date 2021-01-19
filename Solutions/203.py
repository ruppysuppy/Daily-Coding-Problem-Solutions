"""
Problem:

Suppose an array sorted in ascending order is rotated at some pivot unknown to you
beforehand. Find the minimum element in O(log N) time. You may assume the array does
not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.
"""

from typing import List


def find_pivot_helper(arr: List[int], low: int, high: int) -> int:
    if low == high:
        return high

    mid = (high + low) // 2
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    elif mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    elif arr[mid] > arr[high]:
        return find_pivot_helper(arr, mid + 1, high)
    return find_pivot_helper(arr, low, mid - 1)


def find_pivot(arr: List[int]) -> int:
    length = len(arr)
    # the pivot returns the last index of the rotated array
    pivot = find_pivot_helper(arr, 0, length)
    return (pivot + 1) % length


if __name__ == "__main__":
    print(find_pivot([5, 7, 10, 3, 4]))


"""
SPECS:

TIME COMPLEXITY: O(log(n))
SPACE COMPLEXITY: O(log(n)) [python doesn't support tail recursion optimization]
"""
