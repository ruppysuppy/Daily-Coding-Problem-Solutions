"""
Problem:

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same
interface:

init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val.
get(i): gets the value at index i.
"""

from typing import List


class SparseArray:
    def __init__(self, arr: List[int], size: int) -> None:
        self.arr = {}
        self.size = size
        for index, val in enumerate(arr):
            if val != 0:
                self.arr[index] = val

    def __repr__(self) -> str:
        string = ""
        for pos in range(self.size):
            if pos in self.arr:
                string += f"{self.arr[pos]}, "
            else:
                string += "0, "
        return "[" + string.rstrip(" ,") + "]"

    def set(self, pos: int, val: int) -> int:
        if pos > self.size:
            raise IndexError
        if val == 0:
            if pos in self.arr:
                del self.arr[pos]
        else:
            self.arr[pos] = val

    def get(self, pos: int) -> int:
        if pos > self.size:
            raise IndexError
        if pos in self.arr:
            return self.arr[pos]
        return 0


if __name__ == "__main__":
    arr = SparseArray([1, 0, 0, 0, 3, 0, 2, 0], 8)

    print(arr)

    print(arr.get(0))
    print(arr.get(2))
    arr.set(2, 4)
    print(arr.get(2))
    arr.set(4, 1)
    print(arr.get(4))
    arr.set(0, 0)
    print(arr.get(0))

    print(arr)
