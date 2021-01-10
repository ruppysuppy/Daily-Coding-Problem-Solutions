"""
Problem:

Given a linked list and a positive integer k, rotate the list to the right by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become
3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become
3 -> 4 -> 5 -> 1 -> 2.
"""

from DataStructures.LinkedList import Node, LinkedList


def rotate_linked_list(ll: LinkedList, k: int = 0) -> None:
    k = k % ll.length

    for _ in range(k):
        temp = ll.head
        ll.head = ll.head.next
        temp.next = None
        ll.rear.next = temp
        ll.rear = ll.rear.next


if __name__ == "__main__":
    LL = LinkedList()
    for num in [7, 7, 3, 5]:
        LL.add(num)

    print(LL)
    rotate_linked_list(LL, 2)
    print(LL)
    print()

    LL = LinkedList()
    for num in [1, 2, 3, 4, 5]:
        LL.add(num)

    print(LL)
    rotate_linked_list(LL, 3)
    print(LL)


"""
SPECS:

TIME COMPLEXITY: O(k)
SPACE COMPLEXITY: O(1)
"""
