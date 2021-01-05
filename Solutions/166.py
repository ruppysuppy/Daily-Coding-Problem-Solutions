"""
Problem:

Implement a 2D iterator class. It will be initialized with an array of arrays, and
should implement the following methods:

next(): returns the next element in the array of arrays. If there are no more
elements, raise an exception.
has_next(): returns whether or not the iterator still has elements left.
For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly
should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
"""

from typing import Generator, List, Optional


class Iterator2D:
    def __init__(self, iteratable2d: List[List[int]]) -> None:
        self.iteratable2d = iteratable2d
        self.generator = Iterator2D.generator_func(iteratable2d)
        self.next_value = next(self.generator)

    def __repr__(self) -> str:
        return str(self.iteratable2d)

    @staticmethod
    def generator_func(iteratable2d: List[List[int]]) -> Generator[int, None, None]:
        for iteratable in iteratable2d:
            for element in iteratable:
                yield element

    def has_next(self) -> bool:
        return self.next_value is not None

    def next(self) -> Optional[int]:
        curr_value = self.next_value
        try:
            self.next_value = next(self.generator)
        except StopIteration:
            self.next_value = None
        return curr_value


if __name__ == "__main__":
    iter_obj = Iterator2D([[1, 2], [3], [], [4, 5, 6]])
    print(iter_obj)

    print(iter_obj.has_next())
    print(iter_obj.next())

    print(iter_obj.has_next())
    print(iter_obj.next())

    print(iter_obj.has_next())
    print(iter_obj.next())

    print(iter_obj.has_next())
    print(iter_obj.next())

    print(iter_obj.has_next())
    print(iter_obj.next())

    print(iter_obj.has_next())
    print(iter_obj.next())

    print(iter_obj.has_next())
    print(iter_obj.next())
