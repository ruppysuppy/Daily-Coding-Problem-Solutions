"""
Problem:

Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.
It should contain the following methods:
* set(key, value, time): # sets key to value for t = time.
* get(key, time): # gets the key at t = time.
The map should work like this. 
If we set a key at a particular time, it will maintain that value forever or until it gets set at a later time. 
In other words, when we get a key at a time, it should return the value that was set for that key set at the most recent time.

Example 1:
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
d.get(1, 1) # get key 1 at time 1 should be 1
d.get(1, 3) # get key 1 at time 3 should be 2

Example 2:
d.set(1, 1, 5) # set key 1 to value 1 at time 5
d.get(1, 0) # get key 1 at time 0 should be null
d.get(1, 10) # get key 1 at time 10 should be 1

Example 3:
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
d.get(1, 0) # get key 1 at time 0 should be 2
"""

# Node class for storing the data (for Double Linked List)
class Node:
    # initialization
    def __init__(self, val_list, time):
        self.val_list = val_list
        self.time = time
        self.next = None
        self.prev = None

    # string function
    def __str__(self):
        if self.next:
            return f"{self.val_list} ({self.time}) <=> {str(self.next)}"
        else:
            return f"{self.val_list} ({self.time})"

    # equality function
    def __eq__(self, other):
        if type(other) != Node:
            return False

        return self.time == other.time


# Double Linked List to maintain the nodes
class Double_Linked_List:
    # initialization
    def __init__(self):
        self.head = None
        self.rear = None
        self.length = 0

    # string function
    def __str__(self):
        return str(self.head)

    # boolean function
    def __bool__(self):
        return bool(self.head)

    # function to add the value at the end of the linked list
    def add(self, val_list, time):
        self.length += 1

        if self.head == None:
            self.head = Node(val_list, time)
            self.rear = self.head

        else:
            self.rear.next = Node(val_list, time)
            self.rear.next.prev = self.rear
            self.rear = self.rear.next


# Map class to perform the necessary operations
class Map:
    # initialization
    def __init__(self):
        self.linked_list = Double_Linked_List()

    # FUNCTION TO PERFORM THE OPERATION (set)
    def set(self, key, value, time):
        # if the linked list is empty, the value is added
        if not self.linked_list:
            self.linked_list.add({key: value}, time)

        else:
            # getting the head of the linked list
            pos = self.linked_list.head

            # iterating till a node containing larger time is found
            while pos and pos.time < time:
                pos = pos.next

            # if the node has to inserted at the begining
            if pos == self.linked_list.head:
                # creating a new node to hold the values at the new time
                temp_val_list = {key: value}
                new_node = Node(temp_val_list, time)

                # creating the connections
                self.linked_list.head.prev = new_node
                new_node.next = self.linked_list.head
                self.head = new_node

            # if we haven't reached the end of the linked list
            if pos:
                # if the time is equal to the given time, the value is updated
                if time == pos.time:
                    pos.val_list[key] = value
                else:
                    # creating a new node to hold the values at the new time
                    temp_val_list = dict(pos.prev.val_list)
                    temp_val_list[key] = value
                    new_node = Node(temp_val_list, time)

                    # creating the connections
                    new_node.next = pos
                    new_node.prev = pos.prev
                    pos.prev.next = new_node
                    pos.prev = new_node
            else:
                # adding the new node at the rear
                temp_val_list = dict(self.linked_list.rear.val_list)
                temp_val_list[key] = value
                self.linked_list.add(temp_val_list, time)

    # FUNCTION TO PERFORM THE OPERATION (get)
    def get(self, key, time):
        # checking if the linked list has any value
        if not self.linked_list:
            return None

        # getting the head of the linked list
        pos = self.linked_list.head

        # iterating till a node containing larger time is found
        while pos and pos.time < time:
            pos = pos.next

        # if we have reached the end of the linked list
        if not pos:
            try:
                temp = self.linked_list.rear.val_list[key]
                return temp
            except:
                return None
        # if we have found the time
        elif pos and pos.time == time:
            try:
                temp = pos.val_list[key]
                return temp
            except:
                return None
        # if the time is greater, we return the value from the last timestamp
        else:
            try:
                temp = pos.prev.val_list[key]
                return temp
            except:
                return None


# DRIVER CODE
d = Map()
d.set(1, 1, 0)  # set key 1 to value 1 at time 0
d.set(1, 2, 2)  # set key 1 to value 2 at time 2
# print(d.linked_list)
print(d.get(1, 1))  # get key 1 at time 1 should be 1
print(d.get(1, 3))  # get key 1 at time 3 should be 2
print()

d = Map()
d.set(1, 1, 5)  # set key 1 to value 1 at time 5
# print(d.linked_list)
print(d.get(1, 0))  # get key 1 at time 0 should be null
print(d.get(1, 10))  # get key 1 at time 10 should be 1
print()

d = Map()
d.set(1, 1, 0)  # set key 1 to value 1 at time 0
d.set(1, 2, 0)  # set key 1 to value 2 at time 0
# print(d.linked_list)
print(d.get(1, 0))  # get key 1 at time 0 should be 2
