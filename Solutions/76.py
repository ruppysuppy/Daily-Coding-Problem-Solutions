'''
Problem:

You are given an N by M 2D matrix of lowercase letters. 
Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. 
That is, the letter at each column is lexicographically later as you go down each row. 
It does not matter whether each row itself is ordered lexicographically.

Example:

Input = ['cba', 'daf', 'ghi'] (This is not ordered because of the 'a' in the center)
Output = 1 (We can remove the second column to make it ordered: ['ca', 'df', 'gi'])

Input = ['abcdef']
Output = 0 (there's only one row)

Input = ['zyx', 'wvu', 'tsr']
Output = 3 (since we would need to remove all the columns to order it)
'''

# FUNCTION TO PERFORM THE OPERATION
def calc(mat):
    # setting the deault variables
    # num_elements stores the number of elements
    # length stores the length of each row
    # count stores number of columns to remove
    num_elements, length = len(mat), len(mat[0])
    count = 0

    # looping over wach column
    for i in range(length):
        # checking if the columns are lexicographically arranged
        for j in range(num_elements-1):
            # if the column is not lexicographical, count is incremented and control breaks out of the loop
            if (mat[j][i] > mat[j+1][i]):
                count += 1
                break
    
    return count

# DRIVER CODE
inp1 = ["cba", "daf", "ghi"]
inp2 = ["abcdef"]
inp3 = ["zyx", "wvu", "tsr"]

print(calc(inp1))
print(calc(inp2))
print(calc(inp3))