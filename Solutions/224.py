'''
Problem:

Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.
Do this in O(N) time.

Example:

Input = [1, 2, 3, 10]
Output = 7
'''


def find_smallest_subset_sum_not_in_arr(arr):
    res = 1

    for elem in arr:
        if (elem > res):
            break
        res += elem
    
    return res


print(find_smallest_subset_sum_not_in_arr([1, 2, 3, 10]))
print(find_smallest_subset_sum_not_in_arr([1, 2, 10]))
print(find_smallest_subset_sum_not_in_arr([1, 10]))