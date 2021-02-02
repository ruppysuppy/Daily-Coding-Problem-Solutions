"""
Problem:

Implement a queue using a set of fixed-length arrays.

The queue should support enqueue, dequeue, and get_size operations.
"""

from typing import Any


class Queue:
    def __init__(self, num_of_arr: int, size_of_arr: int) -> None:
        # storing the fixed length arrays as matrix
        self.matrix = [[None for _ in range(size_of_arr)] for _ in range(num_of_arr)]
        self.size_of_arr, self.num_of_arr = size_of_arr, num_of_arr
        self.head_pos, self.rear_pos = 0, 0

    def enqueue(self, obj: Any) -> None:
        if self.rear_pos == (self.num_of_arr * self.size_of_arr) - 1:
            raise OverflowError("Queue is full")

        i = (self.rear_pos) // self.size_of_arr
        j = (self.rear_pos) % self.size_of_arr
        self.matrix[i][j] = obj
        self.rear_pos += 1

    def dequeue(self) -> Any:
        if self.rear_pos == 0:
            raise RuntimeError("Queue is empty")

        obj = self.matrix[0][0]
        # resetting other elements' position
        for pos in range(1, self.rear_pos + 1):
            i = (pos) // self.size_of_arr
            j = (pos) % self.size_of_arr
            if j == 0:
                self.matrix[i - 1][self.size_of_arr - 1] = self.matrix[i][j]
            else:
                self.matrix[i][j - 1] = self.matrix[i][j]
        self.rear_pos -= 1
        return obj

    def get_size(self) -> int:
        return self.rear_pos


if __name__ == "__main__":
    queue = Queue(3, 2)

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("SIZE:", queue.get_size())
    print(queue.dequeue())
    print("SIZE:", queue.get_size())

    queue.enqueue(4)

    print(queue.dequeue())

    queue.enqueue(5)
    queue.enqueue(6)

    print("SIZE:", queue.get_size())

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    print("SIZE:", queue.get_size())
