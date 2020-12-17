"""
Problem:

Given a list of integers and a number K, return which contiguous elements of the list
sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4].
"""

from typing import List, Optional


def get_arr_contiguous_sum(arr: List[int], k: int) -> Optional[List[int]]:
    length = len(arr)
    total_sum = 0
    start, end = 0, 0
    # generating the sequence using moving window
    for i in range(length):
        if total_sum == k:
            return arr[start:end]
        total_sum += arr[i]
        end = i + 1
        if total_sum > k:
            total_sum -= arr[start]
            start += 1
    if total_sum == k:
        return arr[start:end]
    return None


if __name__ == "__main__":
    print(get_arr_contiguous_sum([1, 2, 3, 4, 5], 0))
    print(get_arr_contiguous_sum([1, 2, 3, 4, 5], 1))
    print(get_arr_contiguous_sum([1, 2, 3, 4, 5], 5))
    print(get_arr_contiguous_sum([5, 4, 3, 4, 5], 12))
    print(get_arr_contiguous_sum([5, 4, 3, 4, 5], 11))
    print(get_arr_contiguous_sum([1, 2, 3, 4, 5], 9))
    print(get_arr_contiguous_sum([1, 2, 3, 4, 5], 3))
    print(get_arr_contiguous_sum([1, 2, 3, 4, 5], 300))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
