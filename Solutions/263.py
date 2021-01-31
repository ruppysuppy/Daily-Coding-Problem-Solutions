"""
Problem:

Create a basic sentence checker that takes in a stream of characters and determines
whether they form valid sentences. If a sentence is valid, the program should print it
out.

We can consider a sentence valid if it conforms to the following rules:

The sentence must start with a capital letter, followed by a lowercase letter or a
space.
All other characters must be lowercase letters, separators (,,;,:) or terminal marks
(.,?,!,‽).
There must be a single space between each word.
The sentence must end with a terminal mark immediately following a word.
"""

TERMINALS = [".", "?", "!", "‽"]
SEPARATORS = [",", ";", ":"]


def check_sentence(sentence: str) -> None:
    if len(sentence) < 2 or not sentence[0].isupper():
        return
    if not sentence[1].islower() and not sentence[1].isspace():
        return

    space_flag = False
    for char in sentence[1:-1]:
        if char.isspace():
            if space_flag:
                return
            space_flag = True
            continue
        space_flag = False
        if not char.islower() and char not in SEPARATORS:
            return

    if sentence[-1] in TERMINALS:
        print(sentence)


if __name__ == "__main__":
    check_sentence("This, will, pass.")
    check_sentence("ThiS Should fail.")
    check_sentence("this Should fail Too.")
    check_sentence("This too should fail")


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
[n = number of characters in the string]
"""
