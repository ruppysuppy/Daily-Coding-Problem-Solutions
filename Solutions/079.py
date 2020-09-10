"""
Problem:

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

Example:

[10, 5, 7] => true (since we can modify the 10 into a 1 to make the array non-decreasing)
[10, 5, 1]=> false (since we can't modify any one element to get a non-decreasing array)
"""

# FUNCTION TO PERFORM THE OPERATION
def check_1_modify_to_sorted(arr):
    # valstores the i'th element of the array during iteration
    # neg_count stores the number of elements with negative difference (next_elem - current_elem)
    val = arr[0]
    neg_count = 0

    # iterating the list from the 2nd element
    for elem in arr[1:]:
        # if the difference is negative (next_elem - current_elem), neg_count is incremented
        if (elem - val) < 0:
            neg_count += 1
            # if there is more than 1 element with negative difference, the list cannot be made ascending by modifying 1 element (False returned)
            if neg_count > 1:
                return False
        # val is updated for the next iteration
        val = elem

    # if the control reaches the end of the loop, True is returned
    return True


# DRIVER CODE
print(check_1_modify_to_sorted([10, 5, 7]))
print(check_1_modify_to_sorted([10, 5, 1]))
print(check_1_modify_to_sorted([1, 10, 5, 7]))
