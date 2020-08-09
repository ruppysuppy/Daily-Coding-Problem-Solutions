"""
Problem:

Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

Example: 

Input = 156
Output = 3
"""

# FUNCTION TO PERFORM THE OPERATION
def longest_chain_of_1(num):
    # getting the binary representation
    num = bin(num)[2:]
    # chain max stores the number of 1's in the longest chain
    chain_max = 0
    # chain curr stores the number of 1's in the current chain
    chain_curr = 0

    # iterating through the binary number
    for i in num:
        # updating chain max and chain curr
        if i == "1":
            chain_curr += 1
        else:
            chain_max = max(chain_max, chain_curr)
            chain_curr = 0

    # returning the result
    return max(chain_max, chain_curr)


# DRIVER CODE
print(longest_chain_of_1(15))
print(longest_chain_of_1(156))
