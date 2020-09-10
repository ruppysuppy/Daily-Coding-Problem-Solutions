"""
Problem:

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. 
If such a subset cannot be made, then return null.
Integers can appear more than once in the list. You may assume all numbers in the list are positive.

Example:
[12, 1, 61, 5, 9, 2], 24 => [12, 9, 2, 1]
"""

# FUNCTION TO PERFORM THE OPERATION
def target_sum(arr, k):
    # Recursion Base Case 1 (Empty arr)
    if not arr:
        return None

    # Recursion Base Case 2 (Target sum = the 1st element of array)
    elif arr[0] == k:
        return [arr[0]]

    # Recursive call (considering arr[0] is included in the subset summing to k)
    temp = target_sum(arr[1:], k - arr[0])
    # if the function returns a list, arr[0] is added to it and returned
    if temp:
        return [arr[0]] + temp

    # if the function returns None, the result of the recursive call (considering arr[0] is excluded in the subset summing to k)
    return target_sum(arr[1:], k)


# DRIVER CODE
print(target_sum([12, 1, 61, 5, 9, 2], 24))
print(target_sum([12, 1, 61, 5, 9, 2], 61))
print(target_sum([12, 1, 61, 5, -108, 2], -106))
print(target_sum([12, 1, 61, 5, -108, 2], 1006))
