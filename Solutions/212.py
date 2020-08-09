"""
Problem:

Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....
Given a column number, return its alphabetical column id. 

Example:

Input = 1
Output = "A"

Input = 27
Output = "AA"
"""

# FUNCTION TO PERFORM THE OPERATION
def get_col_name(num):
    # declaring the result
    result = ""

    # generating the result from the last character to the 1st
    while num > 0:
        result = chr(64 + (num % 26)) + result
        num = num // 26

    # returning the result
    return result


# DRIVER CODE
print(get_col_name(1))
print(get_col_name(27))
print(get_col_name(30))
print(get_col_name(53))
