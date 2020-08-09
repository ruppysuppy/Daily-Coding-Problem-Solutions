"""
Problem:

Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same. 
If this is not possible, return None.

Example:

Input = "aaabbc"
Output = "ababac"

Input = "aaab"
Output = None
"""


def get_unique_adjacent(string):
    length = len(string)
    freq = {}

    if length == 0:
        return string

    # getting the character frequency
    for i in range(length):
        if string[i] in freq:
            freq[string[i]] += 1
        else:
            freq[string[i]] = 1

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    queue = list(sorted_freq)

    # checking if a desired string can be formed
    if length % 2 == 0:
        if sorted_freq[0][1] > length // 2:
            return None
    else:
        if sorted_freq[0][1] > (length // 2) + 1:
            return None

    res = ""

    # creating the required string
    while queue:
        if len(queue) == 1:
            if queue[0][1] == 2:
                res = queue[0][0] + res + queue[0][0]
                break
            elif queue[0][1] == 1:
                if res[-1] != queue[0][0]:
                    res += queue[0][0]
                else:
                    res = queue[0][0] + res
                break
            else:
                return None

        res += queue[0][0] + queue[1][0]

        queue[0] = queue[0][0], queue[0][1] - 1
        queue[1] = queue[1][0], queue[1][1] - 1

        if len(queue) > 1 and queue[1][1] == 0:
            queue.pop(1)
        if len(queue) > 0 and queue[0][1] == 0:
            queue.pop(0)

    return res


# DRIVER CODE
print(get_unique_adjacent("aaabbc"))
print(get_unique_adjacent("aaabbcc"))
print(get_unique_adjacent("aaabbac"))

# cannot form a word of the desired form
print(get_unique_adjacent("aaab"))
print(get_unique_adjacent("aaabbaa"))
