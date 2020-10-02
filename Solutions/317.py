"""
Problem:

Write a function that returns the bitwise AND of all integers between M and N,
inclusive.
"""


def bitwise_and_on_range(start: int, end: int) -> int:
    # using naive approach
    result = start
    for num in range(start + 1, end + 1):
        result = result & num
    return result


if __name__ == "__main__":
    print(bitwise_and_on_range(3, 4))
    print(bitwise_and_on_range(5, 6))
    print(bitwise_and_on_range(126, 127))
    print(bitwise_and_on_range(127, 215))
    print(bitwise_and_on_range(129, 215))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
