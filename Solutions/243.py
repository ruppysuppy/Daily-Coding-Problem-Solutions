'''
Problem:

Given an array of numbers N and an integer k, your task is to split N into k partitions such that the maximum sum of any partition is minimized. 
Return this sum.

Example:

N = [5, 1, 2, 7, 3, 4]
k = 3
Output = 8 (since the optimal partition is [5, 1, 2], [7], [3, 4])
'''

from sys import maxsize


def minimize_partition_sum_helper(arr, k):
    # if the number of partition is 1, using the entire array as partition
    if k == 1:
        return [arr], sum(arr)

    min_val = maxsize
    min_cand = None
    # checking all possible partitions
    for i in range(len(arr)):
        arr_1, sum_1 = [arr[:i]], sum(arr[:i])
        arr_2, sum_2 = minimize_partition_sum_helper(arr[i:], k - 1)
        candidate = arr_1 + arr_2, max(sum_1, sum_2)
        if candidate[1] < min_val:
            min_val = candidate[1]
            min_cand = candidate
    return min_cand


def minimize_partition_sum(arr, k):
    _, max_sum = minimize_partition_sum_helper(arr, k)
    return max_sum


# DRIVER CODE
print(minimize_partition_sum([5, 1, 2, 7, 3, 4], 3))