"""
Problem:

Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns true while 1 -> 4 returns false.
"""

from DataStructures.LinkedList import LinkedList


def is_palindrome(ll: LinkedList) -> bool:
    if ll.head is None:
        return True
    elif ll.rear == ll.head:
        return True

    pos1 = ll.head
    pos2 = ll.rear
    for i in range((ll.length + 1) // 2):
        if pos1.val != pos2.val:
            return False
        # updating the end pointer
        pos = pos1
        for _ in range((ll.length - (2 * i)) - 2):
            pos = pos.next
        pos2 = pos
        # updating the start pointer
        pos1 = pos1.next
    return True


if __name__ == "__main__":
    LL = LinkedList()
    for i in [1, 4, 3, 2, 3, 4, 1]:
        LL.add(i)
    print("Palindrome: {}\t\tList: {}".format(is_palindrome(LL), LL))

    LL = LinkedList()
    for i in [1, 4, 3]:
        LL.add(i)
    print("Palindrome: {}\t\tList: {}".format(is_palindrome(LL), LL))

    LL = LinkedList()
    for i in [1]:
        LL.add(i)
    print("Palindrome: {}\t\tList: {}".format(is_palindrome(LL), LL))

    LL = LinkedList()
    print("Palindrome: {}\t\tList: {}".format(is_palindrome(LL), LL))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(1)
[This problem can be reduced to O(n) time & space by caching the Linked List in an
array]
[If a Double Linked List is used, the problem is reduced to O(n) time & O(1) space]
"""
