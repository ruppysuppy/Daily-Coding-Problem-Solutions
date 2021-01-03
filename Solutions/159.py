"""
Problem:

Given a string, return the first recurring character in it, or null if there is no
recurring chracter.

For example, given the string "acbbac", return "b". Given the string "abcdef", return
null.
"""

from typing import Optional


def get_first_recurring_character(string: str) -> Optional[str]:
    seen_characters = set()

    for char in string:
        if char in seen_characters:
            return char
        seen_characters.add(char)
    return None


if __name__ == "__main__":
    print(get_first_recurring_character("acbbac"))
    print(get_first_recurring_character("abcdef"))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
