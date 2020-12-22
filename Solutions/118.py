"""
Problem:

Given a sorted list of integers, square the elements and give the output in sorted
order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""

from typing import List

Array = List[int]


def merge_sorted_lists(arr1: Array, arr2: Array) -> Array:
    ptr1, length1 = 0, len(arr1)
    ptr2, length2 = 0, len(arr2)
    merged_sorted_array = []
    # generating merged sorted list
    while ptr1 < length1 and ptr2 < length2:
        if arr1[ptr1] < arr2[ptr2]:
            merged_sorted_array.append(arr1[ptr1])
            ptr1 += 1
        else:
            merged_sorted_array.append(arr2[ptr2])
            ptr2 += 1
    merged_sorted_array.extend(arr1[ptr1:])
    merged_sorted_array.extend(arr2[ptr2:])
    return merged_sorted_array


def sort_squared_elements(arr: Array) -> Array:
    last_negative_position = 0
    length = len(arr)
    for i in range(length):
        if arr[i] > 0:
            last_negative_position = i
            break
    else:
        last_negative_position = length

    negative_part = [elem * elem for elem in arr[:last_negative_position]][::-1]
    positive_part = [elem * elem for elem in arr[last_negative_position:]]
    return merge_sorted_lists(positive_part, negative_part)


if __name__ == "__main__":
    print(sort_squared_elements([]))
    print(sort_squared_elements([0]))
    print(sort_squared_elements([-1, 1]))
    print(sort_squared_elements([0, 2, 3]))
    print(sort_squared_elements([-9, -2, 0]))
    print(sort_squared_elements([-9, -2, 0, 2, 3]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
