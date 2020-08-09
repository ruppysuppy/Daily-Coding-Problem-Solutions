"""
Problem:

You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string. 
Determine whether the parentheses are balanced.

Example:

Input = (()*
Output = balanced

Input = (*)
Output = balanced

Input = )*(
Output = not balanced
"""

# FUNCTION TO PERFORM THE OPERATION
def can_balance(string, stack=None):
    # creating the stack if it has not been passed (1st call)
    if stack == None:
        stack = []

    # if both the string and stack are empty, the parenthesis is balanced (base case for recursion)
    if not string and not stack:
        return True
    # if the string is empty and stack isn't, the parenthesis is not balanced (base case for recursion)
    elif not string:
        return False

    # if the 1st element is an opening parenthesis, its added to the stack and the function called recursively
    if string[0] == "(":
        stack.append("(")
        return can_balance(string[1:], stack)

    # if the 1st element is an closing parenthesis, if the parenthesis can be balanced the function called recursively
    # else False is returned
    elif string[0] == ")":
        if stack and stack[-1] == "(":
            stack.pop()
            return can_balance(string[1:], stack)
        else:
            return False

    # if the 1st element is '*', all the possible combinations are checked and if any of them can be balanced, True is returned
    elif string[0] == "*":
        return (
            can_balance("(" + string[1:], list(stack))
            or can_balance(")" + string[1:], list(stack))
            or can_balance(string[1:], list(stack))
        )


# DRIVER CODE
print(can_balance("(()*"))
print(can_balance("(*)"))
print(can_balance(")*("))
