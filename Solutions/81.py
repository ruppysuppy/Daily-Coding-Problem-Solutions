'''
Problem:

Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. 
You can assume each valid number in the mapping is a single digit.

Example:

Input = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f']}, "23"
Output = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
'''

# FUNCTION TO PERFORM THE OPERATION
def mapping(inp_map, string, res=[]):
    # returning the res array if the string is empty (base case for recursion)
    if (not string):
        return res
    
    # during the 1st call, adding the characters to the list
    if (not res):
        for elem in inp_map[string[0]]:
            res.append(elem)

    # adding additional characters depending upon the next character of the input string
    else:
        # using another list as it cannot be modified while looping over it
        temp = []
        # adding new character to each character present in res and adding the result to temp list
        for part in res:
            for elem in inp_map[string[0]]:
                temp.append(part+elem)
        # overwriting res
        res = temp
    
    # recursive call for the next charcter
    return mapping(inp_map, string[1:], res)

# DRIVER CODE
print(mapping({'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f']}, "23", []))
print(mapping({'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f']}, "32", []))