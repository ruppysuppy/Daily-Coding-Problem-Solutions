"""
Problem:

We can determine how "out of order" an array A is by counting the number of inversions
it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is,
a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three
inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions:
every distinct pair forms an inversion.
"""

from typing import List, Tuple


def merge(part_a: List[int], part_b: List[int]) -> Tuple[List[int], int]:
    # helper function for merge sort
    i, j = 0, 0
    merged_array = []
    a, a_inv = part_a
    b, b_inv = part_b
    inversions = a_inv + b_inv
    length_a, length_b = len(a), len(b)
    # merging the arrays
    while i < length_a and j < length_b:
        if a[i] < b[j]:
            merged_array.append(a[i])
            i += 1
        else:
            merged_array.append(b[j])
            inversions += length_a - i
            j += 1
    while i < length_a:
        merged_array.append(a[i])
        i += 1
    while j < length_b:
        merged_array.append(b[j])
        j += 1
    return merged_array, inversions


def merge_sort(arr: List[int]) -> Tuple[List[int], int]:
    length = len(arr)
    if length in (0, 1):
        return arr, 0

    mid = length // 2
    merged_array, inversions = merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))
    return merged_array, inversions


def count_inversions(arr: List[int]) -> int:
    _, inversions = merge_sort(arr)
    return inversions


if __name__ == "__main__":
    print(count_inversions([1, 2, 3, 4, 5]))
    print(count_inversions([2, 1, 3, 4, 5]))
    print(count_inversions([2, 4, 1, 3, 5]))
    print(count_inversions([2, 6, 1, 3, 7]))
    print(count_inversions([5, 4, 3, 2, 1]))


"""
SPECS:

TIME COMPLEXITY: O(n x log(n))
SPACE COMPLEXITY: O(log(n))
"""
