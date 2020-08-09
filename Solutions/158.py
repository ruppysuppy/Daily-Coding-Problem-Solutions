"""
Problem:

You are given an N * M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the bottom right corner?
You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

Example:

Input = [[0, 0, 1],
         [0, 0, 1],
         [1, 0, 0]]
Output = 2
(As there are only two ways to get to the bottom right:
* Right, down, down, right
* Down, right, down, right
The top left corner and bottom right corner will always be 0.)
"""

# FUNCTION TO PERFORM THE OPERATION
def get_possible_paths(mat):
    # getting the dimensions of the matrix
    n, m = len(mat), len(mat[0])

    # resetting the values of 1 to -1 as positive numbers are used to construct the paths
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                mat[i][j] = -1

    # setting each element of the vertically down path as 1 (until a wall or the end is encountered)
    for i in range(n):
        if mat[i][0] == -1:
            break
        else:
            mat[i][0] = 1

    # setting each element of the horizontal (right-side) path as 1 (until a wall or the end is encountered)
    for i in range(m):
        if mat[0][i] == -1:
            break
        else:
            mat[0][i] = 1

    # iterating through the matrix, updating the paths
    for i in range(1, n):
        for j in range(1, m):
            # if the current position is not a wall, the value is updated
            if mat[i][j] != -1:
                # res stores how many ways the current position can be reached
                res = 0

                # updating the values based on whether it is a wall
                if mat[i - 1][j] != -1:
                    res += mat[i - 1][j]
                if mat[i][j - 1] != -1:
                    res += mat[i][j - 1]

                # storing the value in the matrix
                mat[i][j] = res

    # returning the required value
    return mat[-1][-1]


# DRIVER CODE
matrix = [[0, 0, 1], [0, 0, 1], [1, 0, 0]]
print(get_possible_paths(matrix))

matrix = [[0, 0, 1], [1, 0, 1], [1, 0, 0]]
print(get_possible_paths(matrix))

matrix = [[0, 0, 0], [1, 0, 0], [0, 0, 0]]
print(get_possible_paths(matrix))

# end cannot be reached as only right and down traversal is allowed
matrix = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
print(get_possible_paths(matrix))
