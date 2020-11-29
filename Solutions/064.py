"""
Problem:

A knight's tour is a sequence of moves by a knight on a chessboard such that all
squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N
chessboard.
"""

from typing import List, Tuple

Board = List[List[int]]


def get_valid_moves(position: Tuple[int, int], n: int) -> Tuple[int, int]:
    y, x = position
    positions = [
        (y + 1, x + 2),
        (y - 1, x + 2),
        (y + 1, x - 2),
        (y - 1, x - 2),
        (y + 2, x + 1),
        (y + 2, x - 1),
        (y - 2, x + 1),
        (y - 2, x - 1),
    ]
    valid_moves = [
        (y_test, x_test)
        for (y_test, x_test) in positions
        if 0 <= y_test < n and 0 <= x_test < n
    ]
    return valid_moves


def is_board_complete(board: Board) -> bool:
    for row in board:
        for elem in row:
            if elem == 0:
                return False
    return True


def solver_helper(board: Board, position: Tuple[int, int], count: int) -> int:
    if is_board_complete(board):
        count += 1
        return count
    for move in get_valid_moves(position, len(board)):
        y, x = move
        if board[y][x] == 0:
            board[y][x] = 1
            count += solver_helper(board, move, 0)
            board[y][x] = 0
    return count


def solve(n: int) -> int:
    board = [[0 for i in range(n)] for j in range(n)]
    board[0][0] = 1
    count = solver_helper(board, (0, 0), 0)
    return count


if __name__ == "__main__":
    print(solve(1))
    print(solve(2))
    print(solve(3))
    print(solve(4))
    print(solve(5))


"""
SPECS:

TIME COMPLEXITY: O(8 ^ (n ^ 2))
SPACE COMPLEXITY: O(n ^ 2)
"""
