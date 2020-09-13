"""
Problem:

A girl is walking along an apple orchard with a bag in each hand. She likes to pick
apples from each tree as she goes along, but is meticulous about not putting different
kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order,
determine the length of the longest portion of her path that consists of just two types
of apple trees.

For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve
types 1 and 3, with a length of four.
"""

from typing import List


def get_longest_path_length(apples: List[int]) -> int:
    curr_apples = {}
    max_path = 0
    start = 0
    curr_apples[apples[start]] = 1
    length = len(apples)
    # moving the pointer to the position where the apple is not the same as the 1st
    # apple in the array
    for i in range(1, length):
        if apples[i] in curr_apples:
            curr_apples[apples[i]] += 1
        else:
            mismatch = i
            break
    else:
        # only 1 type of apple present in the input
        return length
    curr_apples[apples[mismatch]] = 1
    # updating max_path to find the result
    for i in range(mismatch + 1, length):
        curr_apple = apples[i]
        if curr_apple not in curr_apples:
            max_path = max(max_path, i - start)
            while len(curr_apples) > 1:
                curr_apples[apples[start]] -= 1
                if not curr_apples[apples[start]]:
                    del curr_apples[apples[start]]
                start += 1
            curr_apples[curr_apple] = 1
        else:
            curr_apples[curr_apple] += 1
    max_path = max(max_path, length - start)
    return max_path


if __name__ == "__main__":
    print(get_longest_path_length([2, 1, 2, 3, 3, 1, 3, 5]))
    print(get_longest_path_length([2, 1, 2, 2, 2, 1, 2, 1]))
    print(get_longest_path_length([1, 2, 3, 4]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
