"""
Problem:

You are given a string of parentheses. 
Write a function to compute the minimum number of parentheses to be removed to make the string valid 
(i.e. each open parenthesis is eventually closed)

Example:

Input = "()())()"
Output = 1

Input = ")("
Output = 2
"""

# FUNCTION TO PERFORM THE OPERATION
def num_parentheses_remove(expression, stack=[], num_removed=0):
    # returning num_removed if the expression and stack is empty
    if not expression and not stack:
        return num_removed
    # returning num_removed+stack size if the expression and stack isn't empty
    elif not expression:
        return len(stack) + num_removed

    # if the last paranthesis can be balanced, its opening part is removed from the stack
    if (expression[0] == ")") and (stack and stack[-1] == "("):
        stack.pop()
        return num_parentheses_remove(expression[1:], stack, num_removed)

    # getting the number of changes if the current paranthesis is added to stack
    num_added_to_stack = num_parentheses_remove(
        expression[1:], stack + [expression[0]], num_removed
    )
    # getting the number of changes if the current paranthesis is ignored (removed)
    num_ignored = num_parentheses_remove(expression[1:], stack, num_removed + 1)

    # returning the minimum of the 2 (num_added_to_stack, num_ignored)
    return min(num_added_to_stack, num_ignored)


# DIVER CODE
print(num_parentheses_remove("()())()"))
print(num_parentheses_remove(")("))
