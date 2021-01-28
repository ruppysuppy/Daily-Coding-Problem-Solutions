"""
Problem:

You are given N identical eggs and access to a building with k floors. 
Your task is to find the lowest floor that will cause an egg to break, if dropped from that floor. 
Once an egg breaks, it cannot be dropped again. 
If an egg breaks when dropped from the xth floor, you can assume it will also break when dropped from any floor greater than x.
Write an algorithm that finds the minimum number of trial drops it will take, in the worst case, to identify this floor.

Example:

N = 1
k = 5
Output = 5 (we will need to try dropping the egg at every floor, beginning with the first, until we reach the fifth floor)
"""

from sys import maxsize


def calculate(eggs: int, floors: int) -> int:
    dp_mat = [[maxsize for _ in range(floors + 1)] for _ in range(eggs + 1)]
    # base cases
    for i in range(floors + 1):
        dp_mat[1][i] = i
        dp_mat[0][i] = 0
    for i in range(eggs + 1):
        dp_mat[i][0] = 0
    # populating the dp matrix
    for egg in range(2, eggs + 1):
        for floor in range(1, floors + 1):
            for i in range(1, floor + 1):
                temp = 1 + max(dp_mat[egg - 1][i - 1], dp_mat[egg][floor - i])
                dp_mat[egg][floor] = min(dp_mat[egg][floor], temp)
    return dp_mat[eggs][floors]


if __name__ == "__main__":
    print(calculate(2, 20))
    print(calculate(3, 15))


"""
SPECS:

TIME COMPLEXITY: O(n x (floor ^ 2))
SPACE COMPLEXITY: O(n x floor)
"""
