class Graph_Undirected_Unweighted:
    '''
    Graph Undirected Unweighted Class

    Functions:
    add_node: function to add a node in the graph
    add_edge: function to add an edge between 2 nodes in the graph
    '''

    # Initialize function (Automatically called upon creating an object instance)
    def __init__(self):
        self.connections = {}
        self.nodes = 0
        
    # String function (Automatically called upon converting to string, generally used when printing)
    def __str__(self):
        return str(self.connections)
        
    # Length function (Automatically called upon calling len())
    def __len__(self):
        return self.nodes
    
    def add_node(self, node):
        # Function to add a node in the graph if it is not in the graph
        if (node not in self.connections):
            self.connections[node] = set()
            self.nodes += 1
    
    def add_edge(self, node1, node2):
        # Function to add an edge between 2 nodes in the graph
        self.add_node(node1)
        self.add_node(node2)
        
        self.connections[node1].add(node2)
        self.connections[node2].add(node1)