"""
Problem:

The number 6174 is known as Kaprekar's contant, after the mathematician who discovered
an associated property: for all four-digit numbers with at least two distinct digits,
repeatedly applying a simple procedure eventually results in this value. The procedure
is as follows:

For a given input x, create two new numbers that consist of the digits in x in
ascending and descending order. Subtract the smaller number from the larger number.
For example, this algorithm terminates in three steps when starting from 1234:

4321 - 1234 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174
Write a function that returns how many steps this will take for a given input N.
"""

KAPREKAR_CONSTANT = 6174


def get_num_steps(num: int, steps: int = 0) -> int:
    if len(set(list(str(num)))) < 2:
        raise ValueError(
            "Kaprekar's operation requires at least 2 distinct digits in the number"
        )
    if num == KAPREKAR_CONSTANT:
        return steps
    # applying Kaprekar's operation
    digits = list(str(num))
    digits.sort()
    num1 = int("".join(digits[::-1]))
    num2 = int("".join(digits))
    return get_num_steps(num1 - num2, steps + 1)


if __name__ == "__main__":
    print(get_num_steps(1234))
    print(get_num_steps(1204))


"""
SPECS:

TIME COMPLEXITY: O(1) [as it does not exceed 7]
SPACE COMPLEXITY: O(1) [as the number of digits is 4]
"""
