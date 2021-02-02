"""
Problem:

You are given an N by N matrix of random letters and a dictionary of words. Find the
maximum number of words that can be packed on the board from the given dictionary.

A word is considered to be able to be packed on the board if:

It can be found in the dictionary
It can be constructed from untaken letters by other words found so far on the board
The letters are adjacent to each other (vertically and horizontally, not diagonally).
Each tile can be visited only once by any word.
For example, given the following dictionary:

{ 'eat', 'rain', 'in', 'rat' }
and matrix:

[['e', 'a', 'n'],
 ['t', 't', 'i'],
 ['a', 'r', 'a']]
Your function should return 3, since we can make the words 'eat', 'in', and 'rat'
without them touching each other. We could have alternatively made 'eat' and 'rain',
but that would be incorrect since that's only 2 words.
"""

from typing import List, Optional, Set, Tuple, Union


def get_neighbours(
    pos: Tuple[int, int], dim: Tuple[int, int], seen: Set[int]
) -> List[Tuple[int, int]]:
    n, m = dim
    i, j = pos
    positions = [
        (i - 1, j),
        (i + 1, j),
        (i, j - 1),
        (i, j + 1),
    ]
    valid_positions = []
    for position in positions:
        y, x = position
        if (0 <= y < n and 0 <= x < m) and (position not in seen):
            valid_positions.append(position)
    return valid_positions


def can_generate_word(
    matrix: List[List[str]],
    pos: Tuple[int, int],
    word: str,
    seen: Set[int],
    dim: Tuple[int, int],
) -> Union[bool, Optional[Set[int]]]:
    # check if the current word can be generated from the matrix
    if word == "":
        return True, seen
    neighbours = get_neighbours(pos, dim, seen)
    for neighbour in neighbours:
        i, j = neighbour
        if matrix[i][j] == word[0]:
            generated, seen_pos = can_generate_word(
                matrix, neighbour, word[1:], seen | set([neighbour]), dim
            )
            if generated:
                return generated, seen_pos
    return False, None


def get_power_set(words: List[str]) -> List[List[str]]:
    # generate the power set of the given list except the empty set
    num_of_words = len(words)
    accumulator = []
    pow_set_size = pow(2, num_of_words)

    for counter in range(pow_set_size):
        temp = []
        for j in range(num_of_words):
            if (counter & (1 << j)) > 0:
                temp.append(words[j])
        if temp:
            # adding only valid sets
            accumulator.append(temp)
    return accumulator


def get_max_packed_helper(matrix: List[List[str]], words: Set[str]) -> int:
    n, m = len(matrix), len(matrix[0])
    count = 0
    seen = set()

    for i in range(n):
        for j in range(m):
            char = matrix[i][j]
            for word in words:
                if word[0] == char:
                    # a match has been found, trying to generate the entire word from
                    # the first character in the matrix
                    generated, seen_temp = can_generate_word(
                        matrix, (i, j), word[1:], seen, (n, m)
                    )
                    if generated:
                        count += 1
                        seen = seen_temp
    return count


def get_max_packed(matrix: List[List[str]], words: Set[str]) -> int:
    words_list = get_power_set(list(words))
    max_words = 0
    for word_list in words_list:
        max_words = max(max_words, get_max_packed_helper(matrix, word_list))
    return max_words


if __name__ == "__main__":
    print(
        get_max_packed(
            [
                ["e", "a", "n"],
                ["t", "t", "i"],
                ["a", "r", "a"]
            ], {"eat", "rain", "in", "rat"},
        )
    )


"""
SPECS:

TIME COMPLEXITY: O(n x m x words x len(longest word))
SPACE COMPLEXITY: O(n x m)
"""
