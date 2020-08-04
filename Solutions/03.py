'''
Problem:

Write a program to serialize a tree into a string and deserialize a string into a tree.
'''

# Local Import from the datastructure module

from DataStructures.Tree import Node, BinaryTree


# Helper function to serialize the tree (uses prefix traversal)
# data is padded with single quotes (') and comma (,) is used as a delimiter
def serialize_helper(self):
    if self.right is None and self.left is None:
        return f"'{self.val}','None','None'"
    elif self.left is not None and self.right is None:
        return f"'{self.val}',{self.left.serialize_helper()},'None'"
    elif self.left is None and self.right is not None:
        return f"'{self.val}','None',{self.left.serialize_helper()}"
    elif self.left is not None and self.right is not None:
        return (
            f"'{self.val}'," +
            f"{self.left.serialize_helper()}," +
            f"{self.right.serialize_helper()}"
            )


# Function to serialize the tree
def serialize(self):
    return self.root.serialize_helper()


# adding serialization fctions to node and tree
setattr(Node, 'serialize_helper', serialize_helper)
setattr(BinaryTree, 'serialize', serialize)


# Function to deserialize the string
def deserialize_helper(node, data):
    # data is a queue containing the data as a prefix notation can be easily decoded
    # using a queue
    left = data.pop(0).strip("'")
    if left != 'None':
        # if the left child exists, its added to the tree and deserialize_helper called
        node.left = Node(left)
        node.left = deserialize_helper(node.left, data)

    right = data.pop(0).strip("'")
    if right != 'None':
        # if the right child exists, its added to the tree and deserialize_helper
        # called
        node.right = Node(right)
        node.right = deserialize_helper(node.right, data)
    return node


# Function to deserialize a string into a binary tree
def deserialize(string):
    # the string is considered to have the same format as the binary tree serialization
    # eg: data is padded with single quotes (') and comma (,) is used as a delimiter
    data = string.split(',')
    tree = BinaryTree()
    tree.root = Node(data.pop(0).strip("'"))
    deserialize_helper(tree.root, data)
    return tree


# DRIVER CODE
tree = BinaryTree()
tree.root = Node("root")
tree.root.left = Node("left")
tree.root.right = Node("right")
tree.root.left.left = Node("left.left")

print(tree.serialize())

generated_tree = deserialize("'root','left','left.left','None','None','None','right','None','None'")

print(generated_tree.serialize())


'''
SPECS:

SERIALIZE: (n = Number of Nodes)
TIME COMPLEXITY: O(n) 
SPACE COMPLEXITY: O(n)

DESERIALIZE: (n = Number of Characters in the string)
TIME COMPLEXITY: O(n) 
SPACE COMPLEXITY: O(n)
'''
