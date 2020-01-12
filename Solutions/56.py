'''
Problem:

You are given an undirected graph represented as an adjacency matrix and an integer k. 
Write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices share the same color.
You can use at most k colors.
'''

# FUNCTION TO PERFORM THE OPERATION
def check_can_color(adjacency_matrix, k):
    # col_req: tracks the minimum number of color required
    col_req = 0

    # looping over the rows of the adjacency_matrix
    for i in range(len(adjacency_matrix)):
        # temp: tracks the minimum number of colors reuired to color the current node's neighbors
        temp = 1

        # looping over all neighbors
        for j in range(len(adjacency_matrix[0])):
            # if i == j => there is a loop in the graph (its not considered), else temp is incremented
            if (i != j):
                if (adjacency_matrix[i][j] != 0):
                    temp += 1
        
        # updating col_req as per requirement
        if (temp > col_req):
            col_req = temp

    # returns boolean (whether col_req is less than or equal to k)
    return (col_req <= k)

# DRIVER CODE
adjacency_matrix = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
]

print(check_can_color(adjacency_matrix, 4))
print(check_can_color(adjacency_matrix, 3))