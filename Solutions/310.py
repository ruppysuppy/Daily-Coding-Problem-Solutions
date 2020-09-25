"""
Problem:

Write an algorithm that finds the total number of set bits in all integers between 1
and N.
"""


def get_set_bits(num: int) -> int:
    # get the number of bits set in a number [runs in O(log(n))]
    bin_num = bin(num)[2:]
    return sum([int(digit) for digit in bin_num])


def get_total_set_bits(N: int) -> int:
    # sums up the number of bits set in all positive numbers till N
    result = 0
    for i in range(1, N + 1):
        result += get_set_bits(i)
    return result


if __name__ == "__main__":
    print(get_total_set_bits(0))
    print(get_total_set_bits(1))
    print(get_total_set_bits(2))
    print(get_total_set_bits(3))
    print(get_total_set_bits(4))
    print(get_total_set_bits(5))


"""
SPECS:

TIME COMPLEXITY: O(n x log(n))
SPACE COMPLEXITY: O(1)
"""
