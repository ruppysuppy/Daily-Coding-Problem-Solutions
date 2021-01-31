"""
Problem:

Given a set of characters C and an integer k, a De Bruijn sequence is a cyclic sequence
in which every possible k-length string of characters in C occurs exactly once.

For example, suppose C = {0, 1} and k = 3. Then our sequence should contain the
substrings {'000', '001', '010', '011', '100', '101', '110', '111'}, and one possible
solution would be 00010111.

Create an algorithm that finds a De Bruijn sequence.
"""

from typing import List, Set


def generate_all_combinations(
    characters: Set[str], size: int, accumulator: List[str]
) -> None:
    if not accumulator:
        accumulator.extend(characters)
        size -= 1
    while size > 0:
        updated_acc = []
        for _ in range(len(accumulator)):
            temp = accumulator.pop(0)
            for char in characters:
                updated_acc.append(temp + char)
        size -= 1
        accumulator.extend(updated_acc)


def get_de_bruijn_helper(
    characters: Set[str], combinations_set: Set[str], k: int, context: str = ""
) -> Set[str]:
    if not combinations_set:
        return set([context])

    dseqs = set()
    if not context:
        # if context is empty, it is initized using a combination
        for combo in combinations_set:
            child_dseqs = get_de_bruijn_helper(
                characters, combinations_set - set([combo]), k, combo
            )
            dseqs |= child_dseqs
        return dseqs

    for character in characters:
        combo = context[-(k - 1) :] + character
        if combo in combinations_set:
            child_dseqs = get_de_bruijn_helper(
                characters, combinations_set - set([combo]), k, context + character
            )
            dseqs |= child_dseqs
    return dseqs


def get_de_bruijn(characters: Set[str], k: int) -> Set[str]:
    combinations_list = []
    generate_all_combinations(characters, k, combinations_list)
    combinations_set = set(combinations_list)
    return get_de_bruijn_helper(characters, combinations_set, k)


if __name__ == "__main__":
    print(get_de_bruijn({"0", "1"}, 3))


"""
SPECS:

TIME COMPLEXITY: O(n ^ k)
SPACE COMPLEXITY: O(n + k)
"""
