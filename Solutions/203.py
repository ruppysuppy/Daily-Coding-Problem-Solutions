'''
Problem:

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. 
Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.

Example:

Input = [5, 7, 10, 3, 4]
Output = 3
'''

# helper function to perform the computation
def find_pivot_helper(arr, low, high):
    # base case for recursion
    if (low == high):
        return high
    
    # getting the mid
    mid = (high + low) // 2

    # checking if the mid is the pivot
    if (mid < high and arr[mid] > arr[mid + 1]):
        return mid
    # checking if mid-1 is the pivot
    elif (mid > low and arr[mid] < arr[mid - 1]):
        return (mid - 1)
    # checking if the pivot is on the right of mid
    elif (arr[mid] > arr[high]):
        return find_pivot_helper(arr, mid+1, high)
    # if the pivot is on the left of mid
    return find_pivot_helper(arr, low, mid-1)

# FUNCTION TO PERFORM THE OPERATION
def find_pivot(arr):
    # getting the length of the array
    length = len(arr)
    # finding the pivot
    piv = find_pivot_helper(arr, 0, length)
    # returning the 1st index in the pivoted array
    return ((piv + 1) % length)

# DRIVER CODE
print(find_pivot([5, 7, 10, 3, 4]))