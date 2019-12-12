'''
Problem:

Implement regular expression matching with the following special characters:
. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

Example:
Input = "ra.", "ray"
Output = True
'''

# FUNCTION TO PERFORM THE OPERATION
def regex(expression, string):
    # Getting the length of the string and the expression
    len_str = len(string)
    len_ex = len(expression)

    # Creating the Matrix for Dynamic Programming
    DP = [[False]*(len_ex+1) for i in range(len_str+1)]

    # Setting the Base Case (expression="", string="")
    DP[0][0] = True

    # Looping over the matrix
    for i in range(len_str+1):
        for j in range(1,len_ex+1):
            # if a '*' is under consideration, the truth value is given by the following expression
            if (expression[j-1] == '*'):
                DP[i][j] = (DP[i][j-2]) or (i > 0 and j > 1 and (expression[j-2] == '.' or string[i-1] == expression[j-2]) and DP[i-1][j])
            # else if i > 0 (i == 0 => string = "") or the following conditions are met, the truth value is same as the left up diagonal value (DP[i-1][j-1])
            elif ((i > 0) and (expression[j-1] == '.' or expression[j-1] == string[i-1])):
                DP[i][j] = DP[i-1][j-1]
    
    return DP[len_str][len_ex]

# DRIVER CODE
print(regex("r.y", "ray"))
print(regex("ra.", "ray"))
print(regex("r.*", "rabcdefgh"))
print(regex(".*at", "chat"))
print(regex(".*at", "chats"))