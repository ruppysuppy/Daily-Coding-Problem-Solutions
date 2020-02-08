'''
Problem:

Given a matrix of 1s and 0s, return the number of "islands" in the matrix. 
A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring and their perimeter is surrounded by water.

Example:

Input = 1 0 0 0 0
        0 0 1 1 0
        0 1 1 0 0
        0 0 0 0 0
        1 1 0 0 1
        1 1 0 0 1
Output = 4 (this matrix has 4 islands)
'''

# helper function to return the valid neighbours of a point
def get_neighbours(pos, grid_shape):
    # breaking the values
    n, m = grid_shape
    i, j = pos
    # res stores the final list to be returned
    res = []

    # getting all positions surrounding the point (invalid ones included too)
    pos_list = [
        (i-1, j-1),
        (i-1, j),
        (i-1, j+1),
        (i, j-1),
        (i, j+1),
        (i+1, j-1),
        (i+1, j),
        (i+1, j+1)
    ]

    # adding the valid positions to the res list
    for pos_test in pos_list:
        y_test, x_test = pos_test
        if ((x_test >= 0 and x_test < m) and (y_test >= 0 and y_test < n)):
            res.append(pos_test)
    
    return res

# helper function to remove the island
def remove_island(mat, pos):
    # using bfs to remove the islands
    queue = [pos]

    # looping till there are no 1s (island part) surrounding the given position
    while queue:
        # getting the next position to be processed and breaking it
        curr = queue.pop(0)
        i, j = curr

        # if the position contains a 1, its replaced with 0 and the neighbours added to the queue
        if (mat[i][j] == 1):
            mat[i][j] = 0
            queue.extend(get_neighbours((i, j), (len(mat), len(mat[0]))))

# FUNCTION TO PERFORM THE OPERATION
def island_count(mat):
    # initializing the island count to 0
    count = 0

    # looping over the matrix
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            # if an island is encountered, remove_island function is called and the island count incremented
            if (mat[i][j] == 1):
                remove_island(mat, (i, j))
                count += 1
    
    return count

# DRIVER CODE
mat =  [[1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1]]
print(island_count(mat))