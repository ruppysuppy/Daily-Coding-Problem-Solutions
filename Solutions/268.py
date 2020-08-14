"""
Problem:

Given a 32-bit positive integer N, determine whether it is a power of four in faster
than O(log N) time.
"""


def is_power_of_4(num):
    # https://stackoverflow.com/a/19611541/8650340
    return ((num & -num) & 0x55555554) == num


if __name__ == "__main__":
    print(is_power_of_4(2))
    print(is_power_of_4(4))  # 4 ^ 1
    print(is_power_of_4(8))
    print(is_power_of_4(16))  # 4 ^ 2
    print(is_power_of_4(32))
    print(is_power_of_4(64))  # 4 ^ 3
    print(is_power_of_4(128))
    print(is_power_of_4(256))  # 4 ^ 4


"""
SPECS:

TIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
"""
