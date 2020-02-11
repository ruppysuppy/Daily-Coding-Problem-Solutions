'''
Problem:

A rule looks like this:
A NE B
This means this means point A is located northeast of point B.

A SW C
means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. 

Example:

A N B
B NE C
C N A
does not validate, since A cannot be both north and south of C.

A NW B
A N B
is considered valid.
'''

# global vaiable to store the opposites
OPPOSITES = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

# node class (stores the neighbours)
class Node():
    # initialization
    def __init__(self, val):
        self.val = val
        self.neighbours = {'N': set(), 'E': set(), 'S': set(), 'W': set()}
    
    # representation function
    def __repr__(self):
        return f'{self.val}'
    
    # equality condition (operation overloading)
    def __eq__(self, other):
        if (type(other) == Node):
            return (self.val == other.val)
        elif (type(other) == str):
            return (self.val == other)
        else:
            return False
    
    # defining the hash function as its needed in Map class
    def __hash__(self):
        return hash(self.val)

# map class
class Map():
    # initialization
    def __init__(self):
        self.nodes = {}
    
    # FUNCTION TO PERFORM THE OPERATION
    def add_rule(self, rule):
        # breaking the rule into its components
        node1, direction, node2 = rule.split()

        # creating the node
        node1 = Node(node1)
        node2 = Node(node2)

        # cheking for the existance of node1
        if (node1 not in self.nodes):
            self.nodes[node1.val] = node1
        else:
            node1 = self.nodes[node1.val]
        
        # cheking for the existance of node2
        if (node2 not in self.nodes):
            self.nodes[node2.val] = node2
        else:
            node2 = self.nodes[node2.val]
        
        # for each character in direction, the neighbours are updated recursively
        for char in direction:
            # if the node is not valid, RuntimeError is raised
            if ((node1 in node2.neighbours[char]) or (node2 in node1.neighbours[OPPOSITES[char]])):
                raise RuntimeError

            # recursive calling for all neighbours
            for node in node1.neighbours[char]:
                self.add_rule(f'{node} {char} {node2}')
        
        # adding the rule to the calling node
        for char in direction:
            node2.neighbours[char].add(node1)
            node1.neighbours[OPPOSITES[char]].add(node2)

# DRIVER CODE
m = Map()

m.add_rule('A N B')
print('Rule Applied!')
m.add_rule('B NE C')
print('Rule Applied!')

try:
    m.add_rule('C N A')
except RuntimeError:
    print("Invalid Rule!")