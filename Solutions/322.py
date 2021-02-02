"""
Problem:

Starting from 0 on a number line, you would like to make a series of jumps that lead
to the integer N.

On the ith jump, you may move exactly i places to the left or right.

Find a path with the fewest number of jumps required to get from 0 to N.
"""


def get_sum_till_n(n: int) -> int:
    return (n * (n + 1)) // 2


def count_jumps(n: int) -> int:
    # answer will be same either it is positive or negative
    n = abs(n)
    ans = 0
    # continue till number is lesser or not in same parity
    while get_sum_till_n(ans) < n or (get_sum_till_n(ans) - n) & 1:
        ans += 1
    return ans


if __name__ == "__main__":
    print(count_jumps(-3))
    print(count_jumps(0))
    print(count_jumps(1))
    print(count_jumps(2))
    print(count_jumps(3))
    print(count_jumps(4))
    print(count_jumps(5))
    print(count_jumps(9))
    print(count_jumps(10))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
