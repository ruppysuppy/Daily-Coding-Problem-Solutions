"""
Problem:

Given a string and a set of delimiters, reverse the words in the string while
maintaining the relative order of the delimiters. For example, given
"hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases: "hello/world:here/",
"hello//world:here"
"""

from typing import Set


def rev_words(string: str, delimiters: Set[str]) -> str:
    if len(string) == 0:
        return string

    words = []
    delims = []
    flag_beg = string[0] in delimiters
    flag_delim = False
    curr_str = ""
    # generating the words and delimiters
    for char in string:
        if char in delimiters:
            if flag_delim:
                curr_str += char
            else:
                if curr_str:
                    words.append(curr_str)
                curr_str = char
                flag_delim = True
        else:
            if flag_delim:
                flag_delim = False
                delims.append(curr_str)
                curr_str = char
            else:
                curr_str += char
    # check if last character is a delimiter
    if flag_delim:
        delims.append(curr_str)
    else:
        words.append(curr_str)

    words = words[::-1]
    words.append("")
    delims.append("")
    len_words = len(words)
    len_delims = len(delims)
    i, j = 0, 0
    reversed_string = ""
    # generating the reversed string
    if flag_beg:
        j = 1
        reversed_string += delims[0]
    while i < len_words or j < len_delims:
        try:
            reversed_string += words[i]
            reversed_string += delims[j]
            i += 1
            j += 1
        except IndexError:
            break
    return reversed_string


if __name__ == "__main__":
    print(rev_words("hello/world:here", {":", "/"}))
    print(rev_words("here/world:hello", {":", "/"}))
    print(rev_words("hello/world:here/", {":", "/"}))
    print(rev_words("hello//world:here", {":", "/"}))
    print(rev_words("hello", {":", "/"}))
    print(rev_words("//:", {":", "/"}))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
