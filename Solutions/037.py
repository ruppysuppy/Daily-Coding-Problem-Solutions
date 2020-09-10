"""
Problem:

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
You may also use a list or array to represent a set.

Example:
{1, 2, 3} => {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
"""

# FUNCTION TO PERFORM THE OPERATION
def power_set_calc(arr):
    # power_set list is used to store the subsets (initialized with an empty array as an empty array is also a subset)
    power_set = [[]]

    # Adding the current element in the input array to each of the element of the power_set to generate the list of all subsets
    for i in arr:
        for index in range(len(power_set)):
            # temp stores a copy of the element under consideration
            temp = list(power_set[index])
            # the current array element is added to temp
            temp.append(i)
            # the generated temp is added to the power_set
            power_set.append(temp)

    return power_set


# DRIVER CODE
print(power_set_calc([1, 2, 3]))
