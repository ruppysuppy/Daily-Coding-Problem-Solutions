"""
Problem:

Given a list of words, find all pairs of unique indices such that the concatenation of
the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return
[(0, 1), (1, 0), (2, 3)].
"""

from typing import List, Tuple


def is_palindrome(string: str) -> bool:
    return string == string[::-1]


def get_concatenated_palindrome_indices(
    string_list: List[str],
) -> List[Tuple[int, int]]:
    concatenated_palindrome_indices = []
    length = len(string_list)
    # generating concatenated palindrome indices
    for i in range(length):
        for j in range(i + 1, length):
            if is_palindrome(string_list[i] + string_list[j]):
                concatenated_palindrome_indices.append((i, j))
            if is_palindrome(string_list[j] + string_list[i]):
                concatenated_palindrome_indices.append((j, i))
    return concatenated_palindrome_indices


if __name__ == "__main__":
    print(get_concatenated_palindrome_indices(["code", "edoc", "da", "d"]))


"""
SPECS:

TIME COMPLEXITY: O(n x len(word))
SPACE COMPLEXITY: O(n ^ 2)
"""
