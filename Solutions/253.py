'''
Problem:

Given a string and a number of lines k, print the string in zigzag form. In zigzag, characters are printed out diagonally from top left to bottom right until reaching the kth line, then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:

t     a     g
 h   s z   a
  i i   i z
   s     g
'''


def clamp(num, min_value, max_value):
    # function to clamp the number with-in the given range
    return max(min(num, max_value), min_value)


def print_zigzag(string, k):
    if k < 1:
        return
    length = len(string)
    # storing the sting in a matrix
    mat = [[" " for _ in range(length)] for _ in range(k)]
    i, j = 0, 0
    is_increasing = True

    # generating the string matrix
    for char in string:
        mat[i][j] = char
        j += 1
        if is_increasing:
            i += 1
        else:
            i -= 1
        if i == k or i == -1:
            is_increasing = not is_increasing
            if i == k:
                i = clamp(i - 2, 0, k - 1)
            else:
                i = clamp(i + 2, 0, k - 1)
    # printing the string matrix
    for row in mat:
        for elem in row:
            print(elem, end="")
        print()


# DRIVER CODE
print_zigzag("thisisazigzag", 4)
print()
print_zigzag("thisisazigzag", 3)
print()
print_zigzag("thisisazigzag", 2)
print()
print_zigzag("thisisazigzag", 1)
