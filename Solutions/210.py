"""
Problem:

A Collatz sequence in mathematics can be defined as follows. Starting with any positive
integer:

If n is even, the next number in the sequence is n / 2
If n is odd, the next number in the sequence is 3n + 1 It is conjectured that every
such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?
"""

from typing import List


def get_collatz_sequence_length(num: int, acc: int = 0) -> int:
    if num == 1:
        return acc
    if num % 2 == 0:
        return get_collatz_sequence_length(num // 2, acc + 1)
    return get_collatz_sequence_length(3 * num + 1, acc + 1)


def get_longest_collatz_sequence_under_1000000() -> int:
    longest_sequence_value = 0
    longest_sequence = 0
    for i in range(1, 1_000_000):
        curr_sequence = get_collatz_sequence_length(i, 0)
        if curr_sequence > longest_sequence:
            longest_sequence = curr_sequence
            longest_sequence_value = i
    return longest_sequence_value


if __name__ == "__main__":
    # NOTE: brute force implementation, it will take quite a bit of time to execute
    print(get_longest_collatz_sequence_under_1000000())


"""
SPECS:

TIME COMPLEXITY: O(log(n))
SPACE COMPLEXITY: O(log(n))
"""
