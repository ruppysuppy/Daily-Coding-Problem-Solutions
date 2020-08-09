"""
Problem:

Given a binary tree, return the level of the tree with minimum sum.
"""

# local import from the DataStructures module
from DataStructures.Queue import Queue
from DataStructures.Tree import Binary_Tree, Node

# FUNCTION TO PERFROM THE OPERATION
def get_min_sum(tree):
    # if the tree is empty, 0 is returned
    if not tree.root:
        return 0

    # creating a queue
    queue_processing = Queue()
    # adding the root node in the queue
    queue_processing.enqueue(tree.root)
    # adding a None to demarkate the end of a level
    queue_processing.enqueue(None)

    # setting the min_sum (stores the minimum sum of all the levels of the tree) to a high number (sys.maxsize preferably)
    min_sum = 99999
    # temp_sum stores the sum of the current level
    temp_sum = 0

    # processing all the nodes (till the queue is empty)
    while not queue_processing.isEmpty():
        # getting the current node
        node = queue_processing.dequeue()

        # if the node is not None
        if node:
            # the children of the node are added to the queue
            if node.left:
                queue_processing.enqueue(node.left)
            if node.right:
                queue_processing.enqueue(node.right)

            # the node's value is added to temp_sum
            temp_sum += node.val

        # if the node is None (end of a level)
        else:
            # if the level's sum is less than the min_sum, min_sum is updated
            if temp_sum < min_sum:
                min_sum = temp_sum

            # if the queue has any elements, another None is added to demarkate the end of the current level
            # length checking is necessary as if all the nodes are processed, it will keep adding Nones and the loop will go on infinitely
            if len(queue_processing) > 0:
                queue_processing.enqueue(None)
                temp_sum = 0

    # min_sum is returned
    return min_sum


# DRIVER CODE
a = Node(100)
b = Node(200)
c = Node(300)
a.left = b
a.right = c

d = Node(400)
e = Node(500)
b.left = d
b.right = e

f = Node(600)
g = Node(700)
c.left = f
c.right = g

h = Node(800)
d.right = h

tree = Binary_Tree()
tree.root = a

print(get_min_sum(tree))
a.val = 1000
print(get_min_sum(tree))
b.val = 1500
print(get_min_sum(tree))
h.val = 2000
print(get_min_sum(tree))
