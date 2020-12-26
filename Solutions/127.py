"""
Problem:

Let's represent an integer in a linked list format by having each node represent a
digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5 is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9 5 -> 2 return 124 (99 + 25) as:

4 -> 2 -> 1
"""

from DataStructures.LinkedList import LinkedList, Node


def add_linked_lists(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    sum_linked_list = LinkedList()
    pos1, pos2 = ll1.head, ll2.head
    carry, curr_position_sum = 0, 0
    # generating the sum of the linked lists
    while pos1 or pos2:
        if pos1 == None:
            curr_position_sum = pos2.val + carry
            if curr_position_sum >= 10:
                carry, curr_position_sum = 1, curr_position_sum - 10
            else:
                carry = 0
        elif pos2 == None:
            curr_position_sum = pos1.val + carry
            if curr_position_sum >= 10:
                carry, curr_position_sum = 1, curr_position_sum - 10
            else:
                carry = 0
        else:
            curr_position_sum = pos2.val + pos1.val + carry
            if curr_position_sum >= 10:
                carry, curr_position_sum = 1, curr_position_sum - 10
            else:
                carry = 0
        sum_linked_list.add(curr_position_sum)
        # moving to the next value
        if pos1:
            pos1 = pos1.next
        if pos2:
            pos2 = pos2.next
    if carry == 1:
        sum_linked_list.add(1)
    return sum_linked_list


def create_linked_list(val: int) -> LinkedList:
    LL = LinkedList()
    while val > 0:
        LL.add(val % 10)
        val = val // 10
    return LL


if __name__ == "__main__":
    LL1 = create_linked_list(99)
    LL2 = create_linked_list(25)

    print(LL1)
    print(LL2)
    print(add_linked_lists(LL1, LL2))
    print()

    LL1 = create_linked_list(9)
    LL2 = create_linked_list(250)

    print(LL1)
    print(LL2)
    print(add_linked_lists(LL1, LL2))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
