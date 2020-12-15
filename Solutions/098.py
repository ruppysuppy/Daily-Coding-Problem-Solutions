"""
Problem:

Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent"
cells are those horizontally or vertically neighboring. The same letter cell may not be
used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true,
exists(board, "ABCB") returns false.
"""

from typing import List, Set, Tuple

Board = List[List[str]]
Position = Tuple[int, int]


def get_neighbors(positons: Position, n: int, m: int) -> List[Position]:
    i, j = positons
    neighbors = [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]
    result = []
    for neighbor in neighbors:
        i, j = neighbor
        if i <= i < n and 0 <= j < m:
            result.append(neighbor)
    return result


def exists_helper(
    board: Board, position: Position, string: str, visited: Set[Position] = set()
) -> bool:
    if not string:
        return True
    # using backtracking to generate the result as every position can be used only once
    neighbors = get_neighbors(position, len(board), len(board[0]))
    for neighbor in neighbors:
        i, j = neighbor
        if (board[i][j] == string[0]) and (neighbor not in visited):
            visited.add((i, j))
            if exists_helper(board, (i, j), string[1:], visited):
                return True
            visited.remove((i, j))
    return False


def exists(board: Board, string: str) -> bool:
    if not string:
        return True

    for row_index, row in enumerate(board):
        for index, elem in enumerate(row):
            if string[0] == elem:
                if exists_helper(board, (row_index, index), string[1:], set()):
                    return True
    return False


if __name__ == "__main__":
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]

    print(exists(board, "ABCCED"))
    print(exists(board, "SEE"))
    print(exists(board, "ABCB"))


"""
SPECS:

TIME COMPLEXITY: O(n x m)
SPACE COMPLEXITY: O(n x m)
"""