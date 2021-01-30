"""
Problem:

Given a list of words, determine whether the words can be chained to form a circle. A
word X can be placed in front of another word Y in a circle if the last character of X
is same as the first character of Y.

For example, the words ['chair', 'height', 'racket', 'touch', 'tunic'] can form the
following circle: chair -> racket -> touch -> height -> tunic -> chair.
"""


from typing import Dict, List, Set


def check_circle_formation_helper(
    word_list: List[str],
    start: Dict[str, Set[str]],
    end: Dict[str, Set[str]],
    curr: str,
    start_word: str,
    seen: Set[str],
) -> bool:
    if len(seen) == len(word_list):
        if start_word[0] == curr[-1]:
            return True
        return False
    try:
        for word in start[curr[-1]]:
            if word not in seen:
                seen_copy = seen.copy()
                seen_copy.add(word)
                if check_circle_formation_helper(
                    word_list, start, end, word, start_word, seen_copy
                ):
                    return True
    except KeyError:
        # the current word's last character isn't present in start dictionary
        pass
    return False


def check_circle_formation(word_list: List[str]) -> bool:
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


if __name__ == "__main__":
    print(
        check_circle_formation(["chair", "height", "racket", "touch", "tunic"])
    )  # chair, racket, touch, height, tunic, chair
    print(
        check_circle_formation(["height", "racket", "touch", "tunic", "car"])
    )  # racket, touch, height, tunic, car, racket
    print(
        check_circle_formation(["height", "racket", "touch", "tunic"])
    )  # racket, touch, height, tunic (no looping even though there is a chain)
    print(
        check_circle_formation(["height", "racket", "touch", "tunic", "cat"])
    )  # no looping


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n)
"""
