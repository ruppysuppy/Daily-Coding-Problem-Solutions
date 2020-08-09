"""
Problem:

The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N.
The method is to take increasingly larger prime numbers, and mark their multiples as composite.
For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on.
Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.
Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).
"""


def SoE(sieve=[]):
    # if an sieve is passed, its doubled in size to generate a larger sieve
    if sieve:
        length = len(sieve)
        sieve.extend([True for _ in range(length)])
    # if no sieve is passed, a sieve is formed with 20 numbers
    else:
        length = 10
        sieve = [True for _ in range(length * 2)]
        sieve[0], sieve[1] = False, False

    # computing the sieve
    for i in range(2, 2 * length):
        if sieve[i]:
            for j in range(2 * i, 2 * length, i):
                sieve[j] = False
    return sieve


def primes_generator():
    # generator function to keep yielding prime numbers
    primes = SoE()
    prev = 0
    while True:
        # returning the prime numbers and doubling the size of primes array after the
        # current array is exhausted
        for i in range(prev, len(primes)):
            if primes[i]:
                yield i
        prev = len(primes)
        primes = SoE(primes)


# DRIVER CODE
generator = primes_generator()
for _ in range(30):
    print(next(generator))
