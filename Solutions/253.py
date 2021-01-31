"""
Problem:

Given a string and a number of lines k, print the string in zigzag form. In zigzag,
characters are printed out diagonally from top left to bottom right until reaching the
kth line, then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:

t     a     g
 h   s z   a
  i i   i z
   s     g
"""


def clamp(num: int, min_value: int, max_value: int) -> int:
    return max(min(num, max_value), min_value)


def print_zigzag_string(string: str, k: int) -> None:
    if k < 1:
        return

    length = len(string)
    matrix = [[" " for _ in range(length)] for _ in range(k)]
    i, j = 0, 0
    is_increasing = True
    # generating zigzag string matrix
    for char in string:
        matrix[i][j] = char
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
    # displaying the string matrix
    for row in matrix:
        for elem in row:
            print(elem, end="")
        print()


if __name__ == "__main__":
    print_zigzag_string("thisisazigzag", 4)
    print()
    print_zigzag_string("thisisazigzag", 3)
    print()
    print_zigzag_string("thisisazigzag", 2)
    print()
    print_zigzag_string("thisisazigzag", 1)


"""
SPECS:

TIME COMPLEXITY: O(n x k)
SPACE COMPLEXITY: O(n x k)
"""
