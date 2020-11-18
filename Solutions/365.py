"""
Problem:

A quack is a data structure combining properties of both stacks and queues. It can be
viewed as a list of elements written left to right such that three operations are
possible:

push(x): add a new item x to the left end of the list
pop(): remove and return the item on the left end of the list
pull(): remove the item on the right end of the list.
Implement a quack using three stacks and O(1) additional memory, so that the amortized
time for any push, pop, or pull operation is O(1).
"""

from DataStructures.Stack import Stack


class Quack:
    def __init__(self) -> None:
        self.stack_1 = Stack()
        self.stack_2 = Stack()
        self.stack_3 = Stack()
        self.elements = 0

    def __len__(self) -> int:
        return self.elements

    def push(self, x: int) -> None:
        self.stack_1.push(x)
        self.stack_2.push(x)
        self.elements += 1

    def pop(self) -> int:
        if self.elements == 0:
            raise RuntimeWarning("Quack underflow")
        if len(self.stack_2) == 0:
            while not self.stack_3.is_empty():
                self.stack_2.push(self.stack_3.pop())
        self.elements -= 1
        self.stack_2.pop()
        return self.stack_1.pop()

    def pull(self) -> int:
        if self.elements == 0:
            raise RuntimeWarning("Quack underflow")
        if len(self.stack_3) == 0:
            while not self.stack_2.is_empty():
                self.stack_3.push(self.stack_2.pop())
        self.elements -= 1
        return self.stack_3.pop()


if __name__ == "__main__":
    quack = Quack()

    quack.push(1)
    quack.push(2)
    quack.push(3)
    quack.push(4)
    quack.push(5)

    print(quack.pop())
    print(quack.pull())

    print(quack.pop())
    print(quack.pull())

    print(quack.pull())
    print(f"Length: {len(quack)}")
