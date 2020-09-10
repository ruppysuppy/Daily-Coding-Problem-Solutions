"""
Problem:

Implement regular expression matching with the following special characters:
. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

Example:
Input = "ra.", "ray"
Output = True
"""

# FUNCTION TO PERFORM THE OPERATION
def regex(expression, string):
    # Reversing the string (Not Mandatory, did it for ease of use - it could also be traversed from the end)
    string = string[::-1]
    expression = expression[::-1]
    # Getting the length of the expression
    len_ex = len(expression)
    # Position tracker for the string
    pos = 0
    # Flag to check the "*" charcter
    flag = False

    # If index error occours, then its not possible to match the expression to the string
    try:
        # Looping over the expression
        for i in range(len_ex):
            # If no "*" has been encountered
            if not flag:
                # if the expression and the string have the same characters at the position under consideration, the value of pos is incremented
                if expression[i] == string[pos]:
                    pos += 1
                # if the expression has a ".", pos is incremented
                elif expression[i] == ".":
                    pos += 1
                # if the expression has a "*", flag is set to True
                elif expression[i] == "*":
                    flag = True
                # if mismatch occours, False is returned
                else:
                    return False

            # If "*" was encountered in previous iteration
            else:
                # Checking for the occouramce of the charcter before "*" (it occours after the "*" as the expression is now reversed)
                temp = expression[i]

                # Incrementing pos till a different character is encountered
                while string[pos] == temp:
                    pos += 1

                # Resetting flag to ensure the control doesn't enter this segment again till another "*" is encounterd
                flag = False

    # Returning False incase of IndexError
    except IndexError:
        return False

    return True


# DRIVER CODE
print(regex("r.y", "ray"))
print(regex("ra.", "ray"))
print(regex("r.*", "rabcdefgh"))
print(regex(".*at", "chat"))
print(regex(".*at", "chats"))
