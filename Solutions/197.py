"""
Problem:

Given an array and a number `k` that's smaller than the length of the array, rotate the array to the right `k` elements in-place.
"""

# FUNCTION TO PERFORM THE OPERATION
def rotate_right(arr, k):
    # getting the length of the array
    length = len(arr)

    # checking if the rotation has to be performed
    if k != 0:
        # storing the part to be shifted to the front in cache
        cache = arr[-k:]

        # shifting the necessary front part to the end
        for i in range(length - k - 1, -1, -1):
            arr[k + i] = arr[i]

        # adding the end (in cache) to the front
        arr[:k] = cache

    return arr


# DRIVER CODE
print(rotate_right([(i + 1) for i in range(5)], 3))
print(rotate_right([(i + 1) for i in range(5)], 2))
print(rotate_right([(i + 1) for i in range(5)], 1))
