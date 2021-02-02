"""
Problem:

Describe an algorithm to compute the longest increasing subsequence of an array of
numbers in O(n log n) time.
"""

from typing import List


def get_ceil_index(arr: List[int], l: int, r: int, key: int) -> int:
    while r - l > 1:
        m = l + (r - l) // 2
        if arr[m] >= key:
            r = m
        else:
            l = m
    return r


def get_longest_increasing_subsequence(arr: List[int]) -> int:
    length = len(arr)
    tail_table = [0 for i in range(length)]
    tail_table[0] = arr[0]
    result_length = 1

    for i in range(1, length):
        if arr[i] < tail_table[0]:
            # new smallest value
            tail_table[0] = arr[i]
        elif arr[i] > tail_table[result_length - 1]:
            # current element is a part of a increasing subsequence
            tail_table[result_length] = arr[i]
            result_length += 1
        else:
            # current element is the last candidate of an existing subsequence and will
            # replace ceil value in tail_table
            tail_table[get_ceil_index(tail_table, -1, result_length - 1, arr[i])] = arr[
                i
            ]
    return result_length


if __name__ == "__main__":
    print(get_longest_increasing_subsequence([1, 2, 3, 4, 5]))
    print(get_longest_increasing_subsequence([1, 2, 3, 5, 4]))
    print(get_longest_increasing_subsequence([1, 4, 1, 2, 3]))
    print(get_longest_increasing_subsequence([5, 4, 3, 2, 1]))


"""
SPECS:

TIME COMPLEXITY: O(n x log(n))
SPACE COMPLEXITY: O(n)
"""
