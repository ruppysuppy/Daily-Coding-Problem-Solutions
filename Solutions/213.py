'''
Problem:

Given a string of digits, generate all possible valid IP address combinations.
IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255. 
Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.

Example:

Input = "2542540123"
Output = ['254.25.40.123', '254.254.0.123']
'''

# generating the set of acceptable numbers
ACCEPTABLE_NUMBERS = set([str(i) for i in range(256)])

# helper function to generate the ip combinations
def get_ip_combinations_helper(string, curr, accumulator):
    # if the end of the string is reached and a proper ip config is generated
    # the combination is added to the accumulator
    if (not string and len(curr) == 4):
        accumulator.append(list(curr))
        return
    # if the combination is not correct, its not added to the accumulator
    elif (len(curr) > 4):
        return
    
    # declaring the current part
    curr_part = ""

    # iterating through the string
    for char in string:
        # generating the current part
        curr_part += char

        # getting the length of the current part
        length = len(curr_part)
        # if the length is more than acceptable, the function breaks out
        if (length > 3):
            return
        
        # if the current part is an acceptable number, get_ip_combinations_helper is called recursively 
        if (curr_part in ACCEPTABLE_NUMBERS):
            get_ip_combinations_helper(string[length:], list(curr) + [curr_part], accumulator)

# FUNCTION TO PERFORM THE OPERATION
def get_ip_combinations(string):
    # declaring an accumulator to store the values
    accumulator = []
    # calling the helper functions to generate the combinations in the form ["0", "0", "0", "0"]
    get_ip_combinations_helper(string, [], accumulator)
    # returning the ip configurations in the proper format
    return [".".join(combination) for combination in accumulator]

# DRIVER CODE
print(get_ip_combinations("2542540123"))