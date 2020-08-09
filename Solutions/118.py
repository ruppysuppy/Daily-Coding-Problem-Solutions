"""
Problem:

Given a sorted list of integers, square the elements and give the output in sorted order.

Example:

Input = [-9, -2, 0, 2, 3]
Output = [0, 4, 4, 9, 81]
"""

# helper function to merge 2 sorted list into 1 sorted list
def merge_sorted_lists(arr1, arr2):
    # pointers to store the index of the current position in their respective arrays
    ptr1 = 0
    ptr2 = 0
    # lengths of the respective array
    length1 = len(arr1)
    length2 = len(arr2)
    # result stores the complete sorted array
    result = []

    # iterating till the end of one of the arrays
    while ptr1 < length1 and ptr2 < length2:
        # finding the smaller element of the 2 arrays' current position and adding it to the result
        if arr1[ptr1] < arr2[ptr2]:
            result.append(arr1[ptr1])
            ptr1 += 1

        else:
            result.append(arr2[ptr2])
            ptr2 += 1

    # extending the result by the left over part of the unfinished array
    result.extend(arr1[ptr1:])
    result.extend(arr2[ptr2:])

    return result


# FUNCTION TO PERFORM THE OPERATION
def sort_square(arr):
    # pos_start stores the starting index of the positive numbers
    pos_start = 0
    # length stores the length of the array
    length = len(arr)

    # looping over the array
    for i in range(length):
        # if the element is poitive, pos_start is updated and the control breaks out of the loop
        if arr[i] > 0:
            pos_start = i
            break
    # if all elements are negative, pos_start is set to the length of the array
    else:
        pos_start = length

    # generating the poitive and negative parts
    negative_part = [elem * elem for elem in arr[:pos_start][::-1]]
    positive_part = [elem * elem for elem in arr[pos_start:]]

    # returning the final sorted list
    return merge_sorted_lists(positive_part, negative_part)


# DRIVER CODE
print(sort_square([]))
print(sort_square([0]))
print(sort_square([-1, 1]))
print(sort_square([0, 2, 3]))
print(sort_square([-9, -2, 0]))
print(sort_square([-9, -2, 0, 2, 3]))
