"""
Problem:

You are presented with an 8 by 8 matrix representing the positions of pieces on a chess
board. The only pieces on the board are the black king and various white pieces. Given
this matrix, determine whether the king is in check.

For details on how each piece moves, see here.

For example, given the following matrix:

...K....
........
.B......
......P.
.......R
..N.....
........
.....Q..
You should return True, since the bishop is attacking the king diagonally.
"""

from typing import List


def is_attacking(board: List[List[str]]) -> bool:
    for i in range(8):
        for j in range(8):
            # case pawn
            if board[i][j] == "P":
                if j > 0 and board[i - 1][j - 1] == "K":
                    return True
                if j < 8 and board[i - 1][j + 1] == "K":
                    return True
            # case rook
            elif board[i][j] == "R":
                for k in range(8):
                    if board[i][k] == "K" or board[k][j] == "K":
                        return True
            # case knight
            elif board[i][j] == "N":
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
                for y, x in moves:
                    if 0 <= y < 8 and 0 <= x < 8 and board[y][x] == "K":
                        return True
            # case bishop
            elif board[i][j] == "B":
                for y, x in zip(range(i, -1, -1), range(j, -1, -1)):
                    if board[y][x] == "K":
                        return True
                for y, x in zip(range(i, 8), range(j, -1, -1)):
                    if board[y][x] == "K":
                        return True
                for y, x in zip(range(i, 8), range(j, 8)):
                    if board[y][x] == "K":
                        return True
                for y, x in zip(range(i, -1, -1), range(j, 8)):
                    if board[y][x] == "K":
                        return True
            # case queen
            elif board[i][j] == "Q":
                for y, x in zip(range(i, -1, -1), range(j, -1, -1)):
                    if board[y][x] == "K":
                        return True
                for y, x in zip(range(i, 8), range(j, -1, -1)):
                    if board[y][x] == "K":
                        return True
                for y, x in zip(range(i, 8), range(j, 8)):
                    if board[y][x] == "K":
                        return True
                for y, x in zip(range(i, -1, -1), range(j, 8)):
                    if board[y][x] == "K":
                        return True
                for k in range(8):
                    if board[i][k] == "K" or board[k][j] == "K":
                        return True
    return False


if __name__ == "__main__":
    print(
        is_attacking(
            [
                [".", ".", ".", "K", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", "B", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "P", "."],
                [".", ".", ".", ".", ".", ".", ".", "R"],
                [".", ".", "N", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", "Q", ".", "."],
            ]
        )
    )


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
[n = number of pieces on the board (as the board is of dimension 8 x 8, all checks
for if a piece is attacking the king take O(1) time)]
"""
