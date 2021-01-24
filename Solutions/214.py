"""
Problem:

Given an integer n, return the length of the longest consecutive run of 1s in its
binary representation.

For example, given 156, you should return 3.
"""


def get_longest_chain_of_1s(num: int) -> int:
    num = bin(num)[2:]
    chain_max = 0
    chain_curr = 0

    for char in num:
        if char == "1":
            chain_curr += 1
        else:
            chain_max = max(chain_max, chain_curr)
            chain_curr = 0
    return max(chain_max, chain_curr)


if __name__ == "__main__":
    print(get_longest_chain_of_1s(15))
    print(get_longest_chain_of_1s(156))


"""
SPECS:

TIME COMPLEXITY: O(log(n))
SPACE COMPLEXITY: O(1)
[there are log2(n) digits in the binary representation of any number n]
"""
