"""
Problem:

Implement an autocomplete system. That is, given a query string s and a set of all
possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return
[deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up
queries.
"""

from typing import List

from DataStructures.Trie import Trie


def get_suggestion(word_list: List[str], prefix: str) -> List[str]:
    # using trie data structure to get the suggestions (for deatils, check
    # ./DataStructres/Trie)
    trie = Trie()
    trie.add_words(word_list)
    prefix_match = trie.get_suggestions(prefix)
    # type casting the result to list as the return type is a set
    return list(prefix_match)


if __name__ == "__main__":
    print(get_suggestion(["deer", "dog", "deal"], "de"))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
[n = total number of characters (all words)]
"""
