'''
Problem:

Given a circular array, compute its maximum subarray sum in O(n) time.

Example:

Input = [8, -1, 3, 4]
Output = 15 (as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around)

Input = [-4, 5, 1, 0]
Output = 6 (as we choose the numbers 5 and 1)
'''

# helper function (max of array using Kadane's algorithm)
def kadane(arr):
    # declaring the necessary variables
    max_sum = 0
    curr_sum = 0

    # iterating through the array
    for elem in arr:
        # updating current sum
        curr_sum += elem

        # updating current sum to 0 if it becomes negative
        curr_sum = max(curr_sum, 0)
        # updating max sum to hold the maximum
        max_sum = max(max_sum, curr_sum)
    
    return max_sum

# FUNCTION TO PERFORM THE OPERATION
def max_circular_subarr(arr):
    # getting the length of the array
    length = len(arr)
    # getting the maximum subarray sum of the array (without wrap)
    max_kadane = kadane(arr)
    # setting max_wrap to 0
    max_wrap = 0

    # iterating through the array
    for i in range(length):
        # summing all elements and negating all elements
        max_wrap += arr[i]
        arr[i] = -arr[i]

    # adding the max sum of the negated array to max wrap
    max_wrap += kadane(arr)

    # returning the maximum of wrapped sum and kadane's result
    return max(max_wrap, max_kadane)

# DRIVER CODE
print(max_circular_subarr([-4, 5, 1, 0]))
print(max_circular_subarr([8, -1, 3, 4]))
print(max_circular_subarr([-8, -1, -3, -4]))
print(max_circular_subarr([8, -1, 300, -1, 4]))