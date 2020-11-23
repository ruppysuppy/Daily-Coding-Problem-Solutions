"""
Problem:

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out)
data structure with the following methods: enqueue, which inserts an element into the
queue, and dequeue, which removes it.
"""

from DataStructures.Stack import Stack


class Queue:
    def __init__(self) -> None:
        self.stack1 = Stack()
        self.stack2 = Stack()

    def __str__(self) -> str:
        return str(self.stack2[::-1] + self.stack1[::])

    def enqueue(self, val: int) -> None:
        self._transfer_to_stack1()
        self.stack1.push(val)

    def dequeue(self) -> int:
        self._transfer_to_stack2()
        if len(self.stack2) == 0:
            raise RuntimeError("Cannot dequeue from a empty queue")
        return self.stack2.pop()

    def _transfer_to_stack2(self) -> None:
        # helper function to transfer all items to the stack 1 from stack 2
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())

    def _transfer_to_stack1(self) -> None:
        # helper function to transfer all items to the stack 2 from stack 1
        while not self.stack2.is_empty():
            self.stack1.push(self.stack1.pop())


if __name__ == "__main__":
    queue = Queue()

    print(queue)

    queue.enqueue(1)
    queue.enqueue(5)
    queue.enqueue(9)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(0)

    print(queue)

    print(queue.dequeue())
    print(queue.dequeue())

    print(queue)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    print(queue)
