"""
Problem:

You are given a 2-D matrix representing an image, a location of a pixel in the screen and a color C.
Replace the color of the given pixel and all adjacent same colored pixels with C.

Example:

Input: (2, 2), 'G',
B B W
W W W
W W W
B B B

Output:
B B G
G G G
G G G
B B B
"""

# importing array from numpy (its used to properly format the matrix while displaying, not a mandatory requirement)
from numpy import array

# helper function to generate all the valid neighbouring positions
def gen_neighbours(pos, rows, cols):
    # breaking the position into i and j
    i, j = pos
    # res stores the valid neighbours
    res = []

    # getting all neighbours
    neighbours = [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j + 1),
        (i + 1, j + 1),
        (i + 1, j),
        (i + 1, j - 1),
        (i, j - 1),
    ]

    # looping over neighbours and adding the valid neighbours to res
    for neighbour in neighbours:
        y, x = neighbour

        if (not (x >= cols) and not (x < 0)) and (not (y >= rows) and not (y < 0)):
            res.append(neighbour)

    # returning res
    return res


# helper function to modify the matrix
def dfs(mat, pos, new_color, prev_color, visited, rows, cols):
    # updating the color at the current position
    mat[pos[0]][pos[1]] = new_color
    # adding the position to visited set
    visited.add(pos)

    # getting the neighbours
    neighbours = gen_neighbours(pos, rows, cols)

    # looping over neighbours
    for neighbour in neighbours:
        # checking if the color has to be modified for the given position and calling dfs as required
        if neighbour not in visited and mat[neighbour[0]][neighbour[1]] == prev_color:
            dfs(mat, neighbour, new_color, prev_color, visited, rows, cols)


# FUNCTION TO PERFORM THE OPERATION
def update(mat, pos, new_color):
    # getting the rows and columns
    rows = len(mat)
    cols = len(mat[0])

    # calling dfs the modify the matrix
    dfs(mat, pos, new_color, mat[pos[0]][pos[1]], set(), rows, cols)

    # returning the matrix
    return mat


# DRIVER CODE
print("Initial Matrix:")
mat = [["B", "B", "W"], ["W", "W", "W"], ["W", "W", "W"], ["B", "B", "B"]]
print(array(mat))
print("Updated Matrix:")
print(array(update(mat, (2, 2), "G")))
print()

print("Initial Matrix:")
mat = [["B", "B", "W"], ["W", "W", "W"], ["W", "W", "W"], ["B", "B", "B"]]
print(array(mat))
print("Updated Matrix:")
print(array(update(mat, (3, 2), "G")))
print()

print("Initial Matrix:")
mat = [["B", "B", "W"], ["W", "W", "W"], ["W", "W", "W"], ["B", "B", "B"]]
print(array(mat))
print("Updated Matrix:")
print(array(update(mat, (0, 0), "G")))
