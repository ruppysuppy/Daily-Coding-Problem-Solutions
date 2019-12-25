# NOTE: This solution is given by the Daily Coding Problem
# This is a Classic Backtracking Problem, it has several solution methodologies but all use backtracking

'''
Problem:

You have an N by N board. 
Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other.
That is, no two queens share the same row, column, or diagonal.

Example:

Input = 4
Output = 2
'''

# FUNCTION TO PERFORM THE OPERATION
def n_queens(n, board=[]):
    if (n == len(board)):
        return 1

    count = 0

    for col in range(n):
        board.append(col)

        if (is_valid(board)):
            count += n_queens(n, board)
        board.pop()

    return count

# Helper function to check any queens can attack the last queen.
def is_valid(board):
    current_queen_row, current_queen_col = len(board) - 1, board[-1]

    for row, col in enumerate(board[:-1]):
        diff = abs(current_queen_col - col)

        if (diff == 0 or diff == current_queen_row - row):
            return False
    
    return True

# DRIVER CODE
print(n_queens(4))