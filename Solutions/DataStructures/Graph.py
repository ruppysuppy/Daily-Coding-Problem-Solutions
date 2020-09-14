from typing import Union


class GraphUndirectedUnweighted:
    """
    Graph Undirected Unweighted Class

    Functions:
    add_node: function to add a node in the graph
    add_edge: function to add an edge between 2 nodes in the graph
    """

    def __init__(self) -> None:
        self.connections = {}
        self.nodes = 0

    def __repr__(self) -> str:
        return str(self.connections)

    def __len__(self) -> int:
        return self.nodes

    def add_node(self, node: Union[int, str]) -> None:
        # Add a node in the graph if it is not in the graph
        if node not in self.connections:
            self.connections[node] = set()
            self.nodes += 1

    def add_edge(self, node1: Union[int, str], node2: Union[int, str]) -> None:
        # Add an edge between 2 nodes in the graph
        self.add_node(node1)
        self.add_node(node2)
        self.connections[node1].add(node2)
        self.connections[node2].add(node1)


class GraphDirectedUnweighted:
    """
    Graph Directed Unweighted Class

    Functions:
    add_node: function to add a node in the graph
    add_edge: function to add an edge between 2 nodes in the graph
    """

    def __init__(self) -> None:
        self.connections = {}
        self.nodes = 0

    def __repr__(self) -> str:
        return str(self.connections)

    def __len__(self) -> int:
        return self.nodes

    def add_node(self, node: Union[int, str]) -> None:
        # Add a node in the graph if it is not in the graph
        if node not in self.connections:
            self.connections[node] = set()
            self.nodes += 1

    def add_edge(self, node1: Union[int, str], node2: Union[int, str]) -> None:
        # Add an edge between 2 nodes in the graph
        self.add_node(node1)
        self.add_node(node2)
        self.connections[node1].add(node2)


class GraphUndirectedWeighted:
    """
    Graph Undirected Weighted Class

    Functions:
    add_node: function to add a node in the graph
    add_edge: function to add an edge between 2 nodes in the graph
    """

    def __init__(self) -> None:
        self.connections = {}
        self.nodes = 0

    def __repr__(self) -> str:
        return str(self.connections)

    def __len__(self) -> int:
        return self.nodes

    def add_node(self, node: Union[int, str]) -> None:
        # Add a node in the graph if it is not in the graph
        if node not in self.connections:
            self.connections[node] = {}
            self.nodes += 1

    def add_edge(
        self, node1: Union[int, str], node2: Union[int, str], weight: int
    ) -> None:
        # Add an edge between 2 nodes in the graph
        self.add_node(node1)
        self.add_node(node2)
        self.connections[node1][node2] = weight
        self.connections[node2][node1] = weight


class GraphDirectedWeighted:
    """
    Graph Directed Weighted Class

    Functions:
    add_node: function to add a node in the graph
    add_edge: function to add an edge between 2 nodes in the graph
    """

    def __init__(self) -> None:
        self.connections = {}
        self.nodes = 0

    def __repr__(self) -> str:
        return str(self.connections)

    def __len__(self) -> int:
        return self.nodes

    def add_node(self, node: Union[int, str]) -> None:
        # Add a node in the graph if it is not in the graph
        if node not in self.connections:
            self.connections[node] = {}
            self.nodes += 1

    def add_edge(
        self, node1: Union[int, str], node2: Union[int, str], weight: int
    ) -> None:
        # Add an edge between 2 nodes in the graph
        self.add_node(node1)
        self.add_node(node2)
        self.connections[node1][node2] = weight
