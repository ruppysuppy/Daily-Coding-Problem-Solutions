"""
Problem:

You are given a string of length N and a parameter k. The string can be manipulated by
taking one of the first k letters and moving it to the end.

Write a program to determine the lexicographically smallest string that can be created
after an unlimited number of moves.

For example, suppose we are given the string daily and k = 1. The best we can create in
this case is ailyd.
"""


def generate_next(string: str, k: int) -> str:
    return string[k:] + string[:k]


def get_lexicographically_smallest_string(string: str, k: int) -> str:
    seen = set()
    result = string
    curr = generate_next(string, k)

    while curr not in seen:
        result = min(result, curr)
        seen.add(curr)
        curr = generate_next(curr, k)
    return result


if __name__ == "__main__":
    print(get_lexicographically_smallest_string("daily", 1))
    print(get_lexicographically_smallest_string("salloo", 2))
    # unlimited number of moves allowed (so the word of length 5 and k = 2 goes round)
    print(get_lexicographically_smallest_string("daily", 2))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n ^ 2)
"""
