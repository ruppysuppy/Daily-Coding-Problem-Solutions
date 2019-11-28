'''
Problem:

Implement an autocomplete system. 
That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

Example:
['dog', 'deer', 'deal'], 'de' => [deer, deal]
'''

# Node class for the Trie Structure
class Node():
    def __init__(self, ):
        self.children = {}
        self.end = False

# Trie Structure
class Trie():
    # Initialize
    def __init__(self):
        self.root = Node()
    
    # Adding a string to the Trie
    def add(self, string):
        # Starting from the root
        node = self.root

        # Traversing and Creating new nodes as required
        for i in string:
            # If the the node exists moving the pointer to the location
            if (i in node.children):
                node = node.children[i]

            # Creating a new node in case it doesn't exist
            else:
                node.children[i] = Node()
                node = node.children[i]
        
        # Placing flag to indicate end of a word
        node.end = True
    
    # Function to generate the trie from the given words
    def form_trie(self, keys):
        for key in keys:
            self.add(key)
    
    # Suggestion function (Uses suggestion helper)
    def suggestion(self, prefix):
        pos = self.root
        word = prefix
        word_list = []

        # Traversing to the desired position (end of prefix)
        for i in prefix:
            # If the prefix doesn't exist, empty list is returned
            if (i not in pos.children):
                return word_list
            pos = pos.children[i]
        
        # Calling Suggestion helper to traverse the Trie and return suggestions
        return self.suggestion_helper(pos, word, word_list)

    # Recursive helper function    
    def suggestion_helper(self, node, word, word_list):
        # If it is the end of a word (determined using the flag), the word is added to the list
        if (node.end == True):
            word_list.append(word)
        
        # For all characters in the node, suggestion helper is called recursively to generate the list of words
        for i in node.children:
            word_list = self.suggestion_helper(node.children[i], word+i, word_list)

        return word_list

# FUNCTION TO PERFORM THE OPERATION
def get_suggestion(word_list, prefix):
    # Creating the Trie Object
    trie = Trie()

    # Generating the Trie
    trie.form_trie(word_list)

    # Getting the suggestions
    List = trie.suggestion(prefix)

    return List

# DRIVER CODE
print(get_suggestion(['deer', 'dog', 'deal'], 'de'))