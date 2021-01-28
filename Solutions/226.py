"""
Problem:

You come across a dictionary of sorted words in a language you've never seen before.
Write a program that returns the correct order of letters in this language.

For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], you should return
['x', 'z', 'w', 'y'].
"""

from typing import Dict, List, Optional, Set


def update_letter_order(sorted_words: List[str], letters: Dict[str, Set[str]]) -> None:
    order = []
    new_words = {}
    prev_char = None

    for word in sorted_words:
        if word:
            char = word[0]
            if char != prev_char:
                order.append(char)
            if char not in new_words:
                new_words[char] = list()
            new_words[char].append(word[1:])
            prev_char = char

    for index, char in enumerate(order):
        letters[char] = letters[char] | set(order[index + 1 :])
    for char in new_words:
        update_letter_order(new_words[char], letters)


def find_path(
    letters: Dict[str, Set[str]], start: str, path: List[str], length: int
) -> Optional[List[str]]:
    if len(path) == length:
        return path
    if not letters[start]:
        return None

    for next_start in letters[start]:
        new_path = find_path(letters, next_start, path + [next_start], length)
        if new_path:
            return new_path


def get_letter_order(sorted_words: List[str]):
    letters = {}
    for word in sorted_words:
        for letter in word:
            if letter not in letters:
                letters[letter] = set()

    update_letter_order(sorted_words, letters)

    max_children = max([len(x) for x in letters.values()])
    potential_heads = [x for x in letters if len(letters[x]) == max_children]

    path = None
    for head in potential_heads:
        path = find_path(letters, head, path=[head], length=len(letters))
        if path:
            break
    return path


if __name__ == "__main__":
    print(get_letter_order(["xww", "wxyz", "wxyw", "ywx", "ywz"]))


"""
SPECS:

TIME COMPLEXITY: O(words x letters + words ^ 2 + letters ^ 2)
SPACE COMPLEXITY: O(words x letters)
"""
