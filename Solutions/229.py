'''
Problem:

Snakes and Ladders is a game played on a 10 x 10 board, the goal of which is get from square 1 to square 100. 
On each turn players will roll a six-sided die and move forward a number of spaces equal to the result. 
If they land on a square that represents a snake or ladder, they will be transported ahead or behind, respectively, to a new square.
Find the smallest number of turns it takes to play snakes and ladders.

For convenience, here are the squares representing snakes and ladders, and their outcomes:
snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
'''


def get_next_ladder(ladders, pos):
    # helper function to get the position of the next ladder
    curr = 101
    for key in ladders: 
        if (key > pos and key < curr): curr = key
    return curr


def get_next_no_snake(snakes, pos):
    # helper function to get the position of the next position without snake
    curr = pos + 6
    for _ in range(6):
        if curr in snakes: curr -= 1
        else: break
    return curr


def play_snake_and_ladders(snakes, ladders):
    # function to return the minimum turns required to play the current board
    # prints the trace of the path ('->' for normal move, '=>' for ladder move)
    pos = 0
    turns = 0

    while pos < 100:
        turns += 1
        pos = min(get_next_ladder(ladders, pos), get_next_no_snake(snakes, pos), 100)
        print(pos, end=" ")

        if (pos in ladders):
            pos = ladders[pos]
            print(f"=> {pos}", end=" ")
        if (pos < 100):
            print("->", end=" ")

    print()
    return turns


snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

print(play_snake_and_ladders(snakes, ladders))