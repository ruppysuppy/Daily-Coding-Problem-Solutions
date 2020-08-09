"""
Problem:

Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.
Design a binary tree node class with the following methods:
is_locked: which returns whether the node is locked
lock: which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
unlock: which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like. 
You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. 
Each method should run in O(h), where h is the height of the tree.
"""

from DataStructures.Tree import Node, Binary_Tree

# Modified Node Class
class Node_modified(Node):
    # Initialize function (Automatically called upon creating an object instance)
    def __init__(self, val):
        """
        Node Class for the nodes of a Binary Tree

        Functions:
        to_str: __str__ helper function
        height_helper: helper function to calculate the height of a Binary Tree
        insert_helper: helper function to add node in a Binary Search Tree
        """

        Node.__init__(self, val)
        self.locked = False
        self.parent = None

    # String function (Automatically called upon converting to string, generally used when printing)
    def __str__(self):
        return f"Value: {self.val}\nStatus: {'Locked' if self.locked else 'Unlocked'}"

    # FUNCTION TO PERFORM THE OPERATION (is locked)
    def is_locked(self):
        return self.locked

    # Helper function to check if any of the descendant is not locked
    def check_descendant_helper(self):
        # If an unlocked node is found, True is returned
        if not self.locked:
            return True

        # If the immediate children doesn't contain any unlocked node, the function is called recursively to traverse the subtrees
        else:
            if self.left:
                left = self.left.check_descendant_helper()
            else:
                left = False

            if self.right and not self.left:
                right = self.right.check_descendant_helper()
            else:
                right = False

            # If any of the subtree contain an unlocked node, the value becomes True (left or right)
            return left or right

    # FUNCTION TO PERFORM THE OPERATION (lock)
    def lock(self):
        flag = False
        node = self

        # Searching for an unlocked parent node
        while node.parent:
            if not node.is_locked():
                flag = True
                break
            node = node.parent
        # If no parent is unlocked, then an unlocked child node is searched
        else:
            if (self.left and self.left.check_descendant_helper()) or (
                self.right and self.right.check_descendant_helper()
            ):
                flag = True

        # If any unlocked node is found, after performing the action (swapping the locked variable) True is returned
        if flag:
            self.locked = True
            return True

        return False

    # FUNCTION TO PERFORM THE OPERATION (unlock)
    def unlock(self):
        flag = False
        node = self

        # Searching for an unlocked parent node
        while node.parent:
            if not node.is_locked():
                flag = True
                break
            node = node.parent
        # If no parent is unlocked, then an unlocked child node is searched
        else:
            if (self.left and self.left.check_descendant_helper()) or (
                self.right and self.right.check_descendant_helper()
            ):
                flag = True

        # If any unlocked node is found, after performing the action (swapping the locked variable) True is returned
        if flag:
            self.locked = False
            return True

        return False

    # Helper function to print all nodes (Recursively - Inplace)
    def to_str(self):
        if self.left:
            self.left.to_str()

        print(f"\n{self}\n")

        if self.right:
            self.right.to_str()


# Modified Binary Tree Class
class Binary_Tree_modified:
    # String function (Automatically called upon converting to string, generally used when printing)
    def __init__(self):
        self.root = None

    # Helper function to print all nodes (Uses helper function in Node_modified)
    def to_str(self):
        self.root.to_str()


# DRIVER CODE
tree = Binary_Tree_modified()
tree.root = Node_modified(5)
tree.root.left = Node_modified(3)
tree.root.left.parent = tree.root
tree.root.right = Node_modified(18)
tree.root.right.parent = tree.root
tree.root.left.left = Node_modified(0)
tree.root.left.left.parent = tree.root.left

tree.to_str()

print(tree.root.left.left.lock())
print(tree.root.left.lock())
print(tree.root.lock())
print(tree.root.left.unlock())

tree.to_str()
