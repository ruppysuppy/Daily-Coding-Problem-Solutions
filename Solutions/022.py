"""
Problem:

Given a dictionary of words and a string made up of those words (no spaces), return the
original sentence in a list. If there is more than one possible reconstruction, return
any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string
"thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string
"bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or
['bedbath', 'and', 'beyond'].
"""

from typing import List


def get_words_in_string(word_list: List[str], string: str) -> List[str]:
    # function to get the words present in the input string
    word_set = set()
    buffer = ""
    words_found = []
    # populating the set with the words for O(1) access
    for word in word_list:
        word_set.add(word)
    # searching for words in the string
    for char in string:
        buffer += char
        if buffer in word_set:
            words_found.append(buffer)
            buffer = ""

    if len(words_found) == 0:
        return None
    return words_found


if __name__ == "__main__":
    print(get_words_in_string(["quick", "brown", "the", "fox"], "thequickbrownfox"))
    print(
        get_words_in_string(
            ["bed", "bath", "bedbath", "and", "beyond"], "bedbathandbeyond"
        )
    )
    print(get_words_in_string(["quick", "brown", "the", "fox"], "bedbathandbeyond"))


"""
SPECS:

TIME COMPLEXITY: O(characters_in_input_string)
SPACE COMPLEXITY: O(words)
"""
