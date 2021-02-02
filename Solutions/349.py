"""
Problem:

Soundex is an algorithm used to categorize phonetically, such that two names that sound
alike but are spelled differently have the same representation.

Soundex maps every name to a string consisting of one letter and three numbers, like
M460.

One version of the algorithm is as follows:

Remove consecutive consonants with the same sound (for example, change ck -> c).
Keep the first letter. The remaining steps only apply to the rest of the string.
Remove all vowels, including y, w, and h.
Replace all consonants with the following digits:
b, f, p, v -> 1
c, g, j, k, q, s, x, z -> 2
d, t -> 3
l -> 4
m, n -> 5
r -> 6
If you don't have three numbers yet, append zeros until you do. Keep the first three
numbers. Using this scheme, Jackson and Jaxen both map to J250.
"""

IRRELEVANT_CHAR = {"a", "e", "i", "o", "u", "y", "w", "h"}
SIMILAR_SOUND_MAP = {"c": {"k", "s"}, "k": {"c"}, "s": {"c"}}
CHAR_DIGIT_MAP = {
    "b": "1",
    "f": "1",
    "p": "1",
    "v": "1",
    "c": "2",
    "g": "2",
    "j": "2",
    "k": "2",
    "q": "2",
    "s": "2",
    "x": "2",
    "z": "2",
    "d": "3",
    "t": "3",
    "l": "4",
    "m": "5",
    "n": "5",
    "r": "6",
}


def soundex(word: str) -> str:
    # removing irrelevant characters from the word
    word = "".join([char for char in word.lower() if char not in IRRELEVANT_CHAR])
    last_char = word[0]
    transformed_word = last_char
    soundex_map = ""
    # eliminating similar sounding characters
    for char in word[1:]:
        if char in SIMILAR_SOUND_MAP:
            if last_char in SIMILAR_SOUND_MAP[char]:
                continue
        transformed_word += char
        last_char = char
    # generating soundex
    soundex_map = transformed_word[0].upper()
    for char in transformed_word[1:]:
        soundex_map += CHAR_DIGIT_MAP[char]
    return soundex_map + "0" * (4 - len(soundex_map))


if __name__ == "__main__":
    print(soundex("Jackson"))
    print(soundex("Jaxen"))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
