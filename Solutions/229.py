"""
Problem:

Snakes and Ladders is a game played on a 10 x 10 board, the goal of which is get from square 1 to square 100. 
On each turn players will roll a six-sided die and move forward a number of spaces equal to the result. 
If they land on a square that represents a snake or ladder, they will be transported ahead or behind, respectively, to a new square.
Find the smallest number of turns it takes to play snakes and ladders.

For convenience, here are the squares representing snakes and ladders, and their outcomes:
snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
"""

from typing import Dict


def get_next_ladder_position(ladders: Dict[int, int], position: int):
    # helper function to get the position of the next ladder
    curr = 101
    for key in ladders:
        if key > position and key < curr:
            curr = key
    return curr


def get_next_position_with_no_snake(snakes: Dict[int, int], position: int) -> int:
    # helper function to get the position of the next move without landing on a snake
    curr = position + 6
    for _ in range(6):
        if curr not in snakes:
            break
        curr -= 1
    return curr


def play_snake_and_ladders(
    snakes: Dict[int, int], ladders: Dict[int, int], show_trace: bool = False
) -> int:
    # function to return the minimum turns required to play the current board
    position = 0
    turns = 0
    while position < 100:
        turns += 1
        position = min(
            get_next_ladder_position(ladders, position),
            get_next_position_with_no_snake(snakes, position),
            100,
        )
        if show_trace:
            print(position, end=" ")
        if position in ladders:
            position = ladders[position]
            if show_trace:
                print(f"=> {position}", end=" ")
        if position < 100 and show_trace:
            print("->", end=" ")
    if show_trace:
        print()
    return turns


if __name__ == "__main__":
    snakes = {
        16: 6,
        48: 26,
        49: 11,
        56: 53,
        62: 19,
        64: 60,
        87: 24,
        93: 73,
        95: 75,
        98: 78,
    }
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

    print(play_snake_and_ladders(snakes, ladders, show_trace=True))


"""
SPECS:

TIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
[the maximum number of squares is 100]
"""
