"""
Problem:

Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The
objective is to fill the grid with the constraint that every row, column, and box
(3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.
"""

from typing import List, Optional, Tuple

Board = List[List[int]]
Position = Tuple[int, int]


def print_board(board: Board) -> None:
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if board[i][j] != 0:
                print(board[i][j], end=" ")
            else:
                print(".", end=" ")
        print()


def find_empty_position(board: Board) -> Optional[Position]:
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


def check_conflict(board: Board, position: Position, num: int) -> bool:
    y, x = position
    # row check
    for i in range(len(board[0])):
        if board[y][i] == num:
            return False
    # column check
    for i in range(len(board)):
        if board[i][x] == num:
            return False
    # sub-section check
    sec_row = y // 3
    sec_col = x // 3
    for i in range((sec_row * 3), (sec_row * 3) + 3):
        for j in range((sec_col * 3), (sec_col * 3) + 3):
            if board[i][j] == num:
                return False
    return True


def sudoku_solver(board: Board) -> bool:
    position = find_empty_position(board)
    if not position:
        return True
    y, x = position
    # solving the board using backtracking
    for num in range(1, 10):
        if check_conflict(board, position, num):
            board[y][x] = num
            if sudoku_solver(board):
                return True
            board[y][x] = 0
    return False


if __name__ == "__main__":
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7],
    ]

    print("Initial Board:")
    print_board(board)

    sudoku_solver(board)

    print("\nFinal Board:")
    print_board(board)


"""
SPECS:

TIME COMPLEXITY: O(m ^ (n ^ 2))
SPACE COMPLEXITY: O(m) [in the call stack]
[m = number of unfilled positions, n = dimension of the board]
"""
