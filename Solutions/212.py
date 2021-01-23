"""
Problem:

Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ...,
"AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. For example, given 1, return
"A". Given 27, return "AA".
"""


def get_column_name(num: int) -> str:
    result = ""
    while num > 0:
        result = chr(64 + (num % 26)) + result
        num = num // 26
    return result


if __name__ == "__main__":
    print(get_column_name(1))
    print(get_column_name(27))
    print(get_column_name(30))
    print(get_column_name(53))


"""
SPECS:

TIME COMPLEXITY: O(log(n))
SPACE COMPLEXITY: O(log(n))
"""
