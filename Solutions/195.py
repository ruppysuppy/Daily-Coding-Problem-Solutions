'''
Problem:

Let M be an N by N matrix in which every row and every column is sorted. No two elements of M are equal.
Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].
'''

# FUNCTION TO PERFORM THE OPERATION
def get_num_in_range(mat, i1, j1, i2, j2):
    # getting the numbers
    num1, num2 = mat[i1][j1], mat[i2][j2] 
    
    # iterating through the matrix and finding the necessary elements
    count = sum([len([x for x in row if (x < num1 and x > num2)]) for row in mat])
    
    # returning the count
    return count

# DRIVER CODE
mat = [
 [1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]
]
print(get_num_in_range(mat, 3, 3, 1, 1))

matrix = [
    [1, 2, 3, 4],
    [5, 8, 9, 13],
    [6, 10, 12, 14],
    [7, 11, 15, 16]
]
print(get_num_in_range(matrix, 1, 3, 3, 1))

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [10, 11, 12, 13],
    [20, 21, 22, 23]
]
print(get_num_in_range(matrix, 3, 3, 1, 0))