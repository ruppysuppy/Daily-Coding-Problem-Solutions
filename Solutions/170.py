'''
Problem:

You are given a start word, an end word, and a dictionary of valid words.
Find the shortest transformation sequence from start to end such that only one letter is changed at each step of the sequence, and each transformed word exists in the dictionary. 
If there is no possible transformation, return null. Each word in the dictionary have the same length as start and end and is lowercase.

Example:

start = "dog", 
end = "cat",
dictionary = {"dot", "dop", "dat", "cat"}
Output = ["dog", "dot", "dat", "cat"]

start = "dog", 
end = "cat", 
dictionary = {"dot", "tod", "dat", "dar"}
Output = null (as there is no possible transformation from dog to cat)
'''

# function to check if 2 strings differ by exactly 1 charcter
def is_one_diff(s1, s2):
    # getting the lengths of the strings
    len1 = len(s1)
    len2 = len(s2)
    # no_mismatch holds if there is no mismatch between the strings
    no_mismatch = True

    # if the length difference is more than 1, flase is returned as they cannot differ by 1 
    if (len1 != len2):
        if (abs(len1 - len2) > 1):
            return False
        # if the length difference is 1, no_mismatch is nulled as a mismatch has occoured
        no_mismatch = False
    
    # iterating through each set of characters in the strings
    for c1, c2 in zip(s1, s2):
        # if there is a mismatch
        if (c1 != c2):
            # if there was no mismatch previously, no_mismatch is nulled
            if (no_mismatch):
                no_mismatch = False
            # else more than 1 mismatch has occoured and False is returned
            else:
                return False
    
    # if the strings are the same, False is returned
    if (no_mismatch):
        return False
    # if the 2 strings differ by exactly 1 charcter, True is returned
    return True

# undirected graph class
class Graph:
    # initialization
    def __init__(self):
        self.nodes = {}
    
    # function to add a vertex
    def add_vert(self, vert):
        self.nodes[vert] = set()
    
    # function to add an edge between 2 vertices
    def add_edge(self, vert1, vert2):
        # adding the missing vertices
        if (vert1 not in self.nodes):
            self.add_vert(vert1)
        if (vert2 not in self.nodes):
            self.add_vert(vert2)

        # adding the edge
        self.nodes[vert1].add(vert2)
        self.nodes[vert2].add(vert1)
    
    # dfs function to generate a matrix containing all paths from the start word to the search word
    def dfs(self, current, search_elem, visited, sequence, holder_mat):
        # if the search element is reached, the sequence is added to the matrix
        if (current == search_elem):
            sequence.append(current)
            holder_mat.append(sequence)
            return
        
        # the current node is added to the visited set and the current sequence
        visited.add(current)
        sequence.append(current)

        # running dfs for unvisited nodes (recursively)
        for node in self.nodes[current]:
            if (node not in visited):
                self.dfs(node, search_elem, set(visited), list(sequence), holder_mat)
    
    # creating the graph from a list of words
    def create(self, vert_list):
        # getting the length of the list
        length = len(vert_list)

        # checking for every combination of words and adding an edge if they differ by 1 character
        for i in range(length):
            for j in range(i, length):
                if (is_one_diff(vert_list[i], vert_list[j])):
                    self.add_edge(vert_list[i], vert_list[j])

# FUNCTION TO PERFORM THE OPERATION
def min_transform(start, stop, dictionary):
    # adding the start to the dictionary incase its not present
    if (start not in dictionary):
        dictionary.append(start)

    # creating the graph
    graph = Graph()
    graph.create(dictionary)

    # creating the matrix to store the list of traversals
    mat = [] 

    # performing dfs on the graph
    graph.dfs(start, stop, set(), [], mat)

    # if the matrix is empty, there are no paths from the start to the stop words
    if (not mat):
        return None
    
    # getting the shortest sequence from the matrix of sequences
    sequence = None
    length = 99999
    
    for seq in mat:
        if (len(seq) < length):
            sequence = seq
            length = len(seq)
    
    # returning the shortest sequence
    return sequence

# DRIVER CODE
print(min_transform("dog", "cat", ["dot", "dop", "dat", "cat"]))
print(min_transform("dog", "cat", ["dot", "tod", "dat", "dar"]))