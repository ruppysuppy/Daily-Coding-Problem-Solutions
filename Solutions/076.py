"""
Problem:

You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of
columns that can be removed to ensure that each row is ordered from top to bottom
lexicographically. That is, the letter at each column is lexicographically later as you
go down each row. It does not matter whether each row itself is ordered
lexicographically.

For example, given the following table:

cba
daf
ghi
This is not ordered because of the a in the center. We can remove the second column to
make it ordered:

ca
df
gi
So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

abcdef
Your function should return 0, since the rows are already ordered (there's only one
row).

As another example, given the following table:

zyx
wvu
tsr
Your function should return 3, since we would need to remove all the columns to order
it.
"""

from typing import List


def get_minimum_column_removals(matrix: List[List[int]]) -> int:
    rows, columns = len(matrix), len(matrix[0])
    count = 0
    for column in range(columns):
        # checking if the column is lexicographical
        for row in range(rows - 1):
            if matrix[row][column] > matrix[row + 1][column]:
                count += 1
                break
    return count


if __name__ == "__main__":
    print(get_minimum_column_removals(["cba", "daf", "ghi"]))
    print(get_minimum_column_removals(["abcdef"]))
    print(get_minimum_column_removals(["zyx", "wvu", "tsr"]))


"""
SPECS:

TIME COMPLEXITY: O(n x m)
SPACE COMPLEXITY: O(1)
"""
