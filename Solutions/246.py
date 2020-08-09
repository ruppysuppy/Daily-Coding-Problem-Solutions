"""
Problem:

Given a list of words, determine whether the words can be chained to form a circle.
A word X can be placed in front of another word Y in a circle if the last character of X is same as the first character of Y.

Example:

Input = ['chair', 'height', 'racket', 'touch', 'tunic']
Output = True (chair -> racket -> touch -> height -> tunic -> chair)
"""


def check_circle_formation_helper(word_list, start, end, curr, start_word, seen):
    # checking if all words have been used
    if len(seen) == len(word_list):
        # checking if a cycle is formed
        if start_word[0] == curr[-1]:
            return True
        return False
    try:
        # iterating over all possible words from the current word
        for word in start[curr[-1]]:
            if word not in seen:
                seen_copy = seen.copy()
                seen_copy.add(word)
                # checking if a cycle can be formed
                if check_circle_formation_helper(
                    word_list, start, end, word, start_word, seen_copy
                ):
                    return True
    except KeyError:  # incase the current word's last character isn't present in start
        pass
    return False


def check_circle_formation(word_list):
    # generating the start and end maps
    start = {}
    end = {}
    for word in word_list:
        if word[0] not in start:
            start[word[0]] = set()
        start[word[0]].add(word)
        if word[-1] not in end:
            end[word[-1]] = set()
        end[word[-1]].add(word)
    # starting with all words and checking if a circle can be formed
    for word in word_list:
        if check_circle_formation_helper(
            word_list, start, end, word, word, set([word])
        ):
            return True
    return False


# DRIVER CODE
print(
    check_circle_formation(["chair", "height", "racket", "touch", "tunic"])
)  # chair, racket, touch, height, tunic, chair
print(
    check_circle_formation(["height", "racket", "touch", "tunic", "car"])
)  # racket, touch, height, tunic, car, racket
print(
    check_circle_formation(["height", "racket", "touch", "tunic"])
)  # racket, touch, height, tunic (but no looping)
print(
    check_circle_formation(["height", "racket", "touch", "tunic", "cat"])
)  # no looping
