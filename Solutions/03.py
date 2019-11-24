'''
Problem:

Write a program to serialize a tree into a string and deserialize a string into a tree.
'''

# Local Import from the datastructure module

from DataStructures.Tree import Node, Binary_Tree

class Node_modified(Node):
    '''
    Modified Node Class to add the serialize_helper
    
    Functions:
    serialize_helper: Serializes the tree using prefix traversal
    '''

    # Initialize function (uses the Node init)
    def __init__(self, val, left=None, right=None):
        Node.__init__(self, val, left, right)
    
    # Function to serialize the tree (uses prefix traversal and stores the Empty Nodes (None) too)
    def serialize_helper(self):
        if (self.right == None and self.left == None):
            return f"'{self.val}','None','None'"
        elif (self.left != None and self.right == None):
            return f"'{self.val}',{self.left.serialize_helper()},'None'"
        elif (self.left == None and self.right != None):
            return f"'{self.val}','None',{self.left.serialize_helper()}"
        elif (self.left != None and self.right != None):
            return f"'{self.val}',{self.left.serialize_helper()},{self.right.serialize_helper()}"

class Binary_Tree_modified(Binary_Tree):
    '''
    Modified Binary Tree Class to add the serialize function
    
    Functions:
    serialize: Serializes the tree using serialize_helper from the Node_modified Class
    '''

    # Initialize function (uses the Binary_Tree init)
    def __init__(self):
        Binary_Tree.__init__(self)
    
    # Function to serialize the tree (uses serialize_helper)
    def serialize(self):
        return self.root.serialize_helper()

# Function to deserialize the string
def deserialize_helper(node, data): # 'data' is a queue as in prefix traversal the nodes can be easily deserialized using a queue (Reason in next line)
    # The 1st node is the root, 2nd the left child, 3rd, left.left ... till a NULL Node is met (That's why the NULL Node is also stored in the serialize function)
    # In Case of a NULL Node, we backtrack and add the right child of the leaf's parent, backtrack again go to leaf's parent's parent's right child
    # This way the entire tree is generated from the extreme left
    # NOTE: We could also use postfix notation and a stack to accomplish this task (in that case the tree would be generated from extreme right)

    left = data.pop(0).strip("'") # stripping the (')s which denote the data

    if (left == 'None'):
        node.left = None # Storing the left node (in case of NULL), though not mandatory as default value is 'None'
    else:
        node.left = Node_modified(left) # Creating a new node (in case it has a valid value)
        node.left = deserialize_helper(node.left, data) # Recusively calling the function on the left node
        
    right = data.pop(0).strip("'") # stripping the (')s which denote the data
    
    if (right == 'None'):
        node.right = None # Storing the right node (in case of NULL), though not mandatory as default value is 'None'
    else:
        node.right = Node_modified(right) # Creating a new node (in case it has a valid value)
        node.right = deserialize_helper(node.right, data) # Recusively calling the function on the right node
        
    return node

# Function to deserialize the string using deserialize_helper
def deserialize(string):
    data = string.split(',') # Spliting along the delimiter ','
    tree = Binary_Tree_modified() # Creating a empty tree
    tree.root = Node_modified(data.pop(0).strip("'")) # Adding the root

    deserialize_helper(tree.root, data) # Recursive function to generate the entire tree
    
    return tree

# DRIVER CODE
tree = Binary_Tree_modified()
tree.root = Node_modified("root")
tree.root.left = Node_modified("left")
tree.root.right = Node_modified("right")
tree.root.left.left = Node_modified("left.left")

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