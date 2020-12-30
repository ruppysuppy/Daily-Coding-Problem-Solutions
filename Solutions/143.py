"""
Problem:

Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x Ordering within a
part can be arbitrary.
For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be
[9, 3, 5, 10, 10, 12, 14]
"""

from typing import List, Optional


def separate_with_pivot(arr: List[int], i: int, j: int, x: int) -> Optional[int]:
    if not arr:
        return
    # separating the elements less than x and greater than or equal to x
    while i < j:
        if arr[i] >= x and arr[j] < x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            continue
        if arr[i] < x:
            i += 1
        if arr[j] >= x:
            j -= 1
    if (arr[i] < x) and (i + 1 < len(arr)):
        return i + 1
    return i


def pivot_list(arr: List[int], x: int) -> List[int]:
    length = len(arr)
    temp = separate_with_pivot(arr, 0, length - 1, x)
    pivot_start = temp if temp else 0
    separate_with_pivot(arr, pivot_start, length - 1, x + 1)
    return arr


if __name__ == "__main__":
    print(pivot_list([9, 12, 3, 5, 14, 10, 10], 10))
    print(pivot_list([9, 12, 3, 5, 14, 10, 10], 8))
    print(pivot_list([9, 12, 3, 5, 11, 10, 10], 10))
    print(pivot_list([9, 12, 14, 10, 10], 8))
    print(pivot_list([3, 5], 8))
    print(pivot_list([8, 8, 8], 8))
    print(pivot_list([], 8))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
