"""
Problem:

On our special chessboard, two bishops attack each other if they share the same
diagonal. This includes bishops that have another bishop located between them, i.e.
bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard.
Write a function to count the number of pairs of bishops that attack each other. The
ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

(0, 0)
(1, 2)
(2, 2)
(4, 0)
The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]
You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and
4.
"""

from typing import List, Set, Tuple

Position = Tuple[int, int]


def generate_diagonals(position: Position, board_size: int) -> Set[Position]:
    row, col = position
    diagonals = set()
    # upper left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        diagonals.add((i, j))
    # lower left diagonal
    for i, j in zip(range(row + 1, board_size), range(col - 1, -1, -1)):
        diagonals.add((i, j))
    # upper right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, board_size)):
        diagonals.add((i, j))
    # lower right diagonal
    for i, j in zip(range(row + 1, board_size), range(col + 1, board_size)):
        diagonals.add((i, j))
    return diagonals


def get_number_of_attacking_bishops(board_size: int, positions: List[Position]) -> int:
    count = 0
    for index, position in enumerate(positions):
        diagonals = generate_diagonals(position, board_size)
        for position in positions[index:]:
            if position in diagonals:
                count += 1
    return count


if __name__ == "__main__":
    positions = [(0, 0), (1, 2), (2, 2), (4, 0)]
    print(get_number_of_attacking_bishops(5, positions))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n)
"""
