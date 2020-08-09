"""
Problem:

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. 
Each False boolean represents a tile you can walk on.
Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. 
If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.


Example:
Matrix = [[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
Start = (3, 0) 
End = (0, 0)
Output = 7
"""

# Import not mandatory (Used it to display the matrix in a prettily)
from numpy import array  # Comment out the full line if you dont have numpy

# Helper function to do the heavy lifting
def min_steps_helper(mat, pos, n, m):
    # List to store all the visited neighboring locations
    arr = []

    # Adding all the values and finding the minimum
    if (
        pos[0] < n
        and pos[0] >= 0
        and pos[1] < m
        and pos[1] >= 0
        and mat[pos[0]][pos[1]] != "t"
    ):
        if pos[0] + 1 < n and mat[pos[0] + 1][pos[1]] not in ["t", 0]:
            arr.append(mat[pos[0] + 1][pos[1]])
        if pos[0] - 1 >= 0 and mat[pos[0] - 1][pos[1]] not in ["t", 0]:
            arr.append(mat[pos[0] - 1][pos[1]])
        if pos[1] + 1 < m and mat[pos[0]][pos[1] + 1] not in ["t", 0]:
            arr.append(mat[pos[0]][pos[1] + 1])
        if pos[1] - 1 >= 0 and mat[pos[0]][pos[1] - 1] not in ["t", 0]:
            arr.append(mat[pos[0]][pos[1] - 1])

    # Updating the value of the present position
    mat[pos[0]][pos[1]] = min(arr) + 1

    # Calling the funtion on each of the valid neigboring positions
    if pos[0] + 1 < n and mat[pos[0] + 1][pos[1]] == 0:
        min_steps_helper(mat, (pos[0] + 1, pos[1]), n, m)
    if pos[0] - 1 >= 0 and mat[pos[0] - 1][pos[1]] == 0:
        min_steps_helper(mat, (pos[0] - 1, pos[1]), n, m)
    if pos[1] + 1 < m and mat[pos[0]][pos[1] + 1] == 0:
        min_steps_helper(mat, (pos[0], pos[1] + 1), n, m)
    if pos[1] - 1 >= 0 and mat[pos[0]][pos[1] - 1] == 0:
        min_steps_helper(mat, (pos[0], pos[1] - 1), n, m)


# FUNCTION TO PERFORM THE OPERATION
def min_steps(mat, n, m, start, stop):
    # Replacing the 'f's with 0's
    for i in range(n):
        for j in range(m):
            if mat[i][j] == "f":
                mat[i][j] = 0

    # Offseting the value by 1 (as 0 represents unvisited positions)
    pos = start
    mat[start[0]][start[1]] = 1

    # Calling the helper function on each neighbouring position where the value is 0
    try:
        if pos[0] + 1 < n and mat[pos[0] + 1][pos[1]] == 0:
            min_steps_helper(mat, (pos[0] + 1, pos[1]), n, m)
        if pos[0] - 1 >= 0 and mat[pos[0] - 1][pos[1]] == 0:
            min_steps_helper(mat, (pos[0] - 1, pos[1]), n, m)
        if pos[1] + 1 < m and mat[pos[0]][pos[1] + 1] == 0:
            min_steps_helper(mat, (pos[0], pos[1] + 1), n, m)
        if pos[1] - 1 >= 0 and mat[pos[0]][pos[1] - 1] == 0:
            min_steps_helper(mat, (pos[0], pos[1] - 1), n, m)

        print(array(mat))  # Comment out the full line if you dont have numpy
        # mat[end[0]][end[1]] - 1 is returned as initially the value was offsetted by +1
        return mat[end[0]][end[1]] - 1

    except:
        return None


# DRIVER CODE
mat = [
    ["f", "f", "f", "f"],
    ["t", "t", "f", "t"],
    ["f", "f", "f", "f"],
    ["f", "f", "f", "f"],
]
n = len(mat)
m = len(mat[0])
start = (3, 0)
end = (0, 0)

print(array(mat))  # Comment out the full line if you dont have numpy
print(min_steps(mat, n, m, start, end))
