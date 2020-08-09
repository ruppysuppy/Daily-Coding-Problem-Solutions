"""
Problem:

There are N couples sitting in a row of length 2 * N.
They are currently ordered randomly, but would like to rearrange themselves so that each couple's partners can sit side by side.
What is the minimum number of swaps necessary for this to happen?
"""

# The range of the swaps is [0, ceil(N / 2)]


def get_desired_index(curr_index):
    if curr_index % 2 == 0:
        return curr_index + 1
    return curr_index - 1


def couple_pairing(array):
    if array == None or (len(array) % 2) != 0:
        return 0
    # key: previous found element, value: desired index for partner
    hash_table = {}
    n_swaps = 0
    for index, element in enumerate(array):
        # if element in hash, then swap with the index value in hash
        if element in hash_table:
            desired_index = hash_table[element]
            value_at_desired_index = array[desired_index]
            # avoid an extra swap for itself, for example if array was [1,1]
            if value_at_desired_index != element:
                array[index], array[desired_index] = array[desired_index], array[index]
                n_swaps += 1
                hash_table[value_at_desired_index] = get_desired_index(index)
        else:
            hash_table[element] = get_desired_index(index)
    return n_swaps


# DRIVER CODE
print(couple_pairing([2, 1, 2, 3, 1, 3]))
print(couple_pairing([3, 2, 1, 1, 2, 3]))
