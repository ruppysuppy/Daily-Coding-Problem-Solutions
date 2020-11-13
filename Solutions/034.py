"""
Problem:

Given a string, find the palindrome that can be made by inserting the fewest number of
characters as possible anywhere in the word. If there is more than one palindrome of
minimum length that can be made, return the lexicographically earliest one (the first
one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add
three letters to it (which is the smallest amount to make a palindrome). There are
seven other palindromes that can be made from "race" by adding three letters, but
"ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
"""


def get_nearest_palindrome(string: str) -> str:
    if string[::-1] == string:
        return string
    # generating the closest palindrome possible
    length = len(string)
    if string[0] == string[-1]:
        return string[0] + get_nearest_palindrome(string[1 : length - 1]) + string[0]
    # incase the 1st characters are different, strings using both the characters are
    # generated
    pal_1 = string[0] + get_nearest_palindrome(string[1:]) + string[0]
    pal_2 = string[-1] + get_nearest_palindrome(string[: length - 1]) + string[-1]
    # if one of the string is shorter, it is returned
    if len(pal_1) != len(pal_2):
        return min(pal_1, pal_2, key=lambda x: len(x))
    # if both strings have the same length, the lexicographically earliest one is
    # returned
    return min(pal_1, pal_2)


if __name__ == "__main__":
    print(get_nearest_palindrome("race"))
    print(get_nearest_palindrome("google"))


"""
SPECS:

TIME COMPLEXITY: O(2 ^ n)
SPACE COMPLEXITY: O(n)
"""
