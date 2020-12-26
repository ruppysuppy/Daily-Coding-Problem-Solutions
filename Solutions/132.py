"""
Problem:

Design and implement a HitCounter class that keeps track of requests (or hits). It
should support the following operations:

* record(timestamp): records a hit that happened at timestamp
* total(): returns the total number of hits recorded
* range(lower, upper): returns the number of hits that occurred between timestamps lower
                       and upper (inclusive)
Follow-up: What if our system has limited memory?
"""

from DataStructures.LinkedList import Node, LinkedList


def add_node_sorted(ll: LinkedList, val: int) -> None:
    ll.length += 1
    if not ll.head:
        ll.head = Node(val)
        ll.rear = ll.head
    elif val > ll.rear.val:
        ll.rear.next = Node(val)
        ll.rear = ll.rear.next
    else:
        pos = ll.head
        while pos.val < val:
            pos = pos.next
        temp = pos.val
        pos.val = val
        new_node = Node(temp)
        new_node.next = pos.next
        pos.next = new_node
        if pos == ll.rear:
            ll.rear = new_node


def get_number_of_nodes_in_range(ll: LinkedList, start: int, stop: int) -> int:
    if not ll.head:
        return 0

    pos = ll.head
    num = 0
    while pos and pos.val < start:
        pos = pos.next
    if not pos:
        return 0
    while pos and pos.val <= stop:
        pos = pos.next
        num += 1
    return num


class HitCounter:
    def __init__(self) -> None:
        self.List = LinkedList()
        self.start = None
        self.end = None

    def record(self, timestamp: int) -> None:
        add_node_sorted(self.List, timestamp)
        # keeping track of the smallest and largest timestamp
        if not self.start:
            self.start = timestamp
            self.end = timestamp
        elif timestamp < self.start:
            self.start = timestamp
        elif timestamp > self.end:
            self.end = timestamp

    def total(self) -> int:
        return len(self.List)

    def range(self, lower: int, upper: int) -> int:
        if upper < self.start or lower > self.end:
            return 0
        return get_number_of_nodes_in_range(self.List, lower, upper)

    def __repr__(self):
        return str(self.List)


if __name__ == "__main__":
    hc = HitCounter()

    time1 = 1
    time2 = 10
    time3 = 20

    print(hc.total())
    print(hc)
    print()

    hc.record(time2)

    print(hc.total())
    print(hc)
    print("Number in range:")
    print(hc.range(5, 15))
    print(hc.range(10, 15))
    print()

    hc.record(time1)

    print(hc.total())
    print(hc)
    print("Number in range:")
    print(hc.range(5, 15))
    print(hc.range(12, 15))
    print()

    hc.record(time3)

    print(hc.total())
    print(hc)
    print("Number in range:")
    print(hc.range(5, 15))
    print(hc.range(0, 25))
    print()
