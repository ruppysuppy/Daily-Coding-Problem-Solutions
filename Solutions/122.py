"""
Problem:

You are given a 2-d matrix where each cell represents number of coins in that cell. 
Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

Example:

Input  [[0, 3, 1, 1],
        [2, 0, 0, 4],
        [1, 5, 3, 1]]
Output = 12 (0 + 2 + 1 + 5 + 3 + 1 = 12 coins)
"""

# FUNCTION TO PERFORM THE OPERATION
def get_max_coins(mat):
    # getting n and m (rows and columns)
    n = len(mat)
    m = len(mat[0])

    # iterating through the matrix
    for i in range(1, n):
        for j in range(1, m):
            # updating the values of the matrix
            mat[i][j] = max(mat[i - 1][j], mat[i][j - 1]) + mat[i][j]

    # returning the result at the last column of the last row
    return mat[n - 1][m - 1]


# DRIVER CODE
mat = [[0, 3, 1, 1], [2, 0, 0, 4], [1, 5, 3, 1]]
print(get_max_coins(mat))

mat = [[0, 3, 1, 1], [2, 8, 9, 4], [1, 5, 3, 1]]
print(get_max_coins(mat))
