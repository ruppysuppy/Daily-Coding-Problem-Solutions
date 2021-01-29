"""
Problem:

There are N couples sitting in a row of length 2 * N. They are currently ordered
randomly, but would like to rearrange themselves so that each couple's partners can sit
side by side. What is the minimum number of swaps necessary for this to happen?
"""

# The range of the swaps is [0, ceil(N / 2)]


from typing import List


def get_desired_index(curr_index: int) -> int:
    if curr_index % 2 == 0:
        return curr_index + 1
    return curr_index - 1


def couple_pairing(array: List[int]) -> int:
    if array == None or (len(array) % 2) != 0:
        return 0
    hash_table = {}
    n_swaps = 0

    for index, element in enumerate(array):
        if element in hash_table:
            desired_index = hash_table[element]
            value_at_desired_index = array[desired_index]
            if value_at_desired_index != element:
                array[index], array[desired_index] = array[desired_index], array[index]
                n_swaps += 1
                hash_table[value_at_desired_index] = get_desired_index(index)
            continue
        hash_table[element] = get_desired_index(index)
    return n_swaps


if __name__ == "__main__":
    print(couple_pairing([2, 1, 2, 3, 1, 3]))
    print(couple_pairing([3, 2, 1, 1, 2, 3]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
