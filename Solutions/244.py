"""
Problem:

The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller
than N. The method is to take increasingly larger prime numbers, and mark their
multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...]
(multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. Once we have
done this for all primes less than N, the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N
as an input).
"""


from typing import Generator, List


def sieve_of_eratosthenes(sieve: List[int] = []) -> List[int]:
    if sieve:
        length = len(sieve)
        sieve.extend([True for _ in range(length)])
    else:
        length = 10
        sieve = [True for _ in range(length * 2)]
        sieve[0], sieve[1] = False, False
    # sieve generation
    for i in range(2, 2 * length):
        if sieve[i]:
            for j in range(2 * i, 2 * length, i):
                sieve[j] = False
    return sieve


def primes_generator() -> Generator[int, None, None]:
    primes = sieve_of_eratosthenes()
    prev = 0
    while True:
        for i in range(prev, len(primes)):
            if primes[i]:
                yield i
        prev = len(primes)
        primes = sieve_of_eratosthenes(primes)


if __name__ == "__main__":
    generator = primes_generator()
    for _ in range(35):
        print(next(generator))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
