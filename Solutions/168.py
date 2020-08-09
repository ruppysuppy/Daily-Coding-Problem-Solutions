"""
Problem:

Given an N by N matrix, rotate it by 90 degrees clockwise.
Follow-up: What if you couldn't use any extra space?

Example:

Input = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

Output = [[7, 4, 1],
          [8, 5, 2],
          [9, 6, 3]]
"""

# numpy array to format the output
from numpy import array

# FUNCTION TO PERFORM THE OPERATION
def rotate_matrix(matrix):
    # getting the number of layers and the last row index
    num_layers = len(matrix) // 2
    max_ind = len(matrix) - 1

    # iterating through the matrix (rotating all numbers)
    for layer in range(num_layers):
        for ind in range(layer, max_ind - layer):
            # rotate 4 numbers (
            #   right col to bottom row,
            #   bottom row to left col,
            #   left col to top row,
            #   top row to right col
            # )
            temp = matrix[layer][ind]
            matrix[layer][ind] = matrix[max_ind - ind][layer]
            matrix[max_ind - ind][layer] = matrix[max_ind - layer][max_ind - ind]
            matrix[max_ind - layer][max_ind - ind] = matrix[ind][max_ind - layer]
            matrix[ind][max_ind - layer] = temp

    return matrix


# DRIVER CODE
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(array(rotate_matrix(matrix)))

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(array(rotate_matrix(matrix)))
