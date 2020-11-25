"""
Problem:

Given a string s and an integer k, break up the string into multiple texts such that
each text has a length of k or less. You must break it up so that words don't break
across lines. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is
exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10,
you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No
string in the list has a length of more than 10.
"""

from typing import List, Optional


def break_string(string: str, k: int) -> Optional[List[str]]:
    word_list = string.split()
    result = []
    curr_len = 0
    curr_str = ""
    # generating the formatted text
    for word in word_list:
        current_word_length = len(word)
        if current_word_length > k:
            return None
        if curr_len == 0:
            # first iteration
            curr_len = current_word_length
            curr_str = word
        elif curr_len + current_word_length + 1 > k:
            # overflow condition
            result.append(curr_str)
            curr_str = word
            curr_len = current_word_length
        else:
            # normal addition to the string
            curr_len += current_word_length
            curr_str += " " + word
    result.append(curr_str)
    return result


if __name__ == "__main__":
    print(break_string("the quick brown fox jumps over the lazy dog", 10))
    print(break_string("the quick brown fox jumps over the lazy dog", 3))
    print(break_string("the quick brown fox jumps over the lazy dog tenletters", 10))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
