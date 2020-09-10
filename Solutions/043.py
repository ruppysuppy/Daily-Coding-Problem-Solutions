"""
Problem:

Implement a stack that has the following methods:
* push(val), which pushes an element onto the stack
* pop(), which pops off and returns the topmost element of the stack. 
    If there are no elements in the stack, then it should throw an error or return null.
* max(), which returns the maximum value in the stack currently. 
    If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.
"""

# STACK CLASS
class Stack:
    # Initialize function (Automatically called upon creating an object instance)
    def __init__(self):
        # stack: stores the stack
        # maximum: stores the all the maxima till the given point
        self.stack = []
        self.maximum = []

    # String function (Automatically called upon converting to string, generally used when printing)
    def __str__(self):
        return (
            "Stack: "
            + ("{} " * len(self.stack))
            + "\nMax Stack: "
            + ("{} " * len(self.maximum))
        ).format(*self.stack, *self.maximum)

    # FUNCTION TO PERFORM THE OPERATION (push)
    def push(self, val):
        # Adding the value to the stack
        self.stack.append(val)

        # if the current value is larger than the previous maxima, its added to the maximum list
        if not self.maximum or self.stack[self.maximum[-1]] < val:
            self.maximum.append(len(self.stack) - 1)

    # FUNCTION TO PERFORM THE OPERATION (pop)
    def pop(self):
        # if the stack is empty, None is returned
        if not self.stack:
            return None

        # if the current element to be removed is in the maximum list, its removed
        if len(self.stack) == self.maximum[-1] + 1:
            self.maximum.pop()

        # the last element is returned
        return self.stack.pop()

    # FUNCTION TO PERFORM THE OPERATION (max)
    def max(self):
        # if the stack is empty, None is returned
        if not self.stack:
            return None

        # the value at the position (self.maximum[-1]) is returned as the maximum list stores the addresses
        return self.stack[self.maximum[-1]]


# DRIVER CODE
s = Stack()
s.push(1)
s.push(3)
s.push(2)
s.push(5)
print(s.max())
print(s)
print(s.pop())
print(s.max())
print(s)
print(s.pop())
print(s.max())
print(s)
print(s.pop())
print(s.max())
print(s)
print(s.pop())
print(s.max())
print(s)
print(s.pop())
