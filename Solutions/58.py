"""
Problem:

An sorted array of integers was rotated an unknown number of times.
Given such an array, find the index of the element in the array in faster than linear time. 
If the element doesn't exist in the array, return null.
You can assume all the integers in the array are unique.

Example:
[13, 18, 25, 2, 8, 10], 8 => 4 (the index of 8 in the array)
"""

# helper function to find the pivot position
def find_pivot(arr, start, stop, length):
    # if the start and the stop pointers cross each other, the arr is sorted with no pivot
    # NOTE: This works only if we have a sorted and rotated array
    if stop < start:
        return 0

    # finding the middle of the array
    mid = (start + stop) // 2

    # checking the corresponding condition to detect where the pivot is
    # if mid value is larger than mid-1, the pivot is at the mid
    if mid > 0 and arr[mid - 1] > arr[mid]:
        return mid
    # if the mid+1 value is smaller than the mid, the pivot is at the mid+1
    elif mid < length - 1 and arr[mid + 1] < arr[mid]:
        return mid + 1
    # if the 1st element under consideration is smaller than the mid, the pivot is on the right
    elif arr[start] < arr[mid]:
        return find_pivot(arr, mid + 1, stop, length)
    # if the last element under consideration is larger than the mid, the pivot is on the left
    elif arr[stop] > arr[mid]:
        return find_pivot(arr, start, mid - 1, length)


# helper function to carry out binary search
def bin_search(arr, low, high, key):
    # checking if the high and low pointers crossed each other
    if high < low:
        return -1

    # finding mid
    mid = (low + high) // 2

    # if the key is at mid, mid is returned
    if key == arr[mid]:
        return mid

    # if key is larger than value at mid, bin_search is called on the right of mid
    if key > arr[mid]:
        return bin_search(arr, (mid + 1), high, key)
    # else bin_search is called on the left of mid
    else:
        return bin_search(arr, low, (mid - 1), key)


# FUNCTION TO PERFORM THE OPERATION
def pivoted_bin_search(arr, length, element):
    # getting the pivot
    pivot = find_pivot(arr, 0, length - 1, length)

    # if the pivot is the searched element, pivot is returned
    if arr[pivot] == element:
        return pivot

    # if value at pivot is smaller than the element (value may exist), bin_search is called to the right of the pivot
    if arr[pivot] < element:
        temp = bin_search(arr, pivot + 1, length - 1, element)
        # if the value is found, the location is returned
        if temp != -1:
            return temp
        # if the element is not present at the right, bin_search is called on the left
        else:
            temp = bin_search(arr, 0, pivot - 1, element)
            # if the value is found, the location is returned, else None is returned
            if temp != -1:
                return temp
            return None
    # if the value cannot be in the array (smaller than the smallest element), None is returned
    else:
        return None


# DRIVER CODE
arr = [13, 18, 25, 2, 8, 10]
print(pivoted_bin_search(arr, len(arr), 8))
print(pivoted_bin_search(arr, len(arr), 10))
print(pivoted_bin_search(arr, len(arr), 15))
print(pivoted_bin_search(arr, len(arr), 2))
print(pivoted_bin_search(arr, len(arr), 8))
arr = [25, 2, 8, 10, 13, 18]
print(pivoted_bin_search(arr, len(arr), 8))
arr = [8, 10, 13, 18, 25, 2]
print(pivoted_bin_search(arr, len(arr), 8))
