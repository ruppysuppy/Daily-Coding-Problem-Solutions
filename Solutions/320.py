"""
Problem:

Given a string, find the length of the smallest window that contains every distinct
character. Characters may appear more than once in the window.

For example, given "jiujitsu", you should return 5, corresponding to the final five
letters.
"""

from sys import maxsize


def get_min_all_char_window(string: str) -> int:
    result = maxsize
    characters = set(string)
    length = len(string)
    curr_char = {}
    start, end = 0, len(characters)
    # initializing moving window
    for i in range(start, end):
        if string[i] not in curr_char:
            curr_char[string[i]] = 0
        curr_char[string[i]] += 1
    # check for all characters in the string is distinct
    if len(curr_char) == len(characters):
        result = len(curr_char)
    # updating moving window
    while end < length:
        if string[end] not in curr_char:
            curr_char[string[end]] = 0
        curr_char[string[end]] += 1
        # shortening window
        while curr_char[string[start]] > 1:
            curr_char[string[start]] -= 1
            start += 1
        # check if the window contains all characters
        if len(curr_char) == len(characters):
            result = min(result, end - start + 1)
        end += 1
    return result


if __name__ == "__main__":
    print(get_min_all_char_window("jiujitsu"))
    print(get_min_all_char_window("jiujiuuts"))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
