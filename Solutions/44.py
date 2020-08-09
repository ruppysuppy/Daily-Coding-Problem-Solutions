"""
Problem:

We can determine how "out of order" an array A is by counting the number of inversions it has. 
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. 
That is, a smaller element appears after a larger element.
Given an array, count the number of inversions it has. Do this faster than O(N^2) time.
You may assume each element in the array is distinct.

Example:
[2, 4, 1, 3, 5] => 3 <(2, 1), (4, 1), and (4, 3)>
[5, 4, 3, 2, 1] => 10 <every distinct pair forms an inversion>
"""

# Helper's helper function (merge function to merge the segments broken up by the merge_sort function)
def merge(a_with_inv, b_with_inv):
    # Variables:
    # i: stores the current index of the left arr
    # j: stores the current index of the right arr
    # merged: final merged arr
    # a: left arr
    # b: right arr
    # a_inv: number of inversions in left arr
    # b_inv: number of inversions in right arr
    # inversions: total inversions till now
    i = 0
    j = 0
    merged = []
    a, a_inv = a_with_inv
    b, b_inv = b_with_inv
    inversions = a_inv + b_inv

    # Creating the merged arr till the elements on left or the right arr run out
    while i < len(a) and j < len(b):
        # Adding the smaller element to the merged arr and incrementing the corresponding index (i or j)
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            # if b[j] is larger, inversion has to be performed, so inversions is incremented
            inversions += len(a[i:])
            j += 1

    # Adding the elements of the array where the elements haven't been processed yet
    while i < len(a):
        merged.append(a[i])
        i += 1
    while j < len(b):
        merged.append(b[j])
        j += 1

    return merged, inversions


# Helper function (uses merge sort to calculate the number of inversions in O(nlog(n)))
def merge_sort(arr):
    # Getting the length of the arr
    length = len(arr)

    # if the array has 0 or 1 element, no inversion is possible
    if length in (0, 1):
        return arr, 0

    # Getting the mid
    mid = length // 2
    # Performing merge_sort on the broken arr (from the mid)
    merged_array, inversions = merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

    return merged_array, inversions


# FUNCTION TO PERFORM THE OPERATION
def count_inversions(arr):
    # Calling merge_sort on the arr to get the sorted arr and inversions
    _sorted_arr, inversions = merge_sort(arr)
    return inversions


# DRIVER CODE
print(count_inversions([1, 2, 3, 4, 5]))
print(count_inversions([2, 1, 3, 4, 5]))
print(count_inversions([2, 4, 1, 3, 5]))
print(count_inversions([2, 6, 1, 3, 7]))
print(count_inversions([5, 4, 3, 2, 1]))
