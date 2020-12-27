"""
Problem:

Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

init(size): initialize the array with size
set(i, val): updates index at i with val where val is either 1 or 0.
get(i): gets the value at index i.
"""


class Bit_Array:
    def __init__(self, length: int) -> None:
        self.length = length
        self.indices = set()

    def set(self, pos: int, val: int) -> None:
        if pos >= self.length:
            raise IndexError("Index is out of range")
        if val == 0:
            if pos in self.indices:
                self.indices.remove(pos)
        else:
            self.indices.add(pos)

    def get(self, pos: int) -> int:
        if pos >= self.length:
            raise IndexError("Index is out of range")
        if pos in self.indices:
            return 1
        return 0

    def __repr__(self) -> str:
        res = []
        for pos in range(self.length):
            if pos in self.indices:
                res.append(1)
            else:
                res.append(0)
        return str(res)


if __name__ == "__main__":
    arr = Bit_Array(8)

    print(arr)

    arr.set(5, 1)
    arr.set(1, 1)

    print(arr)

    print(arr.get(1))
    print(arr.get(4))
