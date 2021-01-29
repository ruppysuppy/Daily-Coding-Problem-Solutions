"""
Problem:

Given a string with repeated characters, rearrange the string so that no two adjacent
characters are the same. If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", return None.
"""

from typing import Optional

from DataStructures.Queue import Queue


def get_unique_adjacent(string: str) -> Optional[str]:
    length = len(string)
    freq = {}
    if length == 0:
        return string

    for i in range(length):
        if string[i] not in freq:
            freq[string[i]] = 0
        freq[string[i]] += 1

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    queue = Queue()
    [queue.enqueue(item) for item in sorted_freq]
    result = ""

    if length % 2 == 0 and sorted_freq[0][1] > length // 2:
        return None
    elif length % 2 == 1 and sorted_freq[0][1] > (length // 2) + 1:
        return None

    while not queue.is_empty():
        if len(queue) == 1:
            elem, freq = queue.peek()
            if freq == 2:
                result = elem + result + elem
                break
            elif freq == 1:
                if result[-1] != elem:
                    result += elem
                else:
                    result = elem + result
                break
            return None

        elem1, freq1 = queue.peek()
        elem2, freq2 = None, None
        if len(queue) > 1:
            elem2, freq2 = queue[1]

        result += elem1 + elem2

        queue[0] = elem1, freq1 - 1
        if len(queue) > 1:
            queue[1] = elem2, freq2 - 1
        if len(queue) > 1 and queue[1][1] == 0:
            queue.dequeue()
        if len(queue) > 0 and queue[0][1] == 0:
            queue.dequeue()
    return result


if __name__ == "__main__":
    print(get_unique_adjacent("aaabbc"))
    print(get_unique_adjacent("aaabbcc"))
    print(get_unique_adjacent("aaabbac"))
    print(get_unique_adjacent("aaab"))
    print(get_unique_adjacent("aaabbaa"))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
