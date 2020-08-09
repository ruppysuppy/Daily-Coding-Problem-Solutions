"""
Problem:

Implement a stack API using only a heap. A stack implements the following methods:
* push(item), which adds an element to the stack
* pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)

Recall that a heap has the following operations:
* push(item), which adds a new key to the heap
* pop(), which removes and returns the max value of the heap
"""

# importing required functions and data
from heapq import heappush, heappop
from sys import maxsize

# Stack class
class Stack:
    # initialization
    def __init__(self):
        self.heap = []
        self.next_wt = maxsize

    # pop function
    def pop(self):
        # if the heap is empty, Value Error is raised
        if not self.heap:
            raise ValueError("Stack Underflow")

        # returning the required value
        _, val = heappop(self.heap)
        return val

    # push function
    def push(self, val):
        # adding the data to the heap as (weight, value)
        heappush(self.heap, (self.next_wt, val))
        # decerementing the next value as the heap functions are for min heap
        self.next_wt -= 1


# DRIVER CODE
stack = Stack()

stack.push(1)
stack.push(7)
stack.push(4)

print(stack.pop())

stack.push(2)

print(stack.pop())
print(stack.pop())
print(stack.pop())

# Error
stack.pop()
