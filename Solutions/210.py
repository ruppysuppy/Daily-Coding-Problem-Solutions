'''
Problem:

A Collatz sequence in mathematics can be defined as follows. 
Starting with any positive integer:
* If n is even, the next number in the sequence is n / 2
* If n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?
'''

# function to calculate the number of numbers in the current sequence
# function optimized for checking all numbers in a range using cache 
# (hard-coded range is 1 to 1000000)
def collatz_seq(num, cache, i, acc=0):
    # base case for recursion
    if (num == 1):
        return acc
    
    # checking in cache if the number is in cache range
    if (num < 1000000):
        # checking if the data is in cache
        if (cache[i] != -1):
            return cache[i]
        # else generating the data and storing in the cache
        else:
            if (num % 2 == 0):
                temp = collatz_seq(num//2, cache, i, acc+1)
                cache[i] = temp
                return temp
            else:
                temp = collatz_seq(3*num+1, cache, i, acc+1)
                cache[i] = temp
                return temp
    # generating the value if its outside the cache range
    else:
        if (num % 2 == 0):
            return collatz_seq(num//2, cache, i, acc+1)
        else:
            return collatz_seq(3*num+1, cache, i, acc+1)

# FUNCTION TO PERFORM THE OPERATION
def get_longest_collatz_seq():
    # declaring the variables
    longest_sequence_value = 0
    longest_sequence = 0

    # cache to store the values
    cache = [-1] * 1_000_000

    # generating the values for the cache in bottom up approach
    for i in range(100000, 1, -1):
        # getting the length of the current sequence
        temp_sequence = collatz_seq(i, cache, i, 0)

        # updating the longest_sequence and longest_sequence_value as per requirement
        if (temp_sequence > longest_sequence):
            longest_sequence = temp_sequence
            longest_sequence_value = i
    # returning number of numbers in the longest sequence
    return longest_sequence_value

# DRIVER CODE
print(get_longest_collatz_seq())