"""
Problem:

You have an N by N board. Write a function that, given N, returns the number of
possible arrangements of the board where N queens can be placed on the board without
threatening each other, i.e. no two queens share the same row, column, or diagonal.
"""

from typing import List


def n_queens(n: int, queen_positions: List[int] = []) -> int:
    # N Queen solution using backtracking
    if n == len(queen_positions):
        return 1

    count = 0
    for col in range(n):
        queen_positions.append(col)
        if is_valid(queen_positions):
            count += n_queens(n, queen_positions)
        queen_positions.pop()
    return count


def is_valid(queen_positions: List[int]) -> bool:
    # check to see if any queen is threatening the current queen
    current_queen_row, current_queen_col = len(queen_positions) - 1, queen_positions[-1]
    for row, col in enumerate(queen_positions[:-1]):
        diff = abs(current_queen_col - col)
        if (
            diff == 0                           # same row
            or diff == current_queen_row - row  # same diagonal
        ):
            return False
    return True


if __name__ == "__main__":
    print(n_queens(1))
    print(n_queens(4))
    print(n_queens(5))


"""
SPECS:

TIME COMPLEXITY: O(2 ^ n)
SPACE COMPLEXITY: O(n)
"""
