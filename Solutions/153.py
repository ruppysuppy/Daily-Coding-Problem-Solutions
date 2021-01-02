"""
Problem:

Find an efficient algorithm to find the smallest distance (measured in number of words)
between any two given words in a string.

For example, given words "hello", and "world" and a text content of "dog cat hello cat
dog dog hello cat world", return 1 because there's only one word "cat" in between the
two words.
"""


def calculate_distance(text: str, word1: str, word2: str) -> int:
    word_list = text.split()
    length = len(word_list)
    distance, position, last_match = None, None, None
    # searching for the smallest distance
    for i in range(length):
        if word_list[i] in (word1, word2):
            if last_match in (word_list[i], None):
                last_match = word_list[i]
                position = i
                continue
            current_distance = i - position - 1
            last_match = word_list[i]
            position = i
            if distance == None:
                distance = current_distance
            else:
                distance = min(distance, current_distance)
    return distance


if __name__ == "__main__":
    print(
        calculate_distance(
            "dog cat hello cat dog dog hello cat world", "hello", "world"
        )
    )
    print(
        calculate_distance("dog cat hello cat dog dog hello cat world", "world", "dog")
    )
    print(calculate_distance("hello world", "hello", "world"))
    print(calculate_distance("hello", "hello", "world"))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
