"""
Problem:

Write an algorithm to justify text. Given a sequence of words and an integer line
length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should
be at least one space between each word. Pad extra spaces when necessary so that each
line has exactly length k. Spaces should be distributed as equally as possible, with
the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with
spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you
should return the following:

["the quick brown", # 1 extra space on the left "fox jumps over", # 2 extra spaces
distributed evenly "the lazy dog" # 4 extra spaces distributed evenly]
"""

from typing import List


def add_word_handler(
    result: List[str], temp: List[str], curr_string_length: int, k: int
) -> None:
    # helper function to handle adding a new word to the result
    extra_spaces = k - curr_string_length
    words_in_current_line = len(temp)
    if words_in_current_line == 1:
        # only 1 word is present, extra padding is added to the right
        word = temp.pop()
        result.append(word + " " * extra_spaces)
    elif extra_spaces % (words_in_current_line - 1) == 0:
        # space can be equally distributed
        full_string = (" " * (extra_spaces // (words_in_current_line - 1) + 1)).join(
            temp
        )
        result.append(full_string)
    else:
        # the space cannot be equally distributed
        # extra spaces are added betweens the words, starting from the left
        extra_uneven_spaces = extra_spaces % (words_in_current_line - 1)
        regular = extra_spaces // (words_in_current_line - 1) + 1
        temp_str = ""
        for i in temp:
            temp_str += i + " " * regular
            if extra_uneven_spaces:
                temp_str += " "
                extra_uneven_spaces -= 1
        result.append(temp_str.rstrip())


def justify_text(word_list: List[str], k: int) -> List[str]:
    result = []
    temp = []
    curr_string_length = 0
    # iterating through the given words
    for word in word_list:
        curr_word_length = len(word)
        if temp == []:
            # no word added to the current string
            temp.append(word)
            curr_string_length = curr_word_length
        elif curr_word_length + curr_string_length + 1 <= k:
            # adding the current word doesn't cause overflow
            temp.append(word)
            curr_string_length += curr_word_length + 1
        else:
            # adding the current word does cause overflow
            add_word_handler(result, temp, curr_string_length, k)
            # updating temp and length (only in case of overflow)
            temp = [word]
            curr_string_length = len(word)
    if temp != []:
        # if the last line caused an overflow
        add_word_handler(result, temp, curr_string_length, k)
    return result


if __name__ == "__main__":
    for string in justify_text(
        ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16
    ):
        print("'" + string + "'")

    for string in justify_text(["done"], 16):
        print("'" + string + "'")

    # NOTE: Using the "'"s is not important, used it to denote the start and end of the
    # string (helpful in case of 1 word in 1 line)


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
