'''
Problem:

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

Example:
[15, 5, 20, 10, 35, 15, 10] => true (since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55)
[15, 5, 20, 10, 35] => false
'''

# helper function to check for checking whether splitting into 2 subsets of equal sum is possible
def split_helper(arr, start, stop, sum_inner, sum_outer):
    # if the start and the stop pointers cross each other, the list cannot be split
    if (start >= stop):
        return False
    # if (sum_inner = sum_outer), we have found the split
    elif (sum_inner == sum_outer):
        return True
    
    # checking for possible splits (once with adding 1st element to sum_outer, again with last element, giving rise to a recursion tree)
    return (split_helper(arr, start+1, stop, sum_inner-arr[start], sum_outer+arr[start]) or \
        split_helper(arr, start, stop-1, sum_inner-arr[stop], sum_outer+arr[stop]))

# FUNCTION FOR PERFORMING THE OPERATION
def equal_sum_split_check(arr):
    # checking if the sum is odd (it cannot be split) 
    # [even though theoretically, empty set can be broken into 2 empty sets, we have condidered the case for valid elements]
    if (not arr or sum(arr) % 2 == 1):
        return False
    
    # sorting the list (pre-requisite for split_helper)
    arr.sort()

    # returning the value returned by split_helper
    return split_helper(arr, 0, len(arr)-1, sum(arr), 0)

# DRIVER CODE
print(equal_sum_split_check([15, 5, 20, 10, 35, 15, 10]))
print(equal_sum_split_check([15, 5, 20, 10, 35]))