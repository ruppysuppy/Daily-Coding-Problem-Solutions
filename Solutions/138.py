"""
Problem:

Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""

from typing import List


def calc_num_coins(target: int, denominations: List[int] = [1, 5, 10, 25]) -> int:
    # pre-requisted: sorted denominations
    length = len(denominations)
    count = 0
    for i in range(length - 1, -1, -1):
        count += target // denominations[i]
        target = target % denominations[i]
        if target == 0:
            break
    if target != 0:
        raise ValueError("Target cannot be reached by using the supplied denominations")
    return count


if __name__ == "__main__":
    print(calc_num_coins(16))
    print(calc_num_coins(90))
    print(calc_num_coins(93))
    print(calc_num_coins(100))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
