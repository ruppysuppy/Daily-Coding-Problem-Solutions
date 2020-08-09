"""
Problem:

Given an integer, find the next permutation of it in absolute order. 

Example:

Input = 48975
Output = 49578
"""

# function used in problem 95 (used as a helper function in this problem)
def get_next_helper(arr):
    # getting the length of arr
    length = len(arr)

    # if arr has 0 or 1 elements, its returned
    if length < 2:
        return arr

    # looping arr from the end to the beginning
    for index in range(length - 1, -1, -1):
        # finding the last element arranged in ascending order
        if index > 0 and arr[index - 1] < arr[index]:
            break

    # if index is 0 (arr is sorted in descending order), arr is reversed
    if index == 0:
        arr.reverse()

    else:
        # finding the next permutation
        # looping over arr from the end to the index
        for k in range(length - 1, index - 1, -1):
            # getting the element to swap
            if arr[k] > arr[index - 1]:
                arr[k], arr[index - 1] = arr[index - 1], arr[k]
                break

        # arranging the other elements in proper order
        sub_array = arr[index:]
        sub_array.reverse()
        arr[index:] = sub_array

    return arr


# FUNCTION TO PERFORM THE OPERATION
def get_next(num):
    return int("".join(get_next_helper(list(str(num)))))


# DRIVER CODE
print(get_next(48975))
