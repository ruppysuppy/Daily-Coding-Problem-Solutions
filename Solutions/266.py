"""
Problem:

A step word is formed by taking a given word, adding a letter, and anagramming the
result. For example, starting with the word "APPLE", you can add an "A" and anagram
to get "APPEAL".

Given a dictionary of words and an input word, create a function that returns all valid
step words.
"""

from typing import Dict, List


def get_character_count(string: str) -> Dict[str, int]:
    freq = {}
    for char in string:
        if char not in freq:
            freq[char] = 0
        freq[char] += 1
    return freq


def is_step_word(word1: str, word2: str) -> bool:
    freq1 = get_character_count(word1)
    freq2 = get_character_count(word2)
    for char in freq1:
        if char in freq2:
            freq2[char] -= freq1[char]
            if freq2[char] == 0:
                del freq2[char]
        else:
            return False
    # checking if word2 is a step word of word1
    if len(freq2) == 1:
        [char] = freq2.keys()
        return freq2[char] == 1
    return False


def get_step_words(word: str, dictionary: List[str]) -> List[str]:
    step_words = []
    for test_word in dictionary:
        if is_step_word(word, test_word):
            step_words.append(test_word)
    return step_words


if __name__ == "__main__":
    print(get_step_words("APPLE", ["APPEAL"]))
    print(get_step_words("APPLE", ["APPEAL", "APPLICT"]))
    print(get_step_words("APPLE", ["APPEAL", "APPLICT", "APPLES"]))


"""
SPECS:

TIME COMPLEXITY: O(n.words)
SPACE COMPLEXITY: O(n)
[n = length of the longest word]
"""
