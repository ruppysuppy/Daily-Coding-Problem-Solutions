"""
Problem:

You are given a 2D matrix of characters and a target word.
Write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

Example:

Mat =  [['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']]
'FOAM' => true (since it's the leftmost column)
'MASS' => true (since it's the last row)
"""

# FUNCTION TO PERFORM THE OPERATION
def word_occorance_check(mat, word):
    # getting the number of rows and columns
    n = len(mat)
    m = len(mat[0])

    # row check (searching for the word in every row)
    for i in range(n):
        temp = "".join(mat[i])

        if word in temp:
            return True

    # column check (searching for the word in every column)
    for j in range(m):
        temp = ""
        for i in range(n):
            temp += mat[i][j]

        if word in temp:
            return True

    return False


# DRIVER CODE
mat = [
    ["F", "A", "C", "I"],
    ["O", "B", "Q", "P"],
    ["A", "N", "O", "B"],
    ["M", "A", "S", "S"],
]

print(word_occorance_check(mat, "FOAM"))
print(word_occorance_check(mat, "MASS"))
print(word_occorance_check(mat, "FORM"))
