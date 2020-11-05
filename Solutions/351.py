"""
Problem:

Word sense disambiguation is the problem of determining which sense a word takes on in
a particular setting, if that word has multiple meanings. For example, in the sentence
"I went to get money from the bank", bank probably means the place where people deposit
money, not the land beside a river or lake.

Suppose you are given a list of meanings for several words, formatted like so:

{
    "word_1": ["meaning one", "meaning two", ...],
    ...
    "word_n": ["meaning one", "meaning two", ...]
}
Given a sentence, most of whose words are contained in the meaning list above, create
an algorithm that determines the likely sense of each possibly ambiguous word.
"""

from typing import Dict, List


def get_meaning(
    sentence: str, meaning_map: Dict[str, List[str]]
) -> Dict[str, List[str]]:
    # this is NOT a fool-proof solution
    # the problem is incomplete
    words = sentence.split()
    words_set = set(words)
    # selecting the words with multiple meanings
    ambiguous_words = [
        word for word in words if word in meaning_map and len(meaning_map[word]) > 1
    ]
    possible_context_meaning_map = {}
    # generating the possible meaning of the words in the given context
    for word in ambiguous_words:
        for meaning in meaning_map[word]:
            for meaning_word in meaning.split():
                if meaning_word in words_set:
                    if word not in possible_context_meaning_map:
                        possible_context_meaning_map[word] = []
                    possible_context_meaning_map[word].append(meaning)
                    break
    return possible_context_meaning_map


if __name__ == "__main__":
    sentence = "I went to get money from the bank"
    meaning_map = {
        "bank": ["place where people deposit money", "land beside a river or lake"],
        "get": ["acquire something"],
        "money": ["medium of exchange"],
        "went": ["to go (past)"],
    }
    print(get_meaning(sentence, meaning_map))


"""
SPECS:

TIME COMPLEXITY: O(sentence x meaning_map x meaning_words)
SPACE COMPLEXITY: O(sentence x meaning_map)
"""

# NOTE: The problem is incomplete.
# We also need a source for which word appears in which context, to be able to infer
# this in the actual sentences.
# Once we have a set of strongly correlated words with each word-sense, we can search
# the context of a word in the target sentence.
# If there is a high overlap of those words with the already correlated words for a
# particular word sense, we can guess that that is the answer.
