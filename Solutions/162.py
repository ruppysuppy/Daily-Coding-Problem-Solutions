"""
Problem:

Given a list of words, return the shortest unique prefix of each word. For example, given the list:

dog
cat
apple
apricot
fish

Return the list:

d
c
app
apr
f
"""

from typing import Dict, List, Optional


def get_unique_prefix_for_string(
    dictionary: Dict[str, int], string: str, string_list: List[str]
) -> Optional[str]:
    prefix = ""
    for char in string:
        prefix += char
        if prefix not in dictionary:
            return prefix
        # if a string with the current prefix exists, the prefix for the string is
        # updated
        prev_str_with_same_prefix = string_list[dictionary[prefix]]
        prev_prefix = prefix
        prev_str_index = dictionary[prefix]

        del dictionary[prefix]
        try:
            prev_prefix = prev_str_with_same_prefix[: len(prev_prefix) + 1]
        except:
            return
        dictionary[prev_prefix] = prev_str_index


def get_unique_prefix(string_list: List[str]) -> List[str]:
    dictionary = {}
    # generating the unique prefix
    for index, string in enumerate(string_list):
        prefix = get_unique_prefix_for_string(dictionary, string, string_list)
        if not prefix:
            raise ValueError("Unique Prefix Generation not possible")
        dictionary[prefix] = index
    return list(dictionary.keys())


if __name__ == "__main__":
    print(get_unique_prefix(["dog", "cat", "apple", "apricot", "fish"]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
