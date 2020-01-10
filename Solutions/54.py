'''
Problem:

Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. 
The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.
Implement an efficient sudoku solver.
'''

# function to print a properly formatted board
def print_board(board):
    # looping over the board
    for i in range(len(board)):
        # printing the subsection (row)
        if (i % 3 == 0 and i != 0):
            print("- - - - - - - - - - - -")

        # looping over the rows
        for j in range(len(board[0])):
            # printing the subsection (col)
            if (j % 3 == 0 and j != 0):
                print(" | ", end="")
            # displaying the elements ("." if the element is absent)
            if (board[i][j] != 0):
                print(board[i][j], end=" ")
            else:
                print(".", end=" ")
        # breaking into a new line
        print()

# function to return the 1st empty element
def find_empty(board):
    # traversing sequentially and searching for the 1st element containing 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] == 0):
                return (i, j)

    # if the board is filled, None is returned
    return None

# function to check if a number can be placed without facing some confilct with another element
def check(board, pos, num):
    # row check
    for i in range(len(board[0])):
        if (board[pos[0]][i] == num):
            return False
    
    # column check
    for i in range(len(board)):
        if (board[i][pos[1]] == num):
            return False
    
    # sub-section check
    sec_row = pos[0] // 3
    sec_col = pos[1] // 3

    # looping over the 3 rows in the sub-section
    for i in range((sec_row*3), (sec_row*3)+3):
        # looping over the 3 columns in the sub-section
        for j in range((sec_col*3), (sec_col*3)+3):
            # if the number is found, False is returned
            if (board[i][j] == num):
                return False
    
    # returning True if there is no confilct in any segment (row, col, sub-section)
    return True

# function to solve the sudoku board (recursive using backtracking)
def sudoku_solver(board):
    # finding the 1st empty element
    loc = find_empty(board)
    # if the board is filled, True is returned
    if (not loc):
        return True

    # trying to place 1 to 9 in the empty element, if successful, recursive call on board
    # if placement fails (due to conflict), backtracked to the last function call and modifying the value
    for i in range(1, 10):
        # checking placement with 1 to 9
        if (check(board, loc, i)):
            board[loc[0]][loc[1]] = i

            # trying to solve for the next missing element
            if (sudoku_solver(board)):
                return True
            
            # backtracking is placement was unsuccessful
            else:
                board[loc[0]][loc[1]] = 0
    
    # returning False if the board cannot be solved
    return False

# DRIVER CODE
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

print("Initial Board:")
print_board(board)
sudoku_solver(board)
print("\nFinal Board:")
print_board(board)