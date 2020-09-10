"""
Problem:

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Your algorithm should run in O(n) complexity.

Example:

Input = [100, 4, 200, 1, 3, 2]
Output = 4 ([1, 2, 3, 4])
"""

# FUNCTION TO PERFORM THE OPERATION
def longest_consecutive_elements_sequence(arr):
    # creating a set from the passed list for fast searching
    # longest stores the length of the longest sequence
    val_set = set(arr)
    longest = 0

    # looping till val_set has some value
    while val_set:
        # getting a random element from val_set
        for i in val_set:
            elem = i
            break

        # removing the element from the set
        # creating length temp for checking the lenth of the sequence the element is a part of
        # creating the max and min limit of the sequence
        val_set.remove(elem)
        length_temp = 1
        max_lim = elem + 1
        min_lim = elem - 1

        # iterating till the max or min limit value is in the set
        while (max_lim in val_set) or (min_lim in val_set):
            # if the max limit is in the set, its removed and max limit and the length of the sequence updated
            if max_lim in val_set:
                length_temp += 1
                val_set.remove(max_lim)
                max_lim += 1

            # if the min limit is in the set, its removed and min limit and the length of the sequence updated
            if min_lim in val_set:
                length_temp += 1
                val_set.remove(min_lim)
                min_lim -= 1

        # if the length of the sequence exceeds the longest length, longest is updated
        if longest < length_temp:
            longest = length_temp

    # NOTE: This function runs in O(n) even though it has 3 loops (2 nested)
    return longest


# DRIVER CODE
print(longest_consecutive_elements_sequence([100, 4, 200, 1]))
print(longest_consecutive_elements_sequence([100, 4, 200, 1, 3]))
print(longest_consecutive_elements_sequence([100, 4, 200, 2, 3]))
print(longest_consecutive_elements_sequence([100, 4, 200, 1, 3, 2]))
print(longest_consecutive_elements_sequence([100, 4, 200, 1, 3, 2, 5]))
