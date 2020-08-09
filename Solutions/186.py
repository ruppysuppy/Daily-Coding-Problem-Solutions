"""
Problem:

You are given an array of positive integers. 
Divide the array into two subsets such that the difference between the sum of the subsets is as small as possible.

Example:

Input = [5, 10, 15, 20, 25]
Output = {10, 25}, {5, 15, 20} (which has a difference of 5, which is the smallest possible difference)
"""

# FUNCTION TO PERFORM THE OPERATION
def smallest_difference_sets(arr, set1=[], set2=[]):
    # if all the elements of the array has been considered, the sets are returned
    if not arr:
        return set1, set2

    # the last element of the array is selected
    temp = arr.pop()

    # generating the 2 sets for each permutation (adding the last element to set1 or set2)
    temp1_1, temp2_1 = smallest_difference_sets(list(arr), set1 + [temp], list(set2))
    temp1_2, temp2_2 = smallest_difference_sets(list(arr), list(set1), set2 + [temp])

    # getting the difference in each case
    diff1 = abs(sum(temp1_1) - sum(temp2_1))
    diff2 = abs(sum(temp1_2) - sum(temp2_2))

    # returning the sets where the difference is minimum
    if diff1 < diff2:
        return temp1_1, temp2_1
    else:
        return temp1_2, temp2_2


# DRIVER CODE
print(smallest_difference_sets([5, 10, 15, 20, 25], [], []))
print(smallest_difference_sets([5, 10, 15, 20], [], []))
print(smallest_difference_sets([500, 10, 15, 20, 25], [], []))
