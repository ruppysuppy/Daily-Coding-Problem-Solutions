"""
Problem:

Given a string of parentheses, find the balanced string that can be produced from it using the minimum number of insertions and deletions. 
If there are multiple solutions, return any of them.

Example:

Input = "(()"
Output = "(())"

Input = "))()("
Output = "()()()()"
"""

# helper function for the computation
def get_min_changes_helper(string, modifications, stack, current):
    # base case for recursion (both the string and the stack is exhausted)
    if not string and not stack:
        return modifications, current
    # base case for recursion (the string is exhausted and the stack still has elements)
    elif not string:
        additions = len(stack)
        return modifications + additions, current + (")" * additions)

    # if the current element is "("
    if string[0] == "(":
        # getting the modifications and the strings for adding the element to the stack or modifying it
        modifications1, string1 = get_min_changes_helper(
            string[1:], modifications, stack + ["("], current + "("
        )
        modifications2, string2 = get_min_changes_helper(
            string[1:], modifications + 1, stack, current
        )

        # returning the required element
        return min(
            [(modifications1, string1), (modifications2, string2)],
            key=lambda tup: tup[0],
        )

    # if the current element is ")"
    else:
        # if the stack holds elements, 1 "(" is poped and getting the modifications and the string
        if stack:
            stack.pop()
            return get_min_changes_helper(
                string[1:], modifications, stack, current + ")"
            )
        # else modifications is incremented and getting the modifications and the string
        else:
            return get_min_changes_helper(string[1:], modifications + 1, stack, current)


# FUNCTION TO PERFORM THE OPERATION
def get_min_changes(string):
    # getting and returning the result
    _, res = get_min_changes_helper(string, 0, [], "")
    return res


# DRIVER CODE
print(get_min_changes("(()"))
print(get_min_changes("))()("))
print(get_min_changes("()(()"))
print(get_min_changes("()(()))"))
print(get_min_changes(")(())"))
print(get_min_changes("())("))
