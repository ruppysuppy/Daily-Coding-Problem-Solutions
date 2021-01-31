"""
Problem:

Ghost is a two-person word game where players alternate appending letters to a word.
The first person who spells out a word, or creates a prefix for which there is no
possible continuation, loses. Here is a sample game:

Player 1: g
Player 2: h
Player 1: o
Player 2: s
Player 1: t [loses]
Given a dictionary of words, determine the letters the first player should start with,
such that with optimal play they cannot lose.

For example, if the dictionary is ["cat", "calf", "dog", "bear"], the only winning
start letter would be b.
"""


from typing import List, Set


def get_winning_letters(words: List[str]) -> Set[str]:
    # requirements for winning start letter:
    # - the length is even for all words starting with the character
    starting_char_freq = {}
    for word in words:
        if word[0] not in starting_char_freq:
            starting_char_freq[word[0]] = []
        starting_char_freq[word[0]].append(word)

    winning_start_letters = set()
    for starting_char in starting_char_freq:
        for word in starting_char_freq[starting_char]:
            if len(word) % 2 != 0:
                break
        else:
            winning_start_letters.add(starting_char)
    return winning_start_letters


if __name__ == "__main__":
    print(get_winning_letters(["cat", "calf", "dog", "bear"]))
    print(get_winning_letters(["something", "hi", "cat", "dog", "bear", "hola"]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
