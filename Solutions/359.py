"""
Problem:

You are given a string formed by concatenating several words corresponding to the
integers zero through nine and then anagramming.

For example, the input could be 'niesevehrtfeev', which is an anagram of
'threefiveseven'. Note that there can be multiple instances of each integer.

Given this string, return the original integers in sorted order. In the example above,
this would be 357.
"""

from collections import Counter
from sys import maxsize
from typing import Counter as C

WORDS = [
    Counter("zero"),
    Counter("one"),
    Counter("two"),
    Counter("three"),
    Counter("four"),
    Counter("five"),
    Counter("six"),
    Counter("seven"),
    Counter("eight"),
    Counter("nine"),
]


def generate_num_helper(counter: C[str]) -> C[int]:
    # runs in O(1) as all the loops run in constant time
    result = Counter()
    for value, word_counter in enumerate(WORDS):
        temp = maxsize
        for key in word_counter:
            # checking the number of occurance of current number
            if counter[key] >= word_counter[key]:
                temp = min(temp, counter[key] // word_counter[key])
            else:
                temp = 0
                break
        else:
            # updating the input counter to remove the current number
            curr_counter = Counter()
            for key in word_counter:
                curr_counter[key] = word_counter[key] * temp
            counter = counter - curr_counter
            result[value] = temp
    return result


def generate_num(string: str) -> int:
    str_counter = Counter(string)
    numbers_counter = generate_num_helper(str_counter)

    numbers_list = [str(num) for num in sorted(numbers_counter.elements())]
    return int("".join(numbers_list))


if __name__ == "__main__":
    print(generate_num("niesevehrtfeev"))
    print(generate_num("niesveeviehertifennevf"))


"""
SPECS:

TIME COMPLEXITY: O(n x log(n))
SPACE COMPLEXITY: O(n)
"""
