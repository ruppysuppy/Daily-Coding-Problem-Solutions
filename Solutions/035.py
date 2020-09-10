"""
Problem:
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. 
You can only swap elements of the array.
Do this in linear time and in-place.

Example:
['G', 'B', 'R', 'R', 'B', 'R', 'G'] => ['R', 'R', 'R', 'G', 'G', 'B', 'B']
"""

# FUNCTION TO PERFORM THE OPERATION
def segregate(Arr, length):
    # position vairable to store the (last + 1) location of "R"s (1st pass) and "G"s (2nd pass)
    pos = 0

    # 1st pass for segregating "R"s
    for i in range(length):
        # if a "R" is encountered, it is swapped with the element at the index pos and pos is incremented
        if Arr[i] == "R":
            Arr[i], Arr[pos] = Arr[pos], Arr[i]
            pos += 1

    # 1st pass for segregating "G"s
    for i in range(pos, length):
        # if a "G" is encountered, it is swapped with the element at the index pos and pos is incremented
        if Arr[i] == "G":
            Arr[i], Arr[pos] = Arr[pos], Arr[i]
            pos += 1

    return Arr


# DRIVER CODE
inp = ["G", "B", "R", "R", "B", "R", "G"]
print(segregate(inp, len(inp)))
