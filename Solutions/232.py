"""
Problem:

Implement a PrefixMapSum class with the following methods:
* insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value. 
* sum(prefix: str): Return the sum of all values of keys that begin with a given prefix. 

For example, you should be able to run the following code:
>>> mapsum.insert("columnar", 3)
>>> assert mapsum.sum("col") == 3
>>> mapsum.insert("column", 2)
>>> assert mapsum.sum("col") == 5
"""

from DataStructures.Trie import Trie


class PrefixMapSum:
    def __init__(self):
        self.trie = Trie()
        self.hash_map = {}

    def insert(self, key, value):
        if key not in self.hash_map:
            self.trie.add(key)
        self.hash_map[key] = value

    def sum(self, prefix):
        words = self.trie.get_suggestions(prefix)
        result = 0
        for word in words:
            result += self.hash_map[word]
        return result


# DRIVER CODE
mapsum = PrefixMapSum()

mapsum.insert("columnar", 3)
print(mapsum.sum("col"))

mapsum.insert("column", 2)
print(mapsum.sum("col"))
