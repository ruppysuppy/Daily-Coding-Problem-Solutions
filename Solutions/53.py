'''
Problem:

Implement a queue using two stacks. 
Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: 
* enqueue: which inserts an element into the queue
* dequeue: which removes it.
'''

# local import from the DataStructure module
from DataStructures.Stack import Stack

# modifying the default stack class to incorporate subraction operations
class Stack_modified(Stack):
    # keeping the default initialization
    def __init__(self):
        Stack.__init__(self)

    # subtraction operation (popping all elements from one stack and pushing it to another stack, essentially reversing it)
    def __sub__(self, other):
        # creating temp
        temp = self.pop()

        # popping from the satck and pushing it to the other till the 1st stack is empty
        while (temp != None):
            other.push(temp)
            temp = self.pop()

# queue class using 2 stacks
class Queue():
    # initalization with 2 stacks (stack1 is the main stack, stack2 is auxillary, its requried for dequeue operation)
    def __init__(self):
        self.stack1 = Stack_modified()
        self.stack2 = Stack_modified()
    
    # enqueue adds the passed value to the end of stack1
    def enqueue(self, val):
        self.stack1.push(val)
    
    # dequeue opearation
    def dequeue(self):
        # storing the inverted stack1 in stack2
        self.stack1 - self.stack2
        # getting the 1st inserted element (present at the rear of stack2)
        temp = self.stack2.pop()
        # storing the inverted stack2 in stack1 (getting stack1 without the 1st inserted element)
        self.stack2 - self.stack1

        # returning the 1st inserted element
        return temp
    
    # string function to display the stack
    def __str__(self):
        return ("Queue in Stack form:\n" + self.stack1.__str__())

# DRIVER CODE
queue = Queue()
print(queue)
queue.enqueue(1)
print(queue)
queue.enqueue(5)
print(queue)
queue.enqueue(9)
print(queue)
queue.enqueue(3)
print(queue)
queue.enqueue(4)
print(queue)
queue.enqueue(0)
print(queue)
print("De-Queued Element: {}".format(queue.dequeue()))
print(queue)
print("De-Queued Element: {}".format(queue.dequeue()))
print(queue)