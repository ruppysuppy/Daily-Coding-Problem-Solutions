"""
Problem:

Given an array of numbers and a number k, determine if there are three entries in the
array which add up to the specified number k. For example, given [20, 303, 3, 4, 25]
and k = 49, return true as 20 + 4 + 25 = 49.
"""

from typing import List


def target_sum_of_two(arr: List[int], k: int, index_1: int, index_2: int) -> bool:
    while index_1 < index_2:
        elem_1, elem_2 = arr[index_1], arr[index_2]
        curr_sum = elem_1 + elem_2
        if curr_sum == k:
            return True
        elif curr_sum < k:
            index_1 += 1
        else:
            index_2 -= 1
    return False


def target_sum_of_three(arr: List[int], k: int) -> bool:
    length = len(arr)
    # sorting the array to utilize the optimizations offered by a sorted array to find
    # target sum of 2 numbers
    arr.sort()

    for index_1, elem in enumerate(arr):
        index_2, index_3 = index_1 + 1, length - 1
        if elem >= k:
            break
        if target_sum_of_two(arr, k - elem, index_2, index_3):
            return True
    return False


if __name__ == "__main__":
    print(target_sum_of_three([20, 303, 3, 4, 25], 49))
    print(target_sum_of_three([20, 303, 3, 4, 25], 50))
    print(target_sum_of_three([20, 300, -300, 4, 25], 25))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(1)
"""
