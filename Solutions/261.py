"""
Problem:

Huffman coding is a method of encoding characters based on their frequency. Each letter
is assigned a variable-length binary string, such as 0101 or 111110, where shorter
lengths correspond to more common letters. To accomplish this, a binary tree is built
such that the path from the root to any leaf uniquely maps to a character. When
traversing the path, descending to a left child corresponds to a 0 in the prefix, while
descending right corresponds to 1.

Here is an example tree (note that only the leaf nodes have letters):

        *
      /   \
    *       *
   / \     / \
  *   a   t   *
 /             \
c               s
With this encoding, cats would be represented as 0000110111.

Given a dictionary of character frequencies, build a Huffman tree, and use it to
determine a mapping between characters and their encoded binary strings.
"""

from typing import Dict, Union

from DataStructures.Tree import Node


def huffman_code_tree(node: Union[Node, str], binString: str = "") -> Dict[str, str]:
    if type(node) is str:
        return {node: binString}
    d = dict()
    d.update(huffman_code_tree(node.left, binString + "0"))
    d.update(huffman_code_tree(node.right, binString + "1"))
    return d


def get_huffman_code(char_freq: Dict[str, int]) -> Dict[str, str]:
    # calculating Huffman code
    nodes = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
    while len(nodes) > 1:
        key1, c1 = nodes[-1]
        key2, c2 = nodes[-2]
        nodes = nodes[:-2]
        node = Node(None, key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    huffmanCode = huffman_code_tree(nodes[0][0])
    return huffmanCode


if __name__ == "__main__":
    print(get_huffman_code({"c": 1, "a": 2, "t": 2, "s": 1}))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
