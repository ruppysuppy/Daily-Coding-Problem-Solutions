'''
Problem:

Blackjack is a two player card game whose rules are as follows:
* The player and then the dealer are each given two cards.
* The player can then "hit", or ask for arbitrarily many additional cards, so long as their total does not exceed 21.
* The dealer must then hit if their total is 16 or lower, otherwise pass.
* Finally, the two compare totals, and the one with the greatest sum not exceeding 21 is the winner.
For this problem, cards values are counted as follows: each card between 2 and 10 counts as their face value, face cards count as 10, and aces count as 1.
Given perfect knowledge of the sequence of cards in the deck, implement a blackjack solver that maximizes the player's score (that is, wins minus losses).
'''

from random import randint


def generate_sequence():
    # generating a sequence of random cards
    sequence = []
    cards = [i for _ in range(4) for i in range(1, 11)]
    while cards:
        sequence.append(cards.pop(randint(0, len(cards) - 1)))
    return sequence


def get_best_score(sequence, player_score=0, dealer_score=0):
    # getting the best possible score (player) for the given sequence of cards
    if not sequence:
        return player_score, dealer_score
    elif player_score > 21 and dealer_score > 21:
        return -1, -1
    elif player_score > 21:
        return -1, dealer_score
    elif dealer_score > 21:
        return player_score, -1
    return max(
        get_best_score(sequence[1:], player_score + sequence[0], dealer_score),
        get_best_score(sequence[1:], player_score, dealer_score + sequence[0]),
        (player_score, dealer_score),
        # the player's score has more weightage than the dealer's score
        key=lambda x: 1.01 * x[0] + x[1]
    )


def simulate(n=1000):
    # simulating the game n times and returning the percent of victories for the player
    wins = 0
    for _ in range(n):
        sequence = generate_sequence()
        player_score, dealer_score = get_best_score(sequence)
        if player_score > dealer_score and player_score <= 21:
            wins += 1
    return (wins / n) * 100


# DRIVER CODE
print(f"The Player won {simulate():.2f}% of the times")