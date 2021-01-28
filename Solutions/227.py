"""
Problem:

Boggle is a game played on a 4 x 4 grid of letters. The goal is to find as many words
as possible that can be formed by a sequence of adjacent letters in the grid, using
each cell at most once. Given a game board and a dictionary of valid words, implement a
Boggle solver.
"""

from typing import List, Set, Tuple

from DataStructures.Trie import Trie

Matrix = List[List[str]]
Position = Tuple[int, int]


def get_neighbours(position: Position) -> List[Position]:
    i, j = position
    neighbours = []
    all_neighbours = [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j + 1),
        (i + 1, j + 1),
        (i + 1, j),
        (i + 1, j - 1),
        (i, j - 1),
    ]
    for y, x in all_neighbours:
        if 0 <= x < 4 and 0 <= y < 4:
            neighbours.append((y, x))
    return neighbours


def get_words(
    matrix: Matrix, position: Position, trie: Trie, curr: str, result: Set[str]
) -> None:
    possibilities = trie.get_suggestions(curr)

    if not possibilities:
        return
    if len(possibilities) == 1 and list(possibilities)[0] == curr:
        result.add(curr)
        return

    for neighbour in get_neighbours(position):
        i, j = neighbour
        get_words(matrix, neighbour, trie, curr + matrix[i][j], result)
    return


def solve_Boggle(matrix: Matrix, dictionary: Set[str]) -> Set[str]:
    prefix_tree = Trie()
    prefix_tree.add_words(dictionary)
    result = set()
    # generating the resultant words
    for i in range(4):
        for j in range(4):
            if matrix[i][j] in prefix_tree.root.children:
                get_words(matrix, (i, j), prefix_tree, matrix[i][j], result)
    return result


if __name__ == "__main__":
    board = [
        ["A", "L", "B", "P"],
        ["C", "O", "E", "Y"],
        ["F", "C", "H", "O"],
        ["B", "A", "D", "A"],
    ]
    words_in_board = {"PECH", "COLA", "YO", "BAD"}
    words_not_in_board = {"FOR", "BULL"}
    dictionary = words_in_board | words_not_in_board

    print(dictionary)
    print(solve_Boggle(board, dictionary))


"""
SPECS:

TIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
[size of board is 4 x 4 (constant)]
"""
