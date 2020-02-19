'''
Problem:

Given a number represented by a list of digits, find the next greater permutation of a number, in terms of lexicographic ordering. 
If there is not greater permutation possible, return the permutation with the lowest value/ordering.
Can you perform the operation without allocating extra memory (disregarding the input memory)?

Example:
Input = [1,2,3]
Output = [1,3,2]

Input = [1,3,2]
Output = [2,1,3]

Input = [3,2,1]
Output = [1,2,3]
'''

# FUNCTION TO PERFORM THE OPERATION
def get_next(arr):
    # getting the length of arr
    length = len(arr)

    # if arr has 0 or 1 elements, its returned
    if (length < 2):
        return arr

    # looping arr from the end to the beginning
    for index in range(length - 1, -1, -1):
        # finding the last element arranged in ascending order
        if (index > 0 and arr[index - 1] < arr[index]):
            break

    # if index is 0 (arr is sorted in descending order), arr is reversed
    if (index == 0):
        arr.reverse()

    else:
        # finding the next permutation
        # looping over arr from the end to the index
        for k in range(length - 1, index - 1, -1):
            # getting the element to swap
            if (arr[k] > arr[index - 1]):
                arr[k], arr[index - 1]  = arr[index - 1], arr[k]
                break

        # arranging the other elements in proper order
        sub_array = arr[index:]
        sub_array.reverse()
        arr[index:] = sub_array

    return arr

# DRIVER CODE
print(get_next([1,2,3]))
print(get_next([1,3,2]))
print(get_next([2,1,3]))
print(get_next([2,3,1]))
print(get_next([3,1,2]))
print(get_next([3,2,1]))