'''
Problem:

1 to 26 represent a to z, find the number of ways a series of numbers can be decoded (eg: 111 returns 3)
'''

# FUNCTION TO PERFORM THE OPERATION
def tree_trav(string, length, acc=1):

    # Main loop to iterate over the string
    for i in range(length-1):
        # If the combination of 2 charaters is a valid encoding, but the 2nd character alone isn't (0)
        if ((string[i] + string[i+1]) in Set and (string[i+1] not in Set)):
            continue

        # If the combination of 2 charaters is a valid encoding:
        # Adding 1 to the accumulator as the number can be decoded in 1 more way and recursively calling the function on the rest of the string
        elif ((string[i] + string[i+1]) in Set):
            temp = string[i+2:]
            acc = tree_trav(temp, len(temp), acc+1)
    
    return acc

# Creating the set of accepted values
Set = set()

for i in range(1, 27):
    Set.add(str(i))

# DRIVER CODE
inp = input("Enter the sequence: ")

print("Total number of subcombinations: {}".format(tree_trav(inp, len(inp))))