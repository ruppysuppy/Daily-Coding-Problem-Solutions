"""
Problem:

The sequence [0, 1, ..., N] has been jumbled, and the only clue you have for its order
is an array representing whether each number is larger or smaller than the last. Given
this information, reconstruct an array that is consistent with it. For example, given
[None, +, +, -, +], you could return [1, 2, 3, 0, 4].
"""


from typing import List, Optional


def get_sequence(relative_arr: List[Optional[str]]) -> List[int]:
    length = len(relative_arr)
    larger_count = relative_arr.count("+")
    first_num = length - 1 - larger_count
    larger_num, smaller_num = first_num + 1, first_num - 1

    result = [first_num]
    for elem in relative_arr[1:]:
        if elem == "+":
            result.append(larger_num)
            larger_num += 1
        else:
            result.append(smaller_num)
            smaller_num -= 1
    return result


if __name__ == "__main__":
    print(get_sequence([None, "+", "+", "-", "+"]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
