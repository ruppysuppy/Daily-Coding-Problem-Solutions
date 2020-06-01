'''
Problem:

Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset (i, j) satisfies either i % j = 0 or j % i = 0.

Example:

Input = [3, 5, 10, 20, 21]
Output = [5, 10, 20]

Input = [1, 3, 6, 24]
Output = [1, 3, 6, 24]
'''

# helper function to perform the computation
def get_largest_subset_helper(arr, prev_num=1, curr_ind=0, prev_subset=[]):
    # if the end of the array has been reached, the previous subsets are returned (base for recursion)
    if (curr_ind == len(arr)):
        return prev_subset

    # getting the current element
    curr_elem = arr[curr_ind]

    # calling the helper function recursively
    res = get_largest_subset_helper(arr, prev_num, curr_ind+1, prev_subset)

    # checking if the element is divisible by the last element (since it would contain all other smaller factors too)
    if (curr_elem % prev_num == 0):
        # generating the alternate result (with the element added)
        alternate_res = get_largest_subset_helper(arr, curr_elem, curr_ind+1, prev_subset+[curr_elem])

        # returning the longer result
        return max(alternate_res, res, key=lambda result: len(result))

    # returning the result in case its not divisible
    return res

# FUNCTION TO PERFORM THE OPERATION
def get_largest_subset(arr):
    # sorting the array
    arr.sort()
    # calling the helper function on the array
    return get_largest_subset_helper(arr, prev_subset=[])

# DRIVER CODE
print(get_largest_subset([]))
print(get_largest_subset([2]))
print(get_largest_subset([2, 3]))
print(get_largest_subset([3, 5, 10, 20, 21]))
print(get_largest_subset([1, 3, 6, 24]))
print(get_largest_subset([3, 9, 15, 30]))
print(get_largest_subset([2, 3, 9, 15, 30]))