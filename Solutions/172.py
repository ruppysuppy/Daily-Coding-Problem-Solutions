"""
Problem:

Given a string s and a list of words words, where each word is the same length, find
all starting indices of substrings in s that is a concatenation of every word in words
exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return [0, 13],
since "dogcat" starts at index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there are no
substrings composed of "dog" and "cat" in s.

The order of the indices does not matter.
"""

from itertools import permutations as generate_permutations
from re import finditer
from typing import Iterable, List


def concat_iteratable(iterateable: Iterable[str]) -> str:
    concated_value = ""
    for elem in iterateable:
        concated_value += elem
    return concated_value


def get_permutation_match_indices(s: str, words: List[str]) -> List[int]:
    permutations = [
        concat_iteratable(permutation)
        for permutation in list(generate_permutations(words))
    ]
    indices = []
    for permutation in permutations:
        indices.extend([match.start() for match in finditer(permutation, s)])
    return indices


if __name__ == "__main__":
    print(get_permutation_match_indices("barfoobazbitbyte", ["dog", "cat"]))
    print(get_permutation_match_indices("dogcatcatcodecatdog", ["cat", "dog"]))
    print(get_permutation_match_indices("dogcatcatcodecatdogcat", ["cat", "dog"]))


"""
SPECS:

TIME COMPLEXITY: O(2 ^ m + 2 ^ n)
SPACE COMPLEXITY: O(n)
[n = number of characters in input string
 m = number of match words]
"""
