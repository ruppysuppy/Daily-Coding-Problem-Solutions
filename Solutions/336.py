"""
Problem:

Write a program to determine how many distinct ways there are to create a max heap from
a list of N given integers.

For example, if N = 3, and our integers are [1, 2, 3], there are two ways, shown below.

  3      3
 / \    / \
1   2  2   1
"""

from math import log2


def choose(n, k, nCk):
    # function to get nCk using dynamic programming
    if k > n:
        return 0
    if n <= 1:
        return 1
    if k == 0:
        return 1
    if nCk[n][k] != -1:
        return nCk[n][k]
    # updating nCk
    answer = choose(n - 1, k - 1, nCk) + choose(n - 1, k, nCk)
    nCk[n][k] = answer
    return answer


def get_left(n):
    # calculate l for give value of n
    if n == 1:
        return 0
    h = int(log2(n))
    # max number of elements that can be present in the hth level of any heap
    num_h = 1 << h  # (2 ^ h)
    # number of elements that are actually present in the last level
    # [hth level (2 ^ h - 1)]
    last = n - ((1 << h) - 1)
    # if more than half of the last level is filled
    if last >= (num_h // 2):
        return (1 << h) - 1
    else:
        return (1 << h) - 1 - ((num_h // 2) - last)


def number_of_heaps(n, dp, nCk):
    # find maximum number of heaps for n
    if n <= 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    # getting the number of nodes left
    left = get_left(n)
    # generating the result
    ans = (
        choose(n - 1, left, nCk)
        * number_of_heaps(left, dp, nCk)
        * number_of_heaps(n - 1 - left, dp, nCk)
    )
    dp[n] = ans
    return ans


def get_number_of_heaps(n):
    # initializing dynamic programming data
    dp = [-1 for i in range(n + 1)]
    nCk = [[-1 for i in range(n + 1)] for i in range(n + 1)]
    # generating result
    return number_of_heaps(n, dp, nCk)


if __name__ == "__main__":
    print(get_number_of_heaps(3))
    print(get_number_of_heaps(10))


"""
SPECS:

TIME COMPLEXITY: O(2 ^ n)
SPACE COMPLEXITY: O(n ^ 2)
"""
