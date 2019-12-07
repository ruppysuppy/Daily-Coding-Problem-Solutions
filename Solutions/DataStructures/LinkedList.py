class Node():
    '''
    Node Class for the nodes of a Linked List
    '''

    # Initialize function (Automatically called upon creating an object instance)
    def __init__(self, val=None):
        self.val = val
        self.next = None
    
    # String function (Automatically called upon converting to string, generally used when printing)
    def __str__(self):
        if (self.next):
            return (f"{str(self.val)} => {str(self.next)}")
        else:
            return str(self.val)

class Linked_list():
    '''
    Linked List Class

    Functions:
    add: function to add a node at the end of the linked list
    '''

    # Initialize function (Automatically called upon creating an object instance)
    def __init__(self):
        self.head = None
        self.rear = None
        self.length = 0
    
    # String function (Automatically called upon converting to string, generally used when printing)
    def __str__(self):
        return str(self.head)
    
    def add(self, val=0):
        # Adds a new node with the provided value and adds it to the end of the list (at the rear)
        self.length += 1

        if (self.head == None):
            self.head = Node(val)
            self.rear = self.head
        
        else:
            self.rear.next = Node(val)
            self.rear = self.rear.next
    
    # Polymorphic function to return the length of the object
    def __len__(self):
        return self.length