"""
Problem:

Alice wants to join her school's Probability Student Club. 
Membership dues are computed via one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. 
Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter?
Write a program to simulate the two games and calculate their expected value.
"""

# importing randint to simulate dice roll and sleep for displaying the simulation
from random import randint
from time import sleep

# function to simulate dice roll
def dice_roll():
    return randint(1, 6)


# FUNCTION TO PERFORM THE OPERATION
def game(stopping_cond, display=False):
    # temp1 and temp2 stores the last 2 throws
    # counter stores the number of throws
    temp1 = 0
    temp2 = 0
    counter = 0

    # simulation the game
    while temp1 != stopping_cond[1] or temp2 != stopping_cond[0]:
        # rolling the dice and updating temp1 and temp2
        val = dice_roll()
        temp2 = temp1
        temp1 = val
        counter += 1

        # displaying the simulation if the user whished to see it
        if display:
            sleep(0.1)
            print(f"On {counter}th throw, value: {val}")

    # displaying the simulation if the user whished to see it
    if display:
        sleep(0.1)
        print(f"Total Value: {counter}\n")

    # returning the number of rolls
    return counter


# DRIVER CODE

# simulation
print("Game 1 (5, 6):")
game((5, 6), True)
print("Game 2 (5, 5):")
game((5, 5), True)

# expected value calculation
g1 = 0
g2 = 0

for i in range(10000):
    g1 += game((5, 6))
    g2 += game((5, 5))

print("Expectation of Game 1: {:.1f}".format(g1 / 10000))
print("Expectation of Game 2: {:.1f}".format(g2 / 10000))
