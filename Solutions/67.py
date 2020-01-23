'''
Problem:

Implement an LFU (Least Frequently Used) cache. 

It should be able to be initialized with a cache size n, and contain the following methods:
* set(key, value): sets key to value. 
If there are already n items in the cache and we are adding a new item, then it should also remove the least frequently used item. 
If there is a tie, then the least recently used key should be removed.
* get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
'''

# node class for the double linked list (in LFU Cache)
class Node():
    # initalize method
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.last = None
        self.next = None
    
    # bollean method
    def __bool__(self):
        return bool(self.key)

# LFU Cache
class LFU_Cache():
    # initalize method
    def __init__(self, size):
        self.head = Node(None, None)
        self.rear = Node(None, None)
        self.head.next = self.rear
        self.rear.last = self.head
        self.cache = {}
        self.size = size
        self.elements = 0
    
    # helper method to add a node to the proper position in the cache linked list
    def add(self, node):
        # inserting the node at head.next
        temp = self.head.next
        self.head.next = node
        node.last = self.head
        temp.last = node
        node.next = temp
        # moving the node at the proper position based on the frequency of use
        self.move_to_pos(node)

    # helper function to move the node to the proper position based on the frequency
    def move_to_pos(self, node):
        while (node.next and node.next.freq <= node.freq):
            node1 = node
            node2 = node.next

            node1.last.next = node2
            node2.last = node1.last

            temp = node2.next
            node2.next = node1
            node1.last = node2
            node1.next = temp
            temp.last = node1

    # helper method to remove a node
    def remove(self, node):
        node.last.next = node.next
        node.next.last = node.last
        node.next = None
        node.last = None
    
    # FUNCTION TO PERFORM THE OPERATION (get)
    def get(self, key):
        # if the key doesn't exist, None is returned
        if (key not in self.cache):
            return None
        
        # incrementing the freq of the accessed node
        node = self.cache[key]
        node.freq += 1
        # moving the node at the proper position based on the frequency of use
        self.move_to_pos(node)
        
        return node.val
    
    # FUNCTION TO PERFORM THE OPERATION (set)
    def set(self, key, val):
        # if the number of elements has reached the max size, the least used element is deleted
        if (self.size == self.elements):
            node = self.head.next
            self.remove(node)
            self.elements -= 1
            del self.cache[node.key]

        # adding new node
        node = Node(key, val)
        self.add(node)
        self.elements += 1
        self.cache[key] = node

# DRIVER CODE
cache = LFU_Cache(3)

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
