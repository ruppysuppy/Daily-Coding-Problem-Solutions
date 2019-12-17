'''
Problem:

You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. 
Suppose it will rain and all spots between two walls get filled up.
Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

Example:

[2, 1, 2] => 1
[3, 0, 1, 3, 0, 5] => 8
'''

# FUNCTION TO PERFORM THE OPERATION
def water(arr):
    # Checking if there is enough walls to store water
    length = len(arr)
    if (length < 3):
        return 0
    
    # Variable to store the total amount of accumulated water
    total_water = 0

    # left and right store the current left and right positions in the array (moving to the middle from the ends)
    # left_max and right_max stores the maximum on the left and right of the current left and right positions respectively
    left = 0
    right = length - 1
    left_max = 0
    right_max = 0

    # iterating till the position pointers cross each other
    while left <= right:
        # if the element at the left position is less than the one on the right, left position marker is moved to the next position
        # if the value is larger than left_max, left_max is updated, else total_water is updated
        if arr[left] < arr[right]:
            if arr[left] > left_max:
                left_max = arr[left]
            else:
                total_water += left_max - arr[left]
            left += 1
        # if the element at the right position is less than the one on the left, left position marker is moved to the previous position
        # if the value is larger than right_max, right_max is updated, else total_water is updated
        else:
            if arr[right] > right_max:
                right_max = arr[right]
            else:
                total_water += right_max - arr[right]
            right -= 1

    return total_water

# DRIVER CODE
print(water([2, 1, 2]))
print(water([3, 0, 1, 3, 0, 5]))
print(water([5, 3, 5, 3, 4]))
print(water([5, 1, 1, 1, 0]))