'''
Problem:

Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single count and character. 
Implement run-length encoding and decoding. 
You can assume the string to be encoded have no digits and consists solely of alphabetic characters. 
You can assume the string to be decoded is valid.

Example:

ENCODE:
Input = "AAAABBBCCDAA"
Output = "4A3B2C1D2A"

DECODE:
Input = "4A3B2C1D2A"
Output = "AAAABBBCCDAA"
'''

# FUNCTION TO PERFORM THE OPERATION (Encode)
def encode(string):
    # Declaring necessary variables
    # ans: stores the encoded string
    # temp: stores the current charcter
    # count: stores the count of the current charcter
    ans = ""
    temp = string[0]
    count = 0

    # Looping over the string
    for i in string:
        # if the current charcter differs from the character in temp, count and temp is added to the answer
        if (i != temp):
            ans += str(count) + temp
            temp = i
            count = 1
        # if the current charcter is same as temp, count is incremented
        else:
            count += 1
    
    # Adding the last character and count
    ans += str(count) + temp
    temp = i
    count = 1

    return ans

# FUNCTION TO PERFORM THE OPERATION (Decode)
def decode(string):
    # Declaring necessary variables
    # ans: stores the encoded string
    # temp: stores the count of the current charcter
    ans = ""
    temp = 0

    # Looping over the string
    for i in string:
        # if the charcter is a digit, its added to temp at the units place
        if (i.isdigit()):
            temp = temp * 10 + int(i)
        # else the result is addedc to the decoded string
        else:
            ans += i * temp
            temp = 0
    
    return ans

# DRIVER CODE
print(encode("AAAABBBCCDAA"))
print(decode("4A3B2C1D2A"))