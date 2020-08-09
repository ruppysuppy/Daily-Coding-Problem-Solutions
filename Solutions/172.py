"""
Problem:

Given a string s and a list of words words, where each word is the same length, find all starting indices of substrings in s that is a concatenation of every word in words exactly once.
The order of the indices does not matter.

Example:
s = "dogcatcatcodecatdog"
words = ["cat", "dog"]
Output = [0, 13] (since "dogcat" starts at index 0 and "catdog" starts at index 13)

s = "barfoobazbitbyte"
words = ["dog", "cat"]
Output = [] (since there are no substrings composed of "dog" and "cat" in s)
"""

# importing permutation (generating all possible permutations)
from itertools import permutations

# importing regex function
from re import finditer

# FUNCTION TO PERFORM THE OPERATION
def get_indices(s, words):
    # getting all permutations
    permutation_list = [x + y for (x, y) in list(permutations(words))]
    # res list to store the results
    res = []

    # checking the occurance of every permutation using regex
    for permutation in permutation_list:
        res.extend([match.start() for match in finditer(permutation, s)])

    # sorting the result and returning it
    res.sort()
    return res


# DRIVER CODE
print(get_indices("barfoobazbitbyte", ["dog", "cat"]))
print(get_indices("dogcatcatcodecatdog", ["cat", "dog"]))
print(get_indices("dogcatcatcodecatdogcat", ["cat", "dog"]))
