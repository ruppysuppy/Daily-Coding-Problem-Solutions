"""
Problem:

Given a function f, and N return a debounced f of N milliseconds.

That is, as long as the debounced f continues to be invoked, f itself will not be
called for N milliseconds.
"""

from time import sleep
from typing import Any, Callable


def debounce(ms: int) -> Callable:
    interval_seconds = ms / 1000

    def decorate(f: Callable) -> Any:
        def wrapped(*args, **kwargs):
            print("waiting initiated...")
            sleep(interval_seconds)
            print("waiting over...")

            return f(*args, **kwargs)

        return wrapped

    return decorate


@debounce(3000)
def add_nums(x: int, y: int) -> int:
    return x + y


if __name__ == "__main__":
    print(add_nums(1, 1))
    print()
    print(add_nums(1, 2))
    print()
    print(add_nums(1, 3))
    print()
    print(add_nums(1, 4))
