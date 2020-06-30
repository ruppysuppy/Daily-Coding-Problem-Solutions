class Node():
    '''
    Node Class for the nodes of a Pre-processing Trie
    '''

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    '''
    Pre-processing Trie Class

    Functions:
    add: function to add nodes to a trie instance
    add_words: add a list of words to a trie instance
    get_suggestions: gets all possible words from the given prefix
    _traverse: helper function for get_suggestions to generate the words
    '''

    def __init__(self):
        self.root = Node()
    
    def add(self, word):
        pos = self.root

        for char in word:
            if (char not in pos.children):
                pos.children[char] = Node()
            
            pos = pos.children[char]
        
        pos.is_end = True
    
    def add_words(self, word_list):
        for word in word_list:
            self.add(word)
    
    def _traverse(self, pos, curr, res):
        if (pos.is_end):
            res.add(curr)
        
        for child in pos.children:
            self._traverse(pos.children[child], curr + child, res)
    
    def get_suggestions(self, prefix):
        pos = self.root

        for char in prefix:
            if (char not in pos.children):
                return []
            pos = pos.children[char]
        
        res = set()
        self._traverse(pos, prefix, res)

        return res
