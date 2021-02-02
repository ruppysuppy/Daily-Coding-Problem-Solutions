"""
Problem:

Mastermind is a two-player game in which the first player attempts to guess the secret
code of the second. In this version, the code may be any six-digit number with all
distinct digits.

Each turn the first player guesses some number, and the second player responds by
saying how many digits in this number correctly matched their location in the secret
code. For example, if the secret code were 123456, then a guess of 175286 would score
two, since 1 and 6 were correctly placed.

Write an algorithm which, given a sequence of guesses and their scores, determines
whether there exists some secret code that could have produced them.

For example, for the following scores you should return True, since they correspond to
the secret code 123456: {175286: 2, 293416: 3, 654321: 0}

However, it is impossible for any key to result in the following scores, so in this
case you should return False: {123456: 4, 345678: 4, 567890: 4}
"""

from typing import Dict


def validate_guess(guess: int, matches: Dict[int, int]) -> bool:
    for match, match_count in matches.items():
        count = 0
        for char_1, char_2 in zip(str(guess).zfill(6), str(match).zfill(6)):
            if char_1 == char_2:
                count += 1
        if count != match_count:
            return False
    return True


def is_match_valid(matches: Dict[int, int]) -> bool:
    for guess in range(1_000_000):
        if validate_guess(guess, matches):
            return True
    return False


if __name__ == "__main__":
    print(is_match_valid({175286: 2, 293416: 3, 654321: 0}))
    print(is_match_valid({123456: 4, 345678: 4, 567890: 4}))


"""
SPECS:

TIME COMPLEXITY: O(1) [As (1,000,000 x 6) is a constant]
SPACE COMPLEXITY: O(1)
"""
