from typing import List, Optional


class TrieNode:
    """
    TrieNode Class for the nodes of a Pre-processing Trie
    """

    def __init__(self) -> None:
        self.children = {}
        self.is_end = False


class Trie:
    """
    Pre-processing Trie Class

    Functions:
    add: Add a string to the Trie
    add_words: Add a list of strings to the Trie
    get_suggestions: Get all possible words from the given prefix
    _traverse: Helper function for get_suggestions (generates the words from prefix)
    """

    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word: str) -> None:
        # Add a string to the Trie
        pos = self.root
        for char in word:
            if char not in pos.children:
                pos.children[char] = TrieNode()
            pos = pos.children[char]
        pos.is_end = True

    def add_words(self, word_list: List[str]) -> None:
        # Add a list of strings to the Trie
        for word in word_list:
            self.add(word)

    def get_suggestions(self, prefix: str) -> Optional[List[str]]:
        # Get all possible words from the given prefix
        pos = self.root
        for char in prefix:
            if char not in pos.children:
                # returns None if no word is possible from the given prefix
                return None
            pos = pos.children[char]
        result = set()
        self._traverse(pos, prefix, result)
        return result

    def _traverse(self, pos: TrieNode, curr: str, result: set) -> None:
        # Helper function for get_suggestions
        # Generates the words from prefix (using result as the accumulator)
        if pos.is_end:
            result.add(curr)
        for child in pos.children:
            self._traverse(pos.children[child], curr + child, result)
