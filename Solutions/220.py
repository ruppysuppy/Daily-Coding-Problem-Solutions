"""
Problem:

In front of you is a row of N coins, with values v_1, v_2, ..., v_n.

You are asked to play the following game. You and an opponent take turns choosing
either the first or last coin from the row, removing it from the row, and receiving the
value of the coin.

Write a program that returns the maximum amount of money you can win with certainty, if
you move first, assuming your opponent plays optimally.
"""

from typing import List


def optimal_strategy_of_game(
    coins_arr: List[int], amount: int = 0, to_play: bool = True
) -> int:
    if not coins_arr:
        return amount
    if to_play:
        return max(
            optimal_strategy_of_game(coins_arr[1:], amount + coins_arr[0], False),
            optimal_strategy_of_game(coins_arr[:-1], amount + coins_arr[-1], False),
        )
    if coins_arr[0] > coins_arr[-1]:
        return optimal_strategy_of_game(coins_arr[1:], amount, True)
    return optimal_strategy_of_game(coins_arr[:-1], amount, True)


if __name__ == "__main__":
    print(optimal_strategy_of_game([1, 2, 3, 4, 5]))


"""
SPECS:

TIME COMPLEXITY: O(2 ^ n)
SPACE COMPLEXITY: O(n)
"""
