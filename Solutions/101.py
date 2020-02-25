'''
Problem:

Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.
A solution will always exist. See Goldbach’s conjecture.


EXAMPLE:

Input: 4 
Output: 2, 2 (2 + 2 = 4. If there are more than one solution possible, return the lexicographically smaller solution)

(If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, 
then [a, b] < [c, d] if a < c or a==c and b < d)
'''

# function to check if a number is prime
def prime(num):
    # if the number is 2 or 3, True is returned
    if (num == 2 or num == 3):
        return True

    # looping over all its potential divisors
    for i in range(2, int(num ** 0.5) + 1):
        # if it is divisble by any number False is returned
        if (num % i == 0):
            return False
    # if no divisor is found, True is returned
    return True

# FUNCTION TO PERFORM THE OPERATION
def num_sum(n):
    # checking if n-2 is prime
    if (n > 2 and prime(n-2)):
        return (2, n-2)
    # checking if n-3 is prime
    if (n > 3 and prime(n-3)):
        return (3, n-3)
    
    # looping over all possible prime numbers [using formula all prime numbers are of the form (6n + 1) or (6n - 1)]
    for i in range(6, n//2, 6):
        # checking if (6n - 1) satisfies the result
        if (prime(i-1)):
            if (prime(n-i+1)):
                return ((i-1), (n-i+1))
        # checking if (6n + 1) satisfies the result
        elif (prime(i+1)):
            if (prime(n-i-1)):
                return ((i+1), (n-i-1))

# DRIVER CODE
inp = 4
res = num_sum(inp)
print(f"{inp} = {res[0]} + {res[1]}")

inp = 10
res = num_sum(inp)
print(f"{inp} = {res[0]} + {res[1]}")

inp = 100
res = num_sum(inp)
print(f"{inp} = {res[0]} + {res[1]}")