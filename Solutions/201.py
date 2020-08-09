"""
Problem:

You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. 
We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, eventually ending with an entry on the bottom row. 
The weight of the path is the sum of the entries.
Write a program that returns the weight of the maximum weight path.

Example:

Input = [[1], [2, 3], [1, 5, 1]]
(represents the triangle:
  1
 2 3
1 5 1)
Output = [1 -> 3 -> 5]
"""

# FUNCTION TO PERFORM THE OPERATION
def calc_path(triangle):
    # getting the number of rows
    rows = len(triangle)

    # few checks
    if rows == 0:
        return []
    elif rows == 1:
        return triangle[0]

    # traingle copy used for dynamic programming
    dp = [list(row) for row in triangle]

    # generating the 2nd last row
    for i in range(len(dp[-2])):
        dp[-2][i] = (
            (max(dp[-1][i], dp[-1][i + 1]) + dp[-2][i]),
            [max(dp[-1][i], dp[-1][i + 1]), dp[-2][i]],
        )

    # using dynamic programming to get the maximum weight (data is generated from the 3rd row from base to the peak)
    for i in range(rows - 3, -1, -1):
        for j in range(i + 1):
            # getting the maximum weight path from the current position
            # elements stored as (weight, path)
            dp[i][j] = (
                (max(dp[i + 1][j][0], dp[i + 1][j + 1][0]) + dp[i][j]),
                max((dp[i + 1][j], dp[i + 1][j + 1]), key=lambda elem: elem[0])[1]
                + [dp[i][j]],
            )

    # getting the path
    return dp[0][0][1][::-1]


# DRIVER CODE
print(calc_path([[1], [2, 3], [1, 5, 1]]))
print(calc_path([[1], [2, 3], [7, 5, 1]]))
