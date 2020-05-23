'''
Problem:

Given an array of elements, return the length of the longest subarray where all its elements are distinct.

Example:

Input = [5, 1, 3, 5, 2, 3, 4, 1]
Output = 5 (as the longest subarray of distinct elements is [5, 2, 3, 4, 1])
'''

# FUNCTION TO PERFORM THE OPERATION
def max_unique_subarr(arr):
    # check for empty array
    if (not arr):
        return 0

    # declaring the required variables
    length = len(arr)
    cache = set()
    max_len = 0
    curr_len = 0
    pos = 0

    # iterating through the array
    for i in range(length):
        # if the element is not present in the moving window, its added to cache
        if (arr[i] not in cache):
            cache.add(arr[i])
            curr_len += 1
        else:
            # updating max_len if curr_len is larger
            if (max_len < curr_len):
                max_len = curr_len
            
            # if the element is present in the moving window, the elements before the 1st occurence in the window are removed
            for j in range(pos, i):
                cache.remove(arr[j])
                curr_len -= 1

                # when the 1st occurance is found, the required updates are done and the control breaks out of the loop
                if (arr[j] == arr[i]):
                    pos = j
                    cache.add(arr[j])
                    curr_len += 1
                    break
            
    
    # updating max_len after exiting the loop
    if (max_len < curr_len):
        max_len = curr_len
    
    return max_len

# DRIVER CODE
print(max_unique_subarr([5, 1, 3, 5, 2, 3, 4, 1, 5]))