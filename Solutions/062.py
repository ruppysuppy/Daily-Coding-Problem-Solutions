"""
Problem:

There is an N by M matrix of zeroes. 
Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. 
You can only move right or down.

Example:

2, 2 => 2 (since there are two ways to get to the bottom-right:
* Right, then down
* Down, then right)

5, 5 => 70
"""

# FUNCTION TO PERFORM THE OPERATION
def num_ways(n, m):
    # matrix creation (of shape n x m)
    # the 1st row and 1st column has 1 as there is only 1 way to move to the position (go right / go down)
    mat = [[(1 if (i == 0 or j == 0) else 0) for i in range(m)] for j in range(n)]

    # looping over the other positions and calculating the number of ways that position can be reached
    # the values are populated from top left to bottom right
    for i in range(1, n):
        for j in range(1, m):
            mat[i][j] = mat[i - 1][j] + mat[i][j - 1]

    # the final result is at the mat[n-1][m-1]
    return mat[n - 1][m - 1]


# DRIVER CODE
print(num_ways(2, 2))
print(num_ways(5, 5))
