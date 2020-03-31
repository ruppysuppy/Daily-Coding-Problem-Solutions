'''
Problem:

Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's and return its area.

Example:

Input = [[1, 0, 0, 0],
         [1, 0, 1, 1],
         [1, 0, 1, 1],
         [0, 1, 0, 0]]
Output = 4
'''

# function to check if all elements in the given range is 1 (used to check if the covered rows can be extended)
def extendable_row(matrix, erow, scol, ecol):
    return all(matrix[erow][scol:ecol])

# function to check if all elements in the given range is 1 (used to check if the covered columns can be extended)
def extendable_col(matrix, ecol, srow, erow):
    for row in range(srow, erow):
        if not matrix[row][ecol]:
            return False
    return True

# helper function to get the maximum covered rectangular area
def area_helper(matrix, num_rows, num_cols, srow, erow, scol, ecol):
    # getting the current area
    current_area = (erow - srow) * (ecol - scol)
    # declaring default values for row and column extended area, to avoid errors while returning
    row_ex_area, col_ex_area = 0, 0

    # checking if the rows considered can be extended
    ex_row = erow < num_rows and extendable_row(matrix, erow, scol, ecol)

    # getting the row extended area
    if (ex_row):
        row_ex_area = area_helper(matrix, num_rows, num_cols,srow, erow+1, scol, ecol)

    # checking if the columns considered can be extended
    ex_col = ecol < num_cols and extendable_col(matrix, ecol, srow, erow)

    # getting the column extended area
    if (ex_col):
        col_ex_area = area_helper(matrix, num_rows, num_cols,srow, erow, scol, ecol+1)

    # returning the maximum area
    return max(current_area, row_ex_area, col_ex_area)

# FUNCTION TO PERFORM THE OPERATION
def get_max_rect(matrix):
    # if the matrix is empty 0 is returned
    if (not matrix):
        return 0

    # max_area stores the area of the largest rectangle
    max_area = 0

    # getting the number of rows and columns
    num_rows, num_cols = len(matrix), len(matrix[0])

    # iterating through the matrix
    for i in range(num_rows):
        for j in range(num_cols):
            # getting the maximum possible area by considering the area under current row and column to the end
            upper_bound_area = (num_rows - i) * (num_cols - j)

            # if the current position contains 1 and the upper bound on area is larger than the max area
            if (matrix[i][j] and upper_bound_area > max_area):
                # the maximum rectangular area covered the current and neighbouring elements is calculated
                area = area_helper(matrix, num_rows, num_cols, i, i+1, j, j+1)
                # max_area is updated according to need
                max_area = max(area, max_area)

    return max_area

# DRIVER CODE
matrix = [[1, 0, 0, 0],
          [1, 0, 1, 1],
          [1, 0, 1, 1],
          [0, 1, 0, 0]]
print(get_max_rect(matrix))

matrix = [[1, 0, 0, 0],
          [1, 0, 1, 1],
          [1, 0, 1, 1],
          [0, 1, 1, 1]]
print(get_max_rect(matrix))

matrix = [[1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1]]
print(get_max_rect(matrix))

matrix = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]
print(get_max_rect(matrix))

matrix = [[1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 0, 0],
          [0, 0, 0, 0]]
print(get_max_rect(matrix))

matrix = [[1, 1, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]]
print(get_max_rect(matrix))