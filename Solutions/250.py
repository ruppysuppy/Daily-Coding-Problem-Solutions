"""
Problem:

A cryptarithmetic puzzle is a mathematical game where the digits of some numbers are
represented by letters. Each letter represents a unique digit.

For example, a puzzle of the form:

  SEND
+ MORE
--------
 MONEY
may have the solution:

{'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O': 0, 'R': 8, 'Y': 2}

Given a three-word puzzle like the one above, create an algorithm that finds a solution
"""


from typing import Dict, List, Set


def get_num_from_string(char_map: Dict[str, int], string: str) -> int:
    mantissa = 10
    total = 0
    for char in string[::-1]:
        total += char_map[char] * mantissa
        mantissa *= 10
    return total


def is_valid_map(exp1: str, exp2: str, res: str, char_map: Dict[str, int]) -> bool:
    num1 = get_num_from_string(char_map, exp1)
    num2 = get_num_from_string(char_map, exp2)
    num3 = get_num_from_string(char_map, res)
    return num1 + num2 == num3


def get_valid_char_map(
    exp1: str, exp2: str, res: str, char_maps: List[Dict[str, int]]
) -> Dict[str, int]:
    for char_map in char_maps:
        if is_valid_map(exp1, exp2, res, char_map):
            return char_map


def assign_letters(
    chars_left: Set[str],
    nums_left: Set[int],
    restrictions: Dict[str, Set[int]],
    char_map: Dict[str, int] = {},
) -> List[Dict[str, int]]:
    # function to assign digits to the characters
    # brute force approach: all valid (doesn't contradict restictions) combinations
    #       are generated
    if not chars_left:
        return [char_map]
    curr_char = list(chars_left)[0]
    char_maps = []
    for num in nums_left:
        if num in restrictions[curr_char]:
            continue
        char_map_cp = char_map.copy()
        char_map_cp[curr_char] = num
        child_char_maps = assign_letters(
            chars_left - set([curr_char]),
            nums_left - set([num]),
            restrictions,
            char_map_cp,
        )
        char_maps.extend(child_char_maps)
    return char_maps


def decode(exp1: str, exp2: str, res: str) -> Dict[str, int]:
    characters = set(exp1) | set(exp2) | set(res)
    if len(characters) > 10:
        raise ValueError("Number of digits cannot be more than 10")

    nums = set(range(0, 10))
    restrictions = {}
    for char in characters:
        restrictions[char] = set()
    for word in [exp1, exp2, res]:
        restrictions[word[0]].add(0)
    char_maps = assign_letters(characters, nums, restrictions)
    return get_valid_char_map(exp1, exp2, res, char_maps)


if __name__ == "__main__":
    print(decode("SEND", "MORE", "MONEY"))


"""
SPECS:

TIME COMPLEXITY: O(2 ^ n)
SPACE COMPLEXITY: O(n)
[n = number of unique characters]
"""
