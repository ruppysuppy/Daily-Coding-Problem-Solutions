'''
Problem:

Given a pivot x, and a list lst, partition the list into three parts.
* The first part contains all elements in lst that are less than x
* The second part contains all elements in lst that are equal to x
* The third part contains all elements in lst that are larger than x Ordering within a part can be arbitrary.

Example:

Input = [9, 12, 3, 5, 14, 10, 10], 10
Output = [9, 3, 5, 10, 10, 12, 14]
'''

# helper function to perform the computation
def separate_with_pivot(arr, i, j, x):
    # if the array is empty, no operation is performed
    if (not arr):
        return

    # looping till i and j pointers cross
    while (i < j):
        # if the left pointer has a value greater than or equal to x and right pointer has a value smaller than x
        # the values are swapped and pointers updated
        if (arr[i] >= x and arr[j] < x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        # else updating the pointers as per requirements
        else:
            if (arr[i] < x):
                i += 1
            if (arr[j] >= x):
                j -= 1

    # returning the position in the array containing a value greater than or equal to x
    if ((arr[i] < x) and (i+1 < len(arr))):
        return i + 1 
    else:
        return i

# FUNCTION TO PERFORM THE OPERATION
def pivot_list(arr, x):
    # getting the length of the array
    length = len(arr)

    # getting the mid position (all elements to the left of mid is less than x), pushing all values smaller than x to the left
    mid = separate_with_pivot(arr, 0, length-1, x)
    # pushing all values smaller than x+1 to the left (to get all the values equal to x clustered to the right of the smaller values)
    separate_with_pivot(arr, mid, length-1, x+1)

    return arr

# DRIVER CODE
print(pivot_list([9, 12, 3, 5, 14, 10, 10], 10))
print(pivot_list([9, 12, 3, 5, 14, 10, 10], 8))
print(pivot_list([9, 12, 3, 5, 11, 10, 10], 10))
print(pivot_list([9, 12, 14, 10, 10], 8))
print(pivot_list([3, 5], 8))
print(pivot_list([8, 8, 8], 8))
print(pivot_list([], 8))