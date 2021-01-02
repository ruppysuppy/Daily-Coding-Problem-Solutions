"""
Problem:

Implement a stack API using only a heap. A stack implements the following methods:

push(item), which adds an element to the stack
pop(), which removes and returns the most recently added element (or throws an error if
       there is nothing on the stack)

Recall that a heap has the following operations:

push(item), which adds a new key to the heap
pop(), which removes and returns the max value of the heap
"""

from sys import maxsize

from DataStructures.Heap import MinHeap


class Stack:
    def __init__(self) -> None:
        self.heap = MinHeap()
        self.next_wt = maxsize

    def pop(self) -> int:
        if len(self.heap) == 0:
            raise ValueError("Stack Underflow")
        _, val = self.heap.extract_min()
        return val

    def push(self, val: int) -> None:
        self.heap.insert((self.next_wt, val))
        self.next_wt -= 1


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(7)
    stack.push(4)

    print(stack.pop())

    stack.push(2)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
