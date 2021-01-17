"""
Problem:

Given an array and a number k that's smaller than the length of the array, rotate the
array to the right k elements in-place.
"""

from typing import List


def rotate_array_right(arr: List[int], k: int) -> List[int]:
    length = len(arr)
    k = k % length
    # rotating array
    if k > 0:
        cache = arr[-k:]
        for i in range(length - k - 1, -1, -1):
            arr[k + i] = arr[i]
        arr[:k] = cache
    return arr


if __name__ == "__main__":
    print(rotate_array_right([(i + 1) for i in range(5)], 9))
    print(rotate_array_right([(i + 1) for i in range(5)], 3))
    print(rotate_array_right([(i + 1) for i in range(5)], 2))
    print(rotate_array_right([(i + 1) for i in range(5)], 1))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n)
"""
