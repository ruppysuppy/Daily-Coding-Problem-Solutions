"""
Problem:

Given a string, return whether it represents a number. Here are the different kinds of
numbers:

"10", a positive integer
"-10", a negative integer
"10.1", a positive real number
"-10.1", a negative real number
"1e5", a number in scientific notation
And here are examples of non-numbers:

"a"
"x 1"
"a -2"
"-"
"""


def check_valid_number_representation(string: str) -> bool:
    is_valid = True
    has_number = False
    num_negatives, num_points, num_e = 0, 0, 0

    for char in string:
        if not (char.isdigit()):
            if char == "-":
                if num_negatives >= 1:
                    # if the string contains an 'e', 2 '-'s are allowed (for mantissa
                    # and exponent)
                    if num_negatives == 1 and num_e == 1:
                        num_negatives += 1
                        continue
                    is_valid = False
                    break
                num_negatives += 1
            elif char == ".":
                if num_points >= 1:
                    # if the string contains an 'e', 2 '.'s are allowed (for mantissa
                    # and exponent)
                    if num_points == 1 and num_e == 1:
                        num_points += 1
                        continue
                    is_valid = False
                    break
                num_points += 1
            elif char == "e":
                # a number can have only 1 'e'
                if num_e >= 1:
                    is_valid = False
                    break
                num_e += 1
            elif char == " ":
                # spaces are ignored
                pass
            else:
                # any other character makes the number invalid
                is_valid = False
                break
        else:
            # current character is a number
            has_number = True
    return is_valid and has_number


if __name__ == "__main__":
    print(check_valid_number_representation("10"))
    print(check_valid_number_representation("-10"))
    print(check_valid_number_representation("10.1"))
    print(check_valid_number_representation("-10.1"))
    print(check_valid_number_representation("1e5"))
    print(check_valid_number_representation("1e-5"))
    print(check_valid_number_representation("-1.6 e -5.2"))
    print(check_valid_number_representation("a"))
    print(check_valid_number_representation("x 1"))
    print(check_valid_number_representation("a -2"))
    print(check_valid_number_representation("-"))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
