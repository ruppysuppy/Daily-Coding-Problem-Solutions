"""
Problem:

Implement an LFU (Least Frequently Used) cache. It should be able to be initialized
with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we
are adding a new item, then it should also remove the least frequently used item. If
there is a tie, then the least recently used key should be removed.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.
"""

from typing import Callable, Optional


class DoubleLinkedListNode:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.freq = 0
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = DoubleLinkedListNode(None, None)
        self.rear = DoubleLinkedListNode(None, None)
        self.head.next, self.rear.prev = self.rear, self.head

    def add(self, node: DoubleLinkedListNode) -> None:
        temp = self.rear.prev
        self.rear.prev, node.next = node, self.rear
        temp.next, node.prev = node, temp
        node.freq += 1
        self._position_node(node)

    def remove(self, node: DoubleLinkedListNode) -> DoubleLinkedListNode:
        temp_last, temp_next = node.prev, node.next
        node.prev, node.next = None, None
        temp_last.next, temp_next.prev = temp_next, temp_last
        return node

    def _position_node(self, node: DoubleLinkedListNode) -> None:
        while node.prev.key and node.prev.freq > node.freq:
            node1, node2 = node, node.prev
            node1.prev, node2.next = node2.prev, node1.prev
            node1.next, node2.prev = node2, node1


class LFUCache:
    def __init__(self, capacity: int) -> None:
        self.list = DoubleLinkedList()
        self.capacity = capacity
        self.num_keys = 0
        self.hits = 0
        self.miss = 0
        self.cache = {}

    def __repr__(self) -> str:
        return (
            f"CacheInfo(hits={self.hits}, misses={self.miss}, "
            f"capacity={self.capacity}, current_size={self.num_keys})"
        )

    def __contains__(self, key: int) -> bool:
        return key in self.cache

    def get(self, key: int) -> Optional[int]:
        if key in self.cache:
            self.hits += 1
            self.list.add(self.list.remove(self.cache[key]))
            return self.cache[key].val
        self.miss += 1
        return None

    def set(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.num_keys >= self.capacity:
                key_to_delete = self.list.head.next.key
                self.list.remove(self.cache[key_to_delete])
                del self.cache[key_to_delete]
                self.num_keys -= 1
            self.cache[key] = DoubleLinkedListNode(key, value)
            self.list.add(self.cache[key])
            self.num_keys += 1
        else:
            node = self.list.remove(self.cache[key])
            node.val = value
            self.list.add(node)


if __name__ == "__main__":
    cache = LFUCache(3)

    print(cache.get("a"))

    cache.set("a", 1)
    cache.set("b", 2)
    cache.set("c", 3)

    print(cache.get("a"))

    cache.set("d", 4)
    cache.set("e", 5)

    print(cache.get("a"))
    print(cache.get("b"))
    print(cache.get("c"))
    print(cache.get("d"))
    print(cache.get("e"))

    print(cache)
