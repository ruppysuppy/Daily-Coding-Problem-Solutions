"""
Problem:

Ghost is a two-person word game where players alternate appending letters to a word. The first person who spells out a word, or creates a prefix for which there is no possible continuation, loses. Here is a sample game:

Player 1: g
Player 2: h
Player 1: o
Player 2: s
Player 1: t [loses]
Given a dictionary of words, determine the letters the first player should start with, such that with optimal play they cannot lose.

For example, if the dictionary is ["cat", "calf", "dog", "bear"], the only winning start letter would be b.
"""


def get_winning_letters(words):
    # creating a map of starting characters to the words
    starting_char_freq = {}
    for word in words:
        if word[0] not in starting_char_freq:
            starting_char_freq[word[0]] = []
        starting_char_freq[word[0]].append(word)
    # getting the winning start characters
    # requirements: only 1 word starts with the character & its length is even
    winning_start_letters = set()
    for starting_char in starting_char_freq:
        if len(starting_char_freq[starting_char]) == 1:
            if len(starting_char_freq[starting_char][0]) % 2 == 0:
                winning_start_letters.add(starting_char)
    return winning_start_letters


# DRIVER CODE
print(get_winning_letters(["cat", "calf", "dog", "bear"]))
print(get_winning_letters(["cat", "something", "hi", "calf", "dog", "bear"]))
