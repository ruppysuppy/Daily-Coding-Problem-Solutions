"""
Problem:

You are given an integer list where each number represents the number of hops you can make.
Determine whether you can reach to the last index starting at index 0.

Example:

Input = [2, 0, 1, 0]
Output = true 

Input = [1, 1, 0, 1]
Output = false
"""

# FUNCTION TO PERFORM THE OPERATION
def can_reach_end(arr):
    # pos stores the current position
    pos = 0
    # length stores the length of the list
    length = len(arr)

    # looping till the pointer value is less than the length of the list
    while pos < length:
        # if we reach the last position, True is returned
        if pos == length - 1:
            return True
        # if the value in the list at the current position is 0, False is retuened (we cannot move any more)
        elif arr[pos] == 0:
            return False
        # getting the next position
        pos += arr[pos]

    # if we surpass the last index, False is returned
    return False


# DRIVER CODE
print(can_reach_end([2, 0, 1, 0]))
print(can_reach_end([1, 1, 0, 1]))
print(can_reach_end([1, 1, 10, 1]))
