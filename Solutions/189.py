"""
Problem:

Given an array of elements, return the length of the longest subarray where all its
elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray
of distinct elements is [5, 2, 3, 4, 1].
"""

from typing import List


def max_unique_subarr(arr: List[int]) -> int:
    if not arr:
        return 0

    length = len(arr)
    cache = set()
    max_length, window_length, window_start = 0, 0, 0

    for i in range(length):
        if arr[i] not in cache:
            cache.add(arr[i])
            window_length += 1
            continue

        max_length = max(max_length, window_length)
        for j in range(window_start, i):
            cache.remove(arr[j])
            window_length -= 1
            if arr[j] == arr[i]:
                window_start = j
                cache.add(arr[j])
                window_length += 1
                break
    return max(max_length, window_length)


if __name__ == "__main__":
    print(max_unique_subarr([5, 1, 3, 5, 2, 3, 4, 1, 5]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
