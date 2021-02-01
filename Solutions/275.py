"""
Problem:

The "look and say" sequence is defined as follows: beginning with the term 1, each
subsequent term visually describes the digits appearing in the previous term. The first
few terms are as follows:

1
11
21
1211
111221
As an example, the fourth term is 1211, since the third term consists of one 2 and one
1.

Given an integer N, print the Nth term of this sequence.
"""

from functools import lru_cache


def generate_look_and_say_term(num: str) -> str:
    result = ""
    temp = ""
    for char in num[::-1]:
        if temp:
            if char == temp[0]:
                temp += char
            else:
                result = f"{len(temp)}{temp[0]}" + result
                temp = char
        else:
            temp = char
    result = f"{len(temp)}{temp[0]}" + result
    return result


# cache is unnecessary for small sizes, but in case of large value of n, it drastically
# speeds up the process using memorization
@lru_cache(maxsize=5)
def get_look_and_say_term(n: int) -> str:
    num = "1"
    for _ in range(n - 1):
        num = generate_look_and_say_term(num)
    return num


if __name__ == "__main__":
    for i in range(1, 6):
        print(f"{i}th term = {get_look_and_say_term(i)}")


"""
SPECS:

[n = number of terms, m = longest look and say term]
TIME COMPLEXITY: O(n + m)
SPACE COMPLEXITY: O(n + m)
[with cache]

TIME COMPLEXITY: O(n * m)
SPACE COMPLEXITY: O(m)
[without cache]
"""
