'''
Problem:

You have a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input. 
Write a function that shuffles a deck of cards represented as an array using only swaps.
It should run in O(N) time.
Hint: Make sure each one of the 52! permutations of the deck is equally likely.
'''

# library import
from random import randint

# a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input.
def rand_gen(k):
    return randint(1, k)


# FUNCTION TO PERFORM THE OPERATION
def swap():
    # creating an array containing numbers from 1 to 52
    arr = [i for i in range(1, 53)]

    # Looping over the array
    for i in range(52):
        # getting the index to swap (index is in the range [0, 51], so subtracting 1 from the generated random number)
        temp = rand_gen(52) - 1

        # swapping the elements at the current position with the element at the generated position
        arr[i], arr[temp] = arr[temp], arr[i]

    # returning the randomized sequence
    return arr

# DRIVER CODE
print(*swap())
print(*swap())