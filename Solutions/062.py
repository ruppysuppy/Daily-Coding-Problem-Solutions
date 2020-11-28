"""
Problem:

There is an N by M matrix of zeroes. Given N and M, write a function to count the
number of ways of starting at the top-left corner and getting to the bottom-right
corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to
get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
"""


def get_num_ways(n: int, m: int) -> int:
    matrix = [[(1 if (i == 0 or j == 0) else 0) for i in range(m)] for j in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
    return matrix[n - 1][m - 1]


if __name__ == "__main__":
    print(get_num_ways(2, 2))
    print(get_num_ways(5, 5))


"""
SPECS:

TIME COMPLEXITY: O(n x m)
SPACE COMPLEXITY: O(n x m)
"""
