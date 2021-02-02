"""
Problem:

Given an integer n, find the next biggest integer with the same number of 1-bits on.
For example, given the number 6 (0110 in binary), return 9 (1001).
"""


def get_set_bits(num: int) -> int:
    # get the number of bits set in a number [runs in O(log(n))]
    bin_num = bin(num)[2:]
    return sum([int(digit) for digit in bin_num])


def get_next_number_with_same_count_of_set_bits(num: int) -> int:
    num_of_set_bits = get_set_bits(num)
    curr = num + 1
    while True:
        if num_of_set_bits == get_set_bits(curr):
            return curr
        curr += 1


if __name__ == "__main__":
    print(get_next_number_with_same_count_of_set_bits(6))


"""
SPECS:

TIME COMPLEXITY: O(n) [as the result always lies between n and 2n]
SPACE COMPLEXITY: O(log(n))
"""
