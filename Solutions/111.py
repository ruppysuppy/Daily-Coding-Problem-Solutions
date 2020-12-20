"""
Problem:

Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""

from typing import Dict, List


def get_char_frequency(string: str) -> Dict[str, int]:
    freq = {}
    for char in string:
        if char not in freq:
            freq[char] = 0
        freq[char] += 1
    return freq


def get_word_start_loc(word: str, string: str) -> List[int]:
    word_len = len(word)
    str_len = len(string)
    char_needed_master = get_char_frequency(word)
    char_needed = dict(char_needed_master)
    curr = 0
    starting_indices = []
    # if the word is longer than the string, no anagram is possible
    if (word_len > str_len) or (word_len == 0):
        return []
    # generating the starting indices
    while curr < str_len:
        for i in range(curr, str_len):
            if string[i] not in char_needed:
                curr = i
                char_needed = dict(char_needed_master)
                break
            elif string[i] in char_needed:
                char_needed[string[i]] -= 1
                if char_needed[string[i]] == 0:
                    del char_needed[string[i]]
                    if char_needed == {}:
                        starting_indices.append(curr)
                        curr = i - 1
                        char_needed = dict(char_needed_master)
                        break
        curr += 1
    return starting_indices


if __name__ == "__main__":
    print(get_word_start_loc("ab", "abxaba"))
    print(get_word_start_loc("tac", "cataract"))


"""
SPECS:

TIME COMPLEXITY: O(len(word) x len(string))
SPACE COMPLEXITY: O(len(word))
"""
