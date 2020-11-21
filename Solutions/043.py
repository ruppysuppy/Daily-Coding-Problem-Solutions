"""
Problem:

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no
elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements
in the stack, then it should throw an error or return null.
Each method should run in constant time.
"""

from DataStructures.Stack import Stack


class MaxStack:
    def __init__(self) -> None:
        self.stack = Stack()
        self.maximum = Stack()

    def __repr__(self) -> str:
        return f"Stack: {self.stack}\nMax Stack: {self.maximum}"

    def push(self, val: int) -> None:
        self.stack.push(val)
        # if the current value is larger than the previous maxima, its index is added
        # to the maximum stack
        if self.maximum.is_empty() or self.stack[self.maximum.peek()] < val:
            self.maximum.push(len(self.stack) - 1)

    def pop(self) -> int:
        if self.stack.is_empty():
            raise RuntimeError("Cannot pop from a empty stack")
        # if the index of the current element to be removed is in the maximum stack,
        # its removed as well
        if len(self.stack) == self.maximum.peek() + 1:
            self.maximum.pop()
        return self.stack.pop()

    def max(self) -> int:
        if self.stack.is_empty():
            raise RuntimeError("Cannot get max of a empty stack")
        # the maximum is accessed from the last poistion stored in maximum stack
        return self.stack[self.maximum.peek()]


if __name__ == "__main__":
    s = MaxStack()

    s.push(1)
    s.push(3)
    s.push(2)
    s.push(5)

    print(s.max())
    print(s)
    print(s.pop())
    print()

    print(s.max())
    print(s)
    print(s.pop())
    print()

    print(s.max())
    print(s)
    print(s.pop())
    print()

    print(s.max())
    print(s)
    print(s.pop())
    print()

    print(s)
