"""
Problem:

Write a function, add_subtract, which alternately adds and subtracts curried arguments.
Here are some sample operations:

add_subtract(7) -> 7
add_subtract(1)(2)(3) -> 1 + 2 - 3 -> 0
add_subtract(-5)(10)(3)(9) -> -5 + 10 - 3 + 9 -> 11
"""

from __future__ import annotations


class CallableInt(int):
    def __init__(self, value: int) -> None:
        int.__init__(value)
        self.should_add = True

    def __call__(self, value: int) -> CallableInt:
        if self.should_add:
            result = CallableInt(self + value)
        else:
            result = CallableInt(self - value)
        result.update_should_add(not self.should_add)
        return result

    def update_should_add(self, should_add: bool) -> None:
        self.should_add = should_add


def add_subtract(value: int) -> CallableInt:
    return CallableInt(value)


if __name__ == "__main__":
    print(add_subtract(7))
    print(add_subtract(1)(2)(3))
    print(add_subtract(-5)(10)(3)(9))
