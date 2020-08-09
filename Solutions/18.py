"""
Problem:

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
[10, 5, 2, 7, 8, 7], 3 => [10, 7, 8, 8]
"""

# FUNCTION TO PERFORM THE OPERATION
def calc_max_per_k(arr, k):
    # Getting the length of the array & the max current element
    length = len(arr)
    max_curr = max(arr[:k])

    # looping over from k'th pos to the end of the array
    for i in range(length - k + 1):
        # setting the start and the end of the window frame
        start = i
        end = i + k - 1

        # temporary cariable to store the current maximum
        temp = max_curr

        # if the element at the start is the maximum, current max is recalculated
        if arr[start] == max_curr:
            max_curr = max(arr[start + 1 : end + 2])

        # if the next element to be considered in the window is larger, current max is set to that value
        elif end < (length - 1) and max_curr < arr[end + 1]:
            max_curr = arr[end + 1]

        # start of the moving window is set to the current max for the iteration
        arr[start] = temp

    # returning the values till start
    return arr[: start + 1]


# DRIVER CODE
print(calc_max_per_k([10, 5, 2, 7, 8, 7], 3))
print(calc_max_per_k([1, 91, 17, 46, 45, 36, 9], 3))
