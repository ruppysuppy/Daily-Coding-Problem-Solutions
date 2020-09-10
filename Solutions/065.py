"""
Problem:

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

Example:
[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
=>1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
"""

# unwind helper function to get the current ring
def unwind_mat_helper(mat, ring, n, m):
    # ring_arr stores the elements of the current ring
    ring_arr = []

    # getting the 1st row
    for i in range(ring, m - ring):
        ring_arr.append(mat[ring][i])

    # getting the last column
    for i in range(ring + 1, n - ring):
        ring_arr.append(mat[i][m - ring - 1])

    # getting the last row (if it exists)
    if n > 1 and m > 1:
        for i in range(m - ring - 2, ring - 1, -1):
            ring_arr.append(mat[n - ring - 1][i])

    # getting the last column (if it exists)
    if n > 1 and m > 1:
        for i in range(n - ring - 2, ring, -1):
            ring_arr.append(mat[i][ring])

    return ring_arr


# FUNCTION TO PERFORM THE OPERATION
def unwind_mat(mat, n, m):
    # res stores the list of unwinded matrix elements
    res = []

    # if (there is more than 1 row/col)
    if n > 1 and m > 1:
        # the number of rings will be (max(n, m)//2)
        # res is extended by the ring as per the number of iterations
        for i in range(max(n, m) // 2):
            res.extend(unwind_mat_helper(mat, i, n, m))

    # if there is 1 row or column, only 1 ring is present
    else:
        res = unwind_mat_helper(mat, 0, n, m)

    return res


# DRIVER CODE
mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
for i in unwind_mat(mat, len(mat), len(mat[0])):
    print(i)

print()
mat = [[1, 2, 3], [4, 5, 6]]
for i in unwind_mat(mat, len(mat), len(mat[0])):
    print(i)

print()
mat = [[1, 4], [2, 5], [3, 6]]
for i in unwind_mat(mat, len(mat), len(mat[0])):
    print(i)

print()
mat = [[1], [2], [3], [4], [5], [6]]
for i in unwind_mat(mat, len(mat), len(mat[0])):
    print(i)

print()
mat = [[1, 2, 3]]
for i in unwind_mat(mat, len(mat), len(mat[0])):
    print(i)
