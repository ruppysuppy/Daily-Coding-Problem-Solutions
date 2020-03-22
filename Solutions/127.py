'''
Problem:

Let's represent an integer in a linked list format by having each node represent a digit in the number. 
The nodes make up the number in reversed order.

For example, the following linked list:
1 -> 2 -> 3 -> 4 -> 5 is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

Example:

Input = 9 -> 9, 5 -> 2
Output = 4 -> 2 -> 1 [124 = 99 + 25]
'''

# local import from the Datastructure module
from DataStructures.LinkedList import Node, Linked_list

# function to add node at the rear of a linked list
def add(self, val=0):
    # if there are no nodes, a node is created and both head and rear points to it
    if (self.head == None):
        self.head = Node(val)
        self.rear = self.head
    
    # if a node already exists, the new node is added to the rear
    else:
        self.rear.next = Node(val)
        self.rear = self.rear.next

# function to add 2 linked lists
def __add__(self, other):
    # ans stores the funal result
    # pos1 is a pointer for the 1st linked list
    # pos2 is a pointer for the 2nd linked list
    # carry stores the carry for the current position
    # temp stores the sum for the current position
    ans = Linked_list()
    pos1 = self.head
    pos2 = other.head
    carry = 0
    temp = 0

    # iterating till the end of both the lists
    while (pos1 or pos2):
        # if the 1st list is empty
        if (pos1 == None):
            # the sum is obtained
            temp = pos2.val + carry
            
            # the carry is obtained
            if (temp >= 10):
                carry = 1
                temp -= 10
            else:
                carry = 0
        
        # if the 2nd list is empty
        elif (pos2 == None):
            # the sum is obtained
            temp = pos1.val + carry
            
            # the carry is obtained
            if (temp >= 10):
                carry = 1
                temp -= 10
            else:
                carry = 0
        
        # if both the lists have value in the current position
        else:
            # the sum is obtained
            temp = pos2.val + pos1.val + carry

            # the carry is obtained
            if (temp >= 10):
                carry = 1
                temp -= 10
            else:
                carry = 0
        
        # adding the necessary value
        ans.add(temp)
        # moving to the next value
        if (pos1):
            pos1 = pos1.next
        if (pos2):
            pos2 = pos2.next
    
    # if at the end, there is a carry, its added to the linked list
    if (carry == 1):
        ans.add(1)
    
    return ans

# adding the necessary functions to the linked list class
setattr(Linked_list, 'add', add)
setattr(Linked_list, '__add__', __add__)

# function to generate a linked list from a number
def create(val):
    LL = Linked_list()

    while (val > 0):
        LL.add(val % 10)
        val = val // 10
    
    return LL

# DRIVER CODE
LL1 = create(99)
LL2 = create(25)

print(LL1)
print(LL2)
print(LL1 + LL2)
print()

LL1 = create(9)
LL2 = create(250)

print(LL1)
print(LL2)
print(LL1 + LL2)