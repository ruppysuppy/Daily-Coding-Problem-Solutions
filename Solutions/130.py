"""
Problem:

Given an array of numbers representing the stock prices of a company in chronological
order and an integer k, return the maximum profit you can make from k buys and sells.
You must buy the stock before you can sell it, and you must sell the stock before you
can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
"""

from typing import List


def get_max_profit_helper(
    arr: List[int],
    curr_index: int,
    curr_profit: int,
    buys_left: int,
    sells_left: int,
    length: int,
) -> int:
    # if the end of the array is reached or no more sells can be performed current
    # profit is returned (base case for recursion)
    if curr_index == length or sells_left == 0:
        return curr_profit
    # if the number of 'buys' and 'sells' left are equal, the stock needs to be bought
    if buys_left == sells_left:
        return max(
            # wait for a different deal
            get_max_profit_helper(
                arr, curr_index + 1, curr_profit, buys_left, sells_left, length
            ),
            # buy at the current price
            get_max_profit_helper(
                arr,
                curr_index + 1,
                curr_profit - arr[curr_index],
                buys_left - 1,
                sells_left,
                length,
            ),
        )
    # if the number of 'buys' and 'sells' left are inequal, the stock needs to be sold
    return max(
        # wait and hold for selling at a different price
        get_max_profit_helper(
            arr, curr_index + 1, curr_profit, buys_left, sells_left, length,
        ),
        # sell at the current price
        get_max_profit_helper(
            arr,
            curr_index + 1,
            curr_profit + arr[curr_index],
            buys_left,
            sells_left - 1,
            length,
        ),
    )


def get_max_profit(arr: List[int], k: int) -> int:
    return get_max_profit_helper(arr, 0, 0, k, k, len(arr))


if __name__ == "__main__":
    print(get_max_profit([5, 2, 4, 0, 1], 2))
    print(get_max_profit([5, 2, 4], 2))
    print(get_max_profit([5, 2, 4], 1))


"""
SPECS:

TIME COMPLEXITY: O(2 ^ n)
SPACE COMPLEXITY: O(n)
"""
