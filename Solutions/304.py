"""
Problem:

A knight is placed on a given square on an 8 x 8 chessboard. It is then moved randomly
several times, where each move is a standard knight move. If the knight jumps off the
board at any point, however, it is not allowed to jump back on.

After k moves, what is the probability that the knight remains on the board?
"""

from typing import List, Tuple


def get_moves(position: Tuple[int, int]) -> List[Tuple[int, int]]:
    i, j = position
    moves = [
        (i + 2, j + 1),
        (i + 2, j - 1),
        (i - 2, j + 1),
        (i - 2, j - 1),
        (i + 1, j + 2),
        (i + 1, j - 2),
        (i - 1, j + 2),
        (i - 1, j - 2),
    ]
    return moves


def get_knight_on_board_probability_helper(position: Tuple[int, int], k: int) -> int:
    i, j = position
    if not (0 <= i < 8) or not (0 <= j < 8):
        return 0
    if k == 0:
        return 1
    # generating total number of valid moves from current position
    moves = get_moves(position)
    accumulator = 0
    for pos in moves:
        accumulator += get_knight_on_board_probability_helper(pos, k - 1)
    return accumulator


def get_knight_on_board_probability(position: Tuple[int, int], k: int) -> float:
    # P(knight remains on board) = (number of positions on board / total positions)
    number_of_move_in_board = get_knight_on_board_probability_helper(position, k)
    return number_of_move_in_board / pow(8, k)


if __name__ == "__main__":
    print("{:.3f}".format(get_knight_on_board_probability((4, 4), 1)))
    print("{:.3f}".format(get_knight_on_board_probability((4, 4), 2)))
    print("{:.3f}".format(get_knight_on_board_probability((1, 1), 3)))


"""
SPECS:

TIME COMPLEXITY: O(8 ^ k)
SPACE COMPLEXITY: O(k)
"""
