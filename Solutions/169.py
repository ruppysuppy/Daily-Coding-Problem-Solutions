"""
Problem:

Given a linked list, sort it in O(n log n) time and constant space.

Example:

Input = 4 -> 1 -> -3 -> 99
Output = -3 -> 1 -> 4 -> 99
"""

# importing from the local Datastructures module
from DataStructures.LinkedList import Node, Linked_list

# merge function
def sortedMerge(self, a, b):
    # base cases (when either part becomes empty)
    if a == None:
        return b
    if b == None:
        return a

    result = None

    # pick either a or b (whichever smaller) and recursion to form the sorted list
    if a.val <= b.val:
        result = a
        result.next = self.sortedMerge(a.next, b)
    else:
        result = b
        result.next = self.sortedMerge(a, b.next)

    return result


# merge sort function for the linked list
def mergeSort(self, h):
    # Base case if head is None
    if h == None or h.next == None:
        return h

    # get the middle of the list
    middle = self.getMiddle(h)
    nexttomiddle = middle.next

    # set the next of middle node to None
    middle.next = None

    # apply mergeSort on left list
    left = self.mergeSort(h)

    # apply mergeSort on right list
    right = self.mergeSort(nexttomiddle)

    # merge the left and right lists
    sortedlist = self.sortedMerge(left, right)
    return sortedlist


# utility function to get the middle of the linked list using fast pointer slow pointer
def getMiddle(self, head):
    # checking if the part is empty
    if head == None:
        return head

    # initializing the fast and slow pointers
    slow = head
    fast = head

    # finding the middle
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next

    # returning the middle
    return slow


# sort function
def sort(self):
    # sorting the linked list
    self.head = self.mergeSort(self.head)

    # updating the rear
    curr = self.head
    while curr.next:
        curr = curr.next
    self.rear = curr

    # returning the linked list
    return self


# adding the necessary function to linked list class
setattr(Linked_list, "sortedMerge", sortedMerge)
setattr(Linked_list, "mergeSort", mergeSort)
setattr(Linked_list, "getMiddle", getMiddle)
setattr(Linked_list, "sort", sort)

# DRIVER CODE
LL = Linked_list()

for val in [6, 3, 7, 5, 30, 2, 50]:
    LL.add(val)

print(LL)
LL.sort()
print(LL)
print()

LL = Linked_list()

for val in [4, 1, -3, 99]:
    LL.add(val)

print(LL)
LL.sort()
print(LL)
