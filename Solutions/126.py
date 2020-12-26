"""
Problem:

Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6]
rotated by two becomes [3, 4, 5, 6, 1, 2]. Try solving this without creating a copy of
the list. How many swap or move operations do you need?
"""

from typing import List


def rotate_list_once(arr: List[int], length: int) -> None:
    # updates the list inplace
    first_elem = arr[0]
    for i in range(length - 1):
        arr[i] = arr[i + 1]
    arr[length - 1] = first_elem


def rotate_list(arr: List[int], k: int) -> List[int]:
    length = len(arr)
    k = k % length
    for _ in range(k):
        rotate_list_once(arr, length)
    return arr


if __name__ == "__main__":
    print(rotate_list([1, 2, 3, 4, 5, 6], 0))
    print(rotate_list([1, 2, 3, 4, 5, 6], 2))
    print(rotate_list([1, 2, 3, 4, 5, 6], 4))
    print(rotate_list([1, 2, 3, 4, 5, 6], 6))
    print(rotate_list([1, 2, 3, 4, 5, 6], 10))
    print(rotate_list([1, 2, 3, 4, 5, 6], 1_000_000_000))


"""
SPECS:

TIME COMPLEXITY: O(k x n)
SPACE COMPLEXITY: O(1)
"""
