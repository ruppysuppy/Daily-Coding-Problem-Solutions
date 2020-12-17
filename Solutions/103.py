"""
Problem:

Given a string and a set of characters, return the shortest substring containing all
the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you
should return "aeci".

If there is no substring containing all the characters in the set, return null.
"""

from typing import Set


def shortest_substring_with_all_characters(string: str, characters: Set[str]) -> str:
    curr_char_queue, index_queue = [], []
    curr_seen = set()
    num_char = len(characters)
    result = None
    # generating the shortest substring
    for i in range(len(string)):
        if string[i] in characters:
            curr_char_queue.append(string[i])
            index_queue.append(i)
            curr_seen.add(string[i])
        # shortening the substring
        shift = 0
        for k in range(len(curr_char_queue) // 2):
            if curr_char_queue[k] == curr_char_queue[-k - 1]:
                shift += 1
        # truncating the queues
        curr_char_queue = curr_char_queue[shift:]
        index_queue = index_queue[shift:]
        # all characters found
        if len(curr_seen) == num_char:
            if (not result) or (len(result) > (index_queue[-1] - index_queue[0] + 1)):
                result = string[index_queue[0] : index_queue[-1] + 1]
    return result


if __name__ == "__main__":
    print(shortest_substring_with_all_characters("abcdedbc", {"g", "f"}))
    print(shortest_substring_with_all_characters("abccbbbccbcb", {"a", "b", "c"}))
    print(shortest_substring_with_all_characters("figehaeci", {"a", "e", "i"}))
    print(shortest_substring_with_all_characters("abcdedbc", {"d", "b", "b"}))
    print(shortest_substring_with_all_characters("abcdedbc", {"b", "c"}))
    print(shortest_substring_with_all_characters("abcdecdb", {"b", "c"}))
    print(shortest_substring_with_all_characters("abcdecdb", {"b", "c", "e"}))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n)
"""
