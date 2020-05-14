'''
Problem:

Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. 
This should be done in-place.
Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.
Hint: Try working backwards from the end state.

Example:

Input = [1, 2, 3, 4]
Output = [1, 4, 2, 3]

Input = [1, 2, 3, 4, 5]
Output = [1, 5, 2, 4, 3]
'''

# importing necessary classes from Datastructures module
from DataStructures.Stack import Stack
from DataStructures.Queue import Queue

# FUNCTION TO PERFORM THE OPERATION
def interleave(stack):
    # creating the queue
    queue = Queue()
    
    # interleaving the elements
    for i in range(1, len(stack)):
        for _ in range(i, len(stack)):
            queue.enqueue(stack.pop())
        for _ in range(len(queue)):
            stack.push(queue.dequeue())
    
    # returning the stack
    return stack

# DRIVER CODE
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack)

stack = interleave(stack)

print(stack)

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack)

stack = interleave(stack)

print(stack)