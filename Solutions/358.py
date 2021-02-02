"""
Problem:

Create a data structure that performs all the following operations in O(1) time:

plus: Add a key with value 1. If the key already exists, increment its value by one.
minus: Decrement the value of a key. If the key's value is currently 1, remove it.
get_max: Return a key with the highest value.
get_min: Return a key with the lowest value.
"""

from sys import maxsize

from DataStructures.PriorityQueue import MaxPriorityQueue, MinPriorityQueue


class MagicDS:
    def __init__(self) -> None:
        self.map = {}
        self.max_priority_queue = MaxPriorityQueue()
        self.min_priority_queue = MinPriorityQueue()

    def plus(self, elem: int) -> None:
        # runs in O(log(n)) [O(1) on Amortized analysis]
        if elem not in self.map:
            self.map[elem] = 1
            self.max_priority_queue.push(elem, 1)
            self.min_priority_queue.push(elem, 1)
        else:
            self.map[elem] += 1
            self.max_priority_queue.update_key(elem, self.map[elem])
            self.min_priority_queue.update_key(elem, self.map[elem])

    def minus(self, elem: int) -> None:
        # runs in O(log(n)) [O(1) on Amortized analysis]
        if elem not in self.map:
            raise ValueError("Cannot decrement a non-existing key")
        if self.map[elem] == 1:
            del self.map[elem]
            self.max_priority_queue.update_key(elem, maxsize)
            self.max_priority_queue.extract_max()
            self.min_priority_queue.update_key(elem, 0)
            self.min_priority_queue.extract_min()
        else:
            self.map[elem] -= 1
            self.max_priority_queue.update_key(elem, self.map[elem])
            self.min_priority_queue.update_key(elem, self.map[elem])

    def get_max(self) -> int:
        # runs in O(1)
        return self.max_priority_queue.peek_max()

    def get_min(self) -> int:
        # runs in O(1)
        return self.min_priority_queue.peek_min()


if __name__ == "__main__":
    ds = MagicDS()

    ds.plus(1)
    ds.plus(1)
    ds.plus(1)
    ds.plus(2)
    ds.plus(2)
    ds.plus(3)

    print(ds.get_max())
    print(ds.get_min())

    ds.minus(1)
    ds.minus(1)
    ds.minus(1)

    print(ds.get_max())
    print(ds.get_min())
