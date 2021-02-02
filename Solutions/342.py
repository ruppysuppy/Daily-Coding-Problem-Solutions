"""
Problem:

reduce (also known as fold) is a function that takes in an array, a combining function,
and an initial value and builds up a result by calling the combining function on each
element of the array, left to right. For example, we can write sum() in terms of
reduce:

def add(a, b):
    return a + b

def sum(lst):
    return reduce(lst, add, 0)

This should call add on the initial value with the first element of the array, and then
the result of that with the second element of the array, and so on until we reach the
end, when we return the sum of the array.

Implement your own version of reduce.
"""

from typing import Any, Callable, Iterable


def reduce(iterable: Iterable, func: Callable, initial_value: int) -> int:
    value = initial_value
    for item in iterable:
        value = func(value, item)
    return value


def add(a: int, b: int) -> int:
    return a + b


def sum(lst: Iterable) -> int:
    return reduce(lst, add, 0)


if __name__ == "__main__":
    print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
[for the reduce function only (considering the iterable doesn't contain a nested
iterable)]
"""
