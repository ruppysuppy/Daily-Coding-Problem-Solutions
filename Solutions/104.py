'''
Problem:

Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

Example:

Input = 1 -> 4 -> 3 -> 4 -> 1 
Output = true

Input = 1 -> 4 
Output = false
'''

# local import from the DataStructures module
from DataStructures.LinkedList import Linked_list

# FUNCTION TO PERFORM THE OPERATION
def palindrome(self):
    # if the linked list is empty, False is returned
    if (self.head == None):
        return False
    
    # if the list contains only 1 element, True is returned
    elif (self.rear == self.head):
        return True
    
    else:
        # pos1 stores the addresses for comparison from the beginning
        pos1 = self.head
        # pos2 stores the addresses for comparison from the end
        pos2 = self.rear

        # comparing all the values from the beginning to the end
        for i in range((self.length + 1) // 2):
            # if there's a mismatch, False is returned
            if (pos1.val != pos2.val):
                return False

            # updating the end pointer (pos2)   [operation done for Single Linked List, so its of O(n^2), for Double Linked List, it would be O(n)]
            pos = pos1
            for _ in range((self.length - (2 * i)) - 2):
                pos = pos.next
            pos2 = pos

            # updating the beginning pointer (pos1)
            pos1 = pos1.next

        return True

# adding the function to the Linked List class
setattr(Linked_list, 'palindrome', palindrome)

# DRIVER CODE
LL = Linked_list()
LL.add(1)
LL.add(4)
LL.add(3)
LL.add(2)
LL.add(3)
LL.add(4)
LL.add(1)

print("Palindrome: {}\t\tList: {}".format(LL.palindrome(), LL))

LL = Linked_list()
LL.add(1)
LL.add(4)
LL.add(3)

print("Palindrome: {}\t\tList: {}".format(LL.palindrome(), LL))

LL = Linked_list()
LL.add(1)

print("Palindrome: {}\t\tList: {}".format(LL.palindrome(), LL))

LL = Linked_list()

print("Palindrome: {}\t\tList: {}".format(LL.palindrome(), LL))