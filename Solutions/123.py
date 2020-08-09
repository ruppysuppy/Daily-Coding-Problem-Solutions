"""
Problem:

Given a string, return whether it represents a number. 

Here are the different kinds of numbers:
* "10", a positive integer
* "-10", a negative integer
* "10.1", a positive real number
* "-10.1", a negative real number
* "1e5", a number in scientific notation

And here are examples of non-numbers:
* "a"
* "x 1"
* "a -2"
* "-"
"""

# FUNCTION TO PERFORM THE OPERATION
def check(string):
    # is Valid checks whether the number is valid
    # num_neg checks the number of occourance of "-"
    # num_pt checks the number of occourance of "."
    # num_e checks the number of occourance of "e"
    # hasNum checks the occourance of a number
    isValid = True
    num_neg = 0
    num_pt = 0
    num_e = 0
    hasNum = False

    # looping over the string
    for i in string:
        # if the current character is not a number
        if not (i.isdigit()):
            # checking the number of the corresponding symbol, if the number of the same symbol is greater than 1, it is not valid [exceptions are there]
            if i == "-":
                if num_neg >= 1:
                    # if the string contains an 'e' we can have 2 '-'s (for mantissa and exponent) [exception]
                    if num_neg == 1 and num_e == 1:
                        num_neg += 1
                        continue

                    isValid = False
                    break
                else:
                    num_neg += 1

            elif i == ".":
                if num_pt >= 1:
                    # if the string contains an 'e' we can have 2 '.'s (for mantissa and exponent) [exception]
                    if num_pt == 1 and num_e == 1:
                        num_pt += 1
                        continue

                    isValid = False
                    break
                else:
                    num_pt += 1

            elif i == "e":
                if num_e >= 1:
                    isValid = False
                    break
                else:
                    num_e += 1

            # if the character is a space, its ignored
            elif i == " ":
                pass

            # any other character makes the string invalid
            else:
                isValid = False
                break

        # if the current character is a number hasNum is set to True
        else:
            hasNum = True

    return isValid and hasNum


# DRIVER CODE
print(check("10"))
print(check("-10"))
print(check("10.1"))
print(check("-10.1"))
print(check("1e5"))
print(check("1e-5"))
print(check("-1.6 e -5.2"))
print(check("a"))
print(check("x 1"))
print(check("a -2"))
print(check("-"))
