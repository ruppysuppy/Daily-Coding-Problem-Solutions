'''
Problem:

Given an array of numbers, find the length of the longest increasing subsequence in the array. 
The subsequence does not necessarily have to be contiguous.

Example: 

Input = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
Output = 6 (the subsequence is [0, 2, 6, 9, 11, 15])
'''

# FUNCTION TO PERFORM THE OPERATION
def longest_increasing_subsequence(arr, length):
    # creating the array to implement dynamic programming
    arr_dp = [1 for i in range(length)]

    # looping over the input arr (from the 2nd element)
    for i in range(1, length):
        # looping from the beginning to the current position
        for j in range(i):
            # if the element at current pos is larger than the one at j'th pos
            # (implying its an increasing subsequence)
            if (arr[i] > arr[j]):
                # the value used for dynamic programming is updated
                # (max(arr_dp[i] (already a part of a larger sub-seq), arr_dp[j]+1 (the resultant sub-seq formed by extending from the j'th pos)))
                arr_dp[i] = max(arr_dp[i], arr_dp[j]+1)
    
    return max(arr_dp)

# DRIVER CODE
arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(longest_increasing_subsequence(arr, len(arr)))