"""
Problem:

Write a program that checks whether an integer is a palindrome. For example, 121 is a
palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a
string.
"""


def is_palindrome(num: int) -> bool:
    digits = 0
    num_copy = num
    while num_copy >= 10:
        digits += 1
        num_copy = num_copy // 10
    # checking for palindrome condition
    for i in range((digits) // 2 + 1):
        digit1 = (num // (10 ** i)) % 10
        digit2 = (num % (10 ** (digits - i + 1))) // (10 ** (digits - i))
        if digit1 != digit2:
            return False
    return True


if __name__ == "__main__":
    print(is_palindrome(121))
    print(is_palindrome(888))
    print(is_palindrome(1661))
    print(is_palindrome(235))
    print(is_palindrome(678))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
[n = number of digits]
"""
