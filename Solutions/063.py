"""
Problem:

Given a 2D matrix of characters and a target word, write a function that returns
whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column.
Similarly, given the target word 'MASS', you should return true, since it's the last
row.
"""

from typing import List


def check_word_occorance(matrix: List[List[str]], word: str) -> bool:
    n = len(matrix)
    m = len(matrix[0])
    # check for word occourance in the rows
    for i in range(n):
        row_string = "".join(matrix[i])
        if word in row_string:
            return True
    # check for word occourance in the columns
    for j in range(m):
        column_string = ""
        for i in range(n):
            column_string += matrix[i][j]
        if word in column_string:
            return True
    return False


if __name__ == "__main__":
    matrix = [
        ["F", "A", "C", "I"],
        ["O", "B", "Q", "P"],
        ["A", "N", "O", "B"],
        ["M", "A", "S", "S"],
    ]

    print(check_word_occorance(matrix, "FOAM"))
    print(check_word_occorance(matrix, "MASS"))
    print(check_word_occorance(matrix, "FORM"))


"""
SPECS:

TIME COMPLEXITY: O(n x m)
SPACE COMPLEXITY: O(n + m)
"""
