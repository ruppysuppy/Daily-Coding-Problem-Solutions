"""
Problem:

Write a map implementation with a get function that lets you retrieve the value of a
key at a particular time.

It should contain the following methods:
    set(key, value, time): # sets key to value for t = time.
    get(key, time): # gets the key at t = time.
The map should work like this. If we set a key at a particular time, it will maintain
that value forever or until it gets set at a later time. In other words, when we get a
key at a time, it should return the value that was set for that key set at the most
recent time.

Consider the following examples:

d.set(1, 1, 0)  # set key 1 to value 1 at time 0
d.set(1, 2, 2)  # set key 1 to value 2 at time 2
d.get(1, 1)     # get key 1 at time 1 should be 1
d.get(1, 3)     # get key 1 at time 3 should be 2

d.set(1, 1, 5)  # set key 1 to value 1 at time 5
d.get(1, 0)     # get key 1 at time 0 should be null
d.get(1, 10)    # get key 1 at time 10 should be 1

d.set(1, 1, 0)  # set key 1 to value 1 at time 0
d.set(1, 2, 0)  # set key 1 to value 2 at time 0
d.get(1, 0)     # get key 1 at time 0 should be 2
"""

from typing import Any, Dict, Optional


class Node:
    def __init__(self, val_list: Dict[int, int], time: int) -> None:
        self.val_list = val_list
        self.time = time
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        if self.next:
            return f"{self.val_list} ({self.time}) <=> {str(self.next)}"
        return f"{self.val_list} ({self.time})"

    def __eq__(self, other: Any) -> bool:
        if type(other) == Node:
            return self.time == other.time
        return False


class Double_Linked_List:
    def __init__(self) -> None:
        self.head = None
        self.rear = None
        self.length = 0

    def __repr__(self) -> str:
        return str(self.head)

    def __bool__(self) -> bool:
        return bool(self.head)

    def add(self, val_list: Dict[int, int], time: int) -> None:
        self.length += 1
        if self.head == None:
            self.head = Node(val_list, time)
            self.rear = self.head
        else:
            self.rear.next = Node(val_list, time)
            self.rear.next.prev = self.rear
            self.rear = self.rear.next


class Map:
    def __init__(self) -> None:
        self.linked_list = Double_Linked_List()

    def set(self, key: int, value: int, time: int) -> None:
        if not self.linked_list:
            self.linked_list.add({key: value}, time)
        else:
            pos = self.linked_list.head
            while pos and pos.time < time:
                pos = pos.next
            # adding the new node at the head
            if pos == self.linked_list.head:
                temp_val_list = {key: value}
                new_node = Node(temp_val_list, time)

                self.linked_list.head.prev = new_node
                new_node.next = self.linked_list.head
                self.head = new_node
            # adding the new value
            if pos:
                if time == pos.time:
                    pos.val_list[key] = value
                else:
                    temp_val_list = dict(pos.prev.val_list)
                    temp_val_list[key] = value
                    new_node = Node(temp_val_list, time)

                    new_node.next = pos
                    new_node.prev = pos.prev
                    pos.prev.next = new_node
                    pos.prev = new_node
                return
            temp_val_list = dict(self.linked_list.rear.val_list)
            temp_val_list[key] = value
            self.linked_list.add(temp_val_list, time)

    def get(self, key: int, time: int) -> Optional[int]:
        if not self.linked_list:
            return None

        pos = self.linked_list.head
        while pos and pos.time < time:
            pos = pos.next
        # key in the rear
        if not pos:
            try:
                temp = self.linked_list.rear.val_list[key]
                return temp
            except:
                return None
        # key in the current node
        elif pos and pos.time == time:
            try:
                temp = pos.val_list[key]
                return temp
            except:
                return None
        # key in previous node
        else:
            try:
                temp = pos.prev.val_list[key]
                return temp
            except:
                return None


if __name__ == "__main__":
    d = Map()
    d.set(1, 1, 0)          # set key 1 to value 1 at time 0
    d.set(1, 2, 2)          # set key 1 to value 2 at time 2
    print(d.get(1, 1))      # get key 1 at time 1 should be 1
    print(d.get(1, 3))      # get key 1 at time 3 should be 2
    print()

    d = Map()
    d.set(1, 1, 5)          # set key 1 to value 1 at time 5
    print(d.get(1, 0))      # get key 1 at time 0 should be null
    print(d.get(1, 10))     # get key 1 at time 10 should be 1
    print()

    d = Map()
    d.set(1, 1, 0)          # set key 1 to value 1 at time 0
    d.set(1, 2, 0)          # set key 1 to value 2 at time 0
    print(d.get(1, 0))      # get key 1 at time 0 should be 2
