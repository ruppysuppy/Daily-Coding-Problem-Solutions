'''
Problem:

Design and implement a HitCounter class that keeps track of requests (or hits). 

It should support the following operations:
* record(timestamp): records a hit that happened at timestamp
* total(): returns the total number of hits recorded
* range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)

Follow-up: What if our system has limited memory?
'''

# importing datetime from the datetime module
from datetime import datetime

# local import from the DataStructure class
from DataStructures.LinkedList import Node, Linked_list

# helper function to add a value in the proper position of the linked list (ensures the list is sorted)
def add_sorted(self, val):
    # incrementing the length
    self.length += 1

    # if there is no values in the list, its added to the head
    if (not self.head):
        self.head = Node(val)
        self.rear = self.head
    
    # if the value to be added is larger than all values in the list, its added after rear
    elif (val > self.rear.val):
        self.rear.next = Node(val)
        self.rear = self.rear.next
    
    else:
        pos = self.head

        # else finding the proper position
        while (pos.val < val):
            pos = pos.next
        
        # overwriting the node's value with the new value and adding a new node with the node's old value next to the node
        temp = pos.val
        pos.val = val

        new_node = Node(temp)
        new_node.next = pos.next

        pos.next = new_node

        # if the node is rear, its reset to the new node (end of the list)
        if (pos == self.rear):
            self.rear = new_node

# helper function to get the number of nodes in the range
def in_range(self, start, stop):
    # if there is no values in the list, 0 is returned
    if (not self.head):
        return 0
    
    # moving to the proper position
    pos = self.head
    num = 0

    while (pos and pos.val < start):
        pos = pos.next
    
    # if we reach the end of the list, 0 is returned
    if (not pos):
        return 0
    
    # counting the number of elements in the range
    while (pos and pos.val <= stop):
        pos = pos.next
        num += 1
    
    return num

# adding the necessary functions to the Linked List class
setattr(Linked_list, 'add_sorted', add_sorted)
setattr(Linked_list, 'in_range', in_range)

# HitCounter class
class HitCounter:
    # initialization
    def __init__(self):
        self.List = Linked_list()
        self.start  = None
        self.end = None
    
    # record function to store timestamp
    def record(self, timestamp):
        # adding the data in sorted order
        self.List.add_sorted(timestamp)

        # keeping track of the smallest and largest timestamp
        if (not self.start):
            self.start = timestamp
            self.end = timestamp
        
        elif (timestamp < self.start):
            self.start = timestamp
        
        elif (timestamp > self.end):
            self.end = timestamp
    
    # total function to get the total number of hits
    def total(self):
        return len(self.List)
    
    # range function to get the number of hits in the time range
    def range(self, lower, upper):
        # checking if the values are in the range of the linked list
        if (upper < self.start or lower > self.end):
            return 0
        
        return self.List.in_range(lower, upper)
    
    # string function to display the object
    def __str__(self):
        return str(self.List)

# DRIVER CODE
hc = HitCounter()

time1 = datetime(2000, 1, 1, 1, 1, 1)
time2 = datetime(2000, 1, 1, 1, 1, 10)
time3 = datetime(2000, 1, 1, 1, 1, 20)

print(hc.total())
print(hc)
print()

hc.record(time2)

print(hc.total())
print(hc)
print("Number in range:")
print(hc.range(datetime(2000, 1, 1, 1, 1, 5), datetime(2000, 1, 1, 1, 1, 15)))
print(hc.range(datetime(2000, 1, 1, 1, 1, 10), datetime(2000, 1, 1, 1, 1, 15)))
print()

hc.record(time1)

print(hc.total())
print(hc)
print("Number in range:")
print(hc.range(datetime(2000, 1, 1, 1, 1, 5), datetime(2000, 1, 1, 1, 1, 15)))
print(hc.range(datetime(2000, 1, 1, 1, 1, 12), datetime(2000, 1, 1, 1, 1, 15)))
print()

hc.record(time3)

print(hc.total())
print(hc)
print("Number in range:")
print(hc.range(datetime(2000, 1, 1, 1, 1, 5), datetime(2000, 1, 1, 1, 1, 15)))
print(hc.range(datetime(2000, 1, 1, 1, 1, 0), datetime(2000, 1, 1, 1, 1, 25)))
print()