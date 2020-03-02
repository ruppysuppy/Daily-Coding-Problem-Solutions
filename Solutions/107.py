'''
Problem:

Print the nodes in a binary tree level-wise. 

Example:

Input =   1
         / \
        2   3
           / \
          4   5
Output = 1, 2, 3, 4, 5
'''

# local import from the DataStructures
from DataStructures.Tree import Binary_Tree, Node

# bfs function to get all the nodes level-wise
def lvl_wise_nodes(self):
    # queue to store the order of processing
    queue = [self.root]
    # ans stores the visited nodes
    ans = []

    # looping till all nodes are processed
    while (queue != []):
        # getting the current node
        pos = queue.pop(0)

        # if the node has a left child, its added to the queue for processing
        if (pos.left != None):
            queue.append(pos.left)
        
        # if the node has a right child, its added to the queue for processing
        if (pos.right != None):
            queue.append(pos.right)
        
        # adding the current node's value to the ans
        ans.append(pos.val)
    
    return ans

# adding the function to the Binary Tree class
setattr(Binary_Tree, 'lvl_wise_nodes', lvl_wise_nodes)

# DRIVER CODE
tree = Binary_Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.right.left = Node(4)
tree.root.right.right = Node(5)

print(f"Tree: {tree}")
print(f"Level wise result: {tree.lvl_wise_nodes()}")