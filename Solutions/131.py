"""
Problem:

Given the head to a singly linked list, where each node also has a 'random' pointer
that points to anywhere in the linked list, deep clone the list.
"""

from DataStructures.LinkedList import LinkedList, Node


def rand_join(ll: LinkedList, pos1: int, pos2: int) -> None:
    pos_source = ll.head
    pos_dest = ll.head
    try:
        # moving the pointers to the required position
        for _ in range(pos1):
            pos_source = pos_source.next
        for _ in range(pos2):
            pos_dest = pos_dest.next
        # setting the random pointer
        pos_source.random_ptr = pos_dest
    except:
        raise IndexError("Given position is out of the Linked List")


def clone(ll: LinkedList) -> LinkedList:
    clone_head = ll.head
    pos1 = ll.head
    pos2 = ll.head.next
    # duplicating all elements (by value in the linked list)
    # [a -> b -> c becomes a -> a -> b -> b -> c -> c]
    for _ in range(ll.length):
        pos1.next = Node(pos1.val)
        pos1 = pos1.next
        pos1.next = pos2
        pos1 = pos1.next
        if pos2 is None:
            break
        pos2 = pos2.next
    # setting the clone head to the proper position
    clone_head = clone_head.next
    pos1 = ll.head
    # setting the random pointer of the cloned linked list
    # (every 2nd element in the new linked list: a -> [a] -> b -> [b] -> c -> [c])
    for _ in range(ll.length - 1):
        pos1.next.random_ptr = pos1.random_ptr
        pos1 = pos1.next.next
    # reverting the linked list to its original form
    pos1 = ll.head
    pos2 = ll.head.next
    for _ in range(ll.length - 1):
        pos1.next = pos2.next
        pos2.next = pos2.next.next
        pos1 = pos1.next
        if pos2.next == None:
            break
        pos2 = pos2.next
    # creating the cloned linked list from the generated nodes
    cloned_LL = LinkedList()
    cloned_LL.head = clone_head
    cloned_LL.length = ll.length
    cloned_LL.rear = pos2
    return cloned_LL


# adding the random pointer to Node class
setattr(Node, "random_ptr", None)

if __name__ == "__main__":
    LL = LinkedList()

    LL.add(1)
    LL.add(2)
    LL.add(3)
    LL.add(4)

    rand_join(LL, 0, 2)
    rand_join(LL, 2, 0)
    rand_join(LL, 1, 3)

    print("Original List:", LL)

    LL_clone = clone(LL)

    print("Cloned List:", LL_clone)

    # adding different elements to show that the clone is a deep copy
    LL.add(100)
    LL_clone.add(5)

    print("\nOriginal List:", LL)

    print("Cloned List:", LL_clone)


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
