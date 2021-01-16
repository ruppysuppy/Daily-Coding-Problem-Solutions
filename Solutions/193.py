"""
Problem:

Given a array of numbers representing the stock prices of a company in chronological
order, write a function that calculates the maximum profit you could have made from
buying and selling that stock. You're also given a number fee that represents a
transaction fee for each buy and sell transaction.

You must buy before you can sell the stock, but you can make as many transactions as
you like.

For example, given [1, 3, 2, 8, 4, 10] and fee = 2, you should return 9, since you
could buy the stock at $1, and sell at $8, and then buy it at $4 and sell it at $10.
Since we did two transactions, there is a $4 fee, so we have 7 + 6 = 13 profit minus $4
of fees.
"""

from typing import List


def get_max_profit(
    prices: List[int], fee: int, profit: int = 0, current: int = 0, can_buy: bool = True
) -> int:
    if not prices:
        return profit
    if can_buy:
        return max(
            get_max_profit(
                prices[1:], fee, profit, (-prices[0] - fee), False
            ),  # buying
            get_max_profit(
                prices[1:], fee, profit, 0, True
            ),  # holding
        )
    return max(
        get_max_profit(
            prices[1:], fee, (profit + current + prices[0]), 0, True
        ),  # selling
        get_max_profit(
            prices[1:], fee, profit, current, False
        ),  # holding
    )


if __name__ == "__main__":
    print(get_max_profit([1, 3, 2, 8, 4, 10], 2))
    print(get_max_profit([1, 3, 2, 1, 4, 10], 2))


"""
SPECS:

TIME COMPLEXITY: O(2 ^ n)
SPACE COMPLEXITY: O(n)
"""
