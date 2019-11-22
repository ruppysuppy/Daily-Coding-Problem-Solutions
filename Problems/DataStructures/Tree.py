class Node():
    '''
    Node Class for the nodes of a Binary Tree

    Functions:
    to_str: __str__ helper function
    height_helper: helper function to calculate the height of a Binary Tree
    insert_helper: helper function to add node in a Binary Search Tree
    '''

    # Initialize function (Automatically called upon creating an object instance)
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    # String function (Automatically called upon converting to string, generally used when printing)
    def __str__(self):
        return self.to_str()
    
    def to_str(self):
        # Returns all the childen in case 1 of them is not None, else returns only the value
        if (self.right == None and self.left == None):
            return f"('{self.val}')"
        elif (self.left != None and self.right == None):
            return f"({self.left.to_str()}, '{self.val}', NULL)"
        elif (self.left == None and self.right != None):
            return f"(NULL, '{self.val}', {self.right.to_str()})"
        elif (self.left != None and self.right != None):
            return f"({self.left.to_str()}, '{self.val}', {self.right.to_str()})"
    
    def height_helper(self):
        # Recusive function to find the height of a tree (using max(left_height, right_height))
        if (self.left == None):
            left_height = 0
        else:
            left_height = self.left.height_helper()
        
        if (self.right == None):
            right_height = 0
        else:
            right_height = self.right.height_helper()
        
        return (max(left_height, right_height) + 1)
    
    def insert_helper(self, val):
        # Insertion helper to insert using the BST property
        if (self.val > val):
            if (self.left == None):
                self.left = Node(val)
            else:
                self.left.insert_helper(val)

        elif (self.val < val):
            if (self.right == None):
                self.right = Node(val)
            else:
                self.right.insert_helper(val)

class Binary_Tree():
    '''
    Binary Tree Class

    Functions:
    find_height: function to calculate the height of a Binary Tree (uses height_helper in the Node Class)
    '''

    # Initialize function (Automatically called upon creating an object instance)
    def __init__(self, val=None):
        if (val != None):
            self.root = Node(val)
        else:
            self.root = None
    
    # String function (Automatically called upon converting to string, generally used when printing)
    def __str__(self):
        return str(self.root)
    
    # Function to return the height of the tree using the height helper
    def find_height(self):
        return self.root.height_helper()

class Binary_Search_Tree(Binary_Tree):
    '''
    Binary Tree Class (INHERITS FROM THE Binary_Tree CLASS)

    Functions:
    add: function to add nodes to a Binary Search Tree (uses insert_helper in the Node Class)
    '''

    # Initialize function (uses the Binart_Tree init)
    def __init__(self, val=None):
        Binary_Tree.__init__(val)
    
    # Function to add Nodes using the insert helper
    def add(self, val):
        if (self.root == None):
            self.root = Node(val)
        else:
            self.root.insert_helper(val)