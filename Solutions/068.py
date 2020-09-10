"""
Problem:

On our special chessboard, two bishops attack each other if they share the same diagonal. 
This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.
You are given N bishops, represented as (row, column) tuples on a M by M chessboard. 
Write a function to count the number of pairs of bishops that attack each other. 
The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

Example:

Input = 5, [(0, 0), (1, 2), (2, 2), (4, 0)]
<The board would look like this:
[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]>
Output = 2 (since bishops 1 and 3 attack each other, as well as bishops 3 and 4)
"""

# helper function to calculate the diagonals
def get_diagonal_pos(pos, board_size):
    # breaking pos into row and column
    row = pos[0]
    col = pos[1]
    # diagonal set stores the diagonal positions of the current bishop
    diagonals = set()

    # calculating the upper left diagonal positions
    curr_row = row - 1
    curr_col = col - 1
    for _ in range(board_size):
        if curr_col < 0 or curr_row < 0:
            break

        diagonals.add((curr_row, curr_col))
        curr_row -= 1
        curr_col -= 1

    # calculating the lower right diagonal positions
    curr_row = row + 1
    curr_col = col + 1
    for _ in range(board_size):
        if curr_col >= board_size or curr_row >= board_size:
            break

        diagonals.add((curr_row, curr_col))
        curr_row += 1
        curr_col += 1

    # calculating the upper right diagonal positions
    curr_row = row - 1
    curr_col = col + 1
    for _ in range(board_size):
        if curr_col >= board_size or curr_row < 0:
            break

        diagonals.add((curr_row, curr_col))
        curr_row -= 1
        curr_col += 1

    # calculating the lower left diagonal positions
    curr_row = row + 1
    curr_col = col - 1
    for _ in range(board_size):
        if curr_col < 0 or curr_row >= board_size:
            break

        diagonals.add((curr_row, curr_col))
        curr_row += 1
        curr_col -= 1

    return diagonals


# FUNCTION TO PERFORM THE OPERATION
def num_attacking(board_size, pos_list):
    # count stores the number of attacking bishops
    count = 0

    # looping over the list of bishop positions
    for pos in pos_list:
        # the diagonals are calculated (returns a set for O(1) access)
        diagonals = get_diagonal_pos(pos, board_size)

        # checking if any bishop lies on the diagonal of the current bishop
        for pos in pos_list:
            # if there is a bishop in the diagonal, count is incremented
            # it considers odering (so (1, 2) and (2, 1) are considered different)
            if pos in diagonals:
                count += 1

    # to eliminate ordering problem, (count/2) is returned
    return count // 2


# DRIVER CODE
pos_list = [(0, 0), (1, 2), (2, 2), (4, 0)]
print(num_attacking(5, pos_list))
