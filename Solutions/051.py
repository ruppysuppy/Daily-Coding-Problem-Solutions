"""
Problem:

Given a function that generates perfectly random numbers between 1 and k (inclusive),
where k is an input, write a function that shuffles a deck of cards represented as an
array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""

from random import randint
from typing import List

# implementation of a function that generates perfectly random numbers between 1 and k
def generate_random_number_in_range(k: int) -> int:
    return randint(1, k)


def swap() -> List[int]:
    # generating the card list
    cards = [card_no for card_no in range(1, 53)]
    # shuffling the cards
    for i in range(52):
        swap_position = generate_random_number_in_range(52) - 1
        cards[i], cards[swap_position] = cards[swap_position], cards[i]
    return cards


if __name__ == "__main__":
    print(*swap())
    print(*swap())


"""
SPECS:

TIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
[n = 52 (constant)]
"""
