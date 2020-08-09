"""
Problem:

Write a function that rotates a list by k elements. 
Try solving this without creating a copy of the list. How many swap or move operations do you need?

Example:

Input = [1, 2, 3, 4, 5, 6]
Output = [3, 4, 5, 6, 1, 2]
"""

# FUNCTION TO PERFORM THE OPERATION
def rotate_list(List, k):
    # getting the length of the list
    length = len(List)
    # getting the number of necessary rotations (needed for optimizing the function if k >> length)
    k = k % length

    # rotating items the necessary times
    for _ in range(k):
        temp = List.pop(0)
        List.append(temp)

    # returning the list
    return List


# DRIVER CODE
print(rotate_list([1, 2, 3, 4, 5, 6], 0))
print(rotate_list([1, 2, 3, 4, 5, 6], 2))
print(rotate_list([1, 2, 3, 4, 5, 6], 4))
print(rotate_list([1, 2, 3, 4, 5, 6], 6))
print(rotate_list([1, 2, 3, 4, 5, 6], 10))
print(rotate_list([1, 2, 3, 4, 5, 6], 1000000000))
