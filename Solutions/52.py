"""
Problem:

This problem was asked by Google.
Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:
* set(key, value): sets key to value. 
If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
* get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
"""

# Node class for Double Linked List
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.last = None
        self.next = None


# LRU Cache class
class LRU_Cache:
    # initialize method
    def __init__(self, size):
        # head and rear store the head and the rear of the double linked list
        self.head = Node(None, None)
        self.rear = Node(None, None)
        self.head.next = self.rear
        self.rear.last = self.head
        # cache stores the keys mapped to the nodes of the double linked list
        self.cache = {}
        # size stores the maximum number of key value pairs the cache can hold
        self.size = size
        # elements stores the number of elements in the cache
        self.elements = 0

    # helper function to add node to the double linked list (rear holds the most recently used node)
    def add(self, node):
        node.next = self.rear
        node.last = self.rear.last
        self.rear.last.next = node
        self.rear.last = node

    # helper function to remove node to the double linked list (not deleted, but connection broken)
    def remove(self, node):
        node.last.next = node.next
        node.next.last = node.last
        node.next = None
        node.last = None

    # get: finds the value mapped to the key, returns None if key not present
    def get(self, key):
        # key not present
        if key not in self.cache:
            return None

        # the node pointed by the key is pushed to the end (most recently used)
        node = self.cache[key]
        self.remove(node)
        self.add(node)

        # the value of the node is returned
        return node.val

    # set: takes a key value pair and stores them
    def set(self, key, val):
        # if the cache is full, the least recently used key value pair (at the head of the linked list) is deleted
        if self.size == self.elements:
            node = self.head.next
            self.remove(node)
            self.elements -= 1
            del self.cache[node.key]

        # adding the new node to the linked list and cache and incrementing elements
        node = Node(key, val)
        self.add(node)
        self.elements += 1
        self.cache[key] = node


# DRIVER CODE
cache = LRU_Cache(3)

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
