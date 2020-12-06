"""
Problem:

Given a mapping of digits to letters (as in a phone number), and a digit string, return
all possible letters the number could represent. You can assume each valid number in
the mapping is a single digit.

For example if {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], } then "23" should return
['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'].
"""

from typing import Dict, List


def get_mappings(
    digit_to_character_map: Dict[str, str], string: str, result: List[str] = []
) -> List[str]:
    if not string:
        return result
    if not result:
        for elem in digit_to_character_map[string[0]]:
            result.append(elem)
        return get_mappings(digit_to_character_map, string[1:], result)
    # generating the mappings
    temp = []
    for part in result:
        for elem in digit_to_character_map[string[0]]:
            temp.append(part + elem)
    result[:] = temp
    return get_mappings(digit_to_character_map, string[1:], result)


if __name__ == "__main__":
    print(get_mappings({"2": ["a", "b", "c"], "3": ["d", "e", "f"]}, "23", []))
    print(get_mappings({"2": ["a", "b", "c"], "3": ["d", "e", "f"]}, "32", []))
    print(get_mappings({"2": ["a", "b", "c"], "3": ["d", "e", "f"]}, "222", []))


"""
SPECS:

TIME COMPLEXITY: O(n ^ m)
SPACE COMPLEXITY: O(n ^ m)
[n = string length, m = no of characters in map]
"""
