"""
Problem:

A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.
Given N, write a function to return the number of knight's tours on an N by N chessboard.
"""

# global variable count
COUNT = 0

# helper function to get the list of possible next moves
def get_valid_pos(pos, n):
    # breaking the pos into x and y
    y, x = pos

    # getting all the next moves
    pos_arr = [
        (y + 1, x + 2),
        (y - 1, x + 2),
        (y + 1, x - 2),
        (y - 1, x - 2),
        (y + 2, x + 1),
        (y + 2, x - 1),
        (y - 2, x + 1),
        (y - 2, x - 1),
    ]

    # res: stores the permissible moves
    res = []

    # traversing the list of moves
    for i in range(8):
        # breaking the position into x_test and y_test
        y_test, x_test = pos_arr[i]

        # adding the valid moves to res
        if not (y_test >= n or x_test >= n or x_test < 0 or y_test < 0):
            res.append(pos_arr[i])

    # returning the valid moves
    return res


# helper function to check if all locations have been visited
def complete_check(board):
    # traversing each row
    for row in board:
        # traversing each element
        for elem in row:
            # if the element=0 (not visited), False is returned
            if elem == 0:
                return False
    # if no unvisited element is found, True is returned
    return True


# helper function to solve the problem (does the actual processing)
def solver_helper(board, pos):
    # declaring COUNT as a global variable
    global COUNT

    # if the board is complete, count is incremented and None returned [backtracked and resolved]
    # (as all combinations has to be check: we need the number of possible solutions, not the solution)
    if complete_check(board):
        COUNT += 1
        return

    # looping over the valid positions
    for valid_pos in get_valid_pos(pos, len(board)):
        # breaking the pos into x and y
        y, x = valid_pos

        # if the position has not been visited in the current path, its processed
        if board[y][x] == 0:
            # marking the position as visited
            board[y][x] = 1
            # recursively calling the function to solve for the other positions
            solver_helper(board, valid_pos)
            # backtracking and resolving the board
            board[y][x] = 0

    return


# FUNCTION TO SOLVE THE PROBLEM
def solve(n):
    # declaring COUNT as a global variable
    global COUNT

    # creating the board using list comprehension
    board = [[0 for i in range(n)] for j in range(n)]
    # setting the initial position of the knight
    board[0][0] = 1

    # calling the helper function to solve the problem
    solver_helper(board, (0, 0))

    # keeping the value of COUNT in temp and reseting COUNT
    temp = COUNT
    COUNT = 0

    # returning temp
    return temp


# DRIVER CODE
print(solve(1))
print(solve(2))
print(solve(3))
print(solve(4))
print(solve(5))
