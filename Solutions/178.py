"""
Problem:

Alice wants to join her school's Probability Student Club. Membership dues are computed
via one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed by a
six. Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter? Write a program
to simulate the two games and calculate their expected value.
"""

from random import randint
from time import sleep
from typing import Tuple


def roll_dice() -> int:
    return randint(1, 6)


def simulate_game(stopping_condition: Tuple[int, int], display: bool = False) -> int:
    last_throw, second_last_throw = 0, 0
    required_second_last_throw, required_last_throw = stopping_condition
    number_of_throws = 0
    # simulation the game
    while (
        last_throw != required_last_throw
        or second_last_throw != required_second_last_throw
    ):
        current_roll = roll_dice()
        second_last_throw, last_throw = last_throw, current_roll
        number_of_throws += 1
        if display:
            sleep(0.1)
            print(f"On {number_of_throws}th throw, value: {current_roll}")
    if display:
        sleep(0.1)
        print(f"Total Throws: {number_of_throws}\n")
    return number_of_throws


if __name__ == "__main__":
    print("Game 1 (5, 6):")
    simulate_game((5, 6), True)
    print("Game 2 (5, 5):")
    simulate_game((5, 5), True)

    g1 = 0
    g2 = 0
    for i in range(10_000):
        g1 += simulate_game((5, 6))
        g2 += simulate_game((5, 5))
    print("Expectation of Game 1: {:.1f}".format(g1 / 10_000))
    print("Expectation of Game 2: {:.1f}".format(g2 / 10_000))


"""
SPECS:

TIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
"""
