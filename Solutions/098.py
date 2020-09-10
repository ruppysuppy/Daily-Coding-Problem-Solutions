"""
Problem:

Given a 2D board of characters and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Input = board, "ABCCED"
Output = true

Input = board, "SEE"
Output = true

Input = board, "ABCB"
Output = false
"""

# helper function for getting all the vaild neighbours
def get_neighbors(pos, n, m):
    i, j = pos

    # getting all neighbours
    neighbors = [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]

    result = []

    # eliminating the invalid neighbours
    for pos in neighbors:
        i, j = pos

        if i >= 0 and i < n:
            if j >= 0 and j < m:
                result.append(pos)

    return result


# helper function to perform the heavy lifting
def exists_helper(board, pos, string, visited=set()):
    # if the string has been exhausted True is returned [BASE CASE FOR RECURSION]
    if not string:
        return True

    # getting the neighbours of the current position
    neighbors = get_neighbors(pos, len(board), len(board[0]))

    # checking all neighbours
    for pos_neighbor in neighbors:
        i, j = pos_neighbor

        # if the next character of the string is found, we visit it and check if the rest of the string can be found
        if (board[i][j] == string[0]) and (pos_neighbor not in visited):
            # adding the current position to visited set
            visited.add((i, j))

            # checking if the rest of the string exists
            if exists_helper(board, (i, j), string[1:], visited):
                return True

            # removing the current position from visited set [BACKTRACKING]
            visited.remove((i, j))

    return False


# FUNCTION TO PERFORM THE OPERATION
def exists(board, string):
    # returning True if an empty string is passed
    if not string:
        return True

    # looping over the matrix
    for index_r, row in enumerate(board):
        for index, elem in enumerate(row):
            # if the 1st character match is found we execute the helper function
            if string[0] == elem:
                # if the helper function returns True, the string has been found (True is returned)
                if exists_helper(board, (index_r, index), string[1:], set()):
                    return True

    # False is returned is after traversing the entire board, the string is not found
    return False


# DRIVER CODE
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]

print(exists(board, "ABCCED"))
print(exists(board, "SEE"))
print(exists(board, "ABCB"))
