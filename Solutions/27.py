'''
Problem:

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
'''

# FUNCTION TO PERFORM THE OPERATION
def check(string, inp_dict={"{": "}", "[": "]", "(": ")"}): # By default round, curly, and square are considered, but other combinations can be used too
    open_set = set(inp_dict.keys()) # Creating a set of opening brackets

    # Declaring the stack
    stack = []

    # Looping over the input string
    try:
        for i in string:
            # If the charcter is an opening bracket and the stack is empty its added to the stack
            if (i in open_set):
                stack.append(i)
            # If its a closing bracket and the stack top contains the corresponding opening bracket, the opening bracket is pop-ed
            elif (inp_dict[stack[-1]] == i):
                stack.pop()
            # Otherwise it isn't balanced
            else:
                return False
    except:
        return False
    
    # If the stack is empty, the number of opening and closing brackets are equal and balanced
    if (stack == []):
        return True
    else:
        return False

# DRIVER CODE
print(check("([])[]({})"))
print(check("([)]"))
print(check("((()"))