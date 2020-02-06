'''
Problem:

Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.
For example, given a file with the content "Hello world", three read7() returns "Hello w", "orld" and then "".
'''
# global varibles
# COUNT7 stores the number of characters read from the file (used in read7)
COUNT7 = 0
# DATA stores the unreturned data (used in readN)
DATA = ""

# read7 function
def read7():
    # declaring COUNT7 as global variable
    global COUNT7

    # reading the next 7 characters
    with open('data_82.txt', 'r') as f:        
        f.seek(COUNT7, 0)
        data = f.read(7)

    # incrementing COUNT7 by 7
    COUNT7 += 7
    
    # returning the data
    return data

# FUNCTION TO PERFORM THE OPERATION
def readN(n):
    # declaring DATA as global variable
    global DATA

    # reading ceiling(n / 7) * 7 characters
    for _ in range(n // 7):
        DATA += read7()    
    DATA += read7()

    # storing the characters which are not needed and returning the characters asked for
    temp = DATA[:n]
    DATA = DATA[n:]

    return temp

# DRIVER CODE
print(readN(3))
print(readN(10))
print(readN(15))
print(readN(25))