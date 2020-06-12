'''
Problem:

Write a program that computes the length of the longest common subsequence of three given strings. 

Example:

Input = "epidemiologist", "refrigeration", "supercalifragilisticexpialodocious"
Output = 5 (since the longest common subsequence is "eieio")
'''

# FUNCTION TO PERFORM THE OPERATION
def lcs_of_3(str1, str2, str3):
    # getting the lengths of the strings
    str1_length = len(str1)
    str2_length = len(str2)
    str3_length = len(str3)

    # creating the 3d matrix for dp
    dp_matrix = [
        [[0 for i in range(str3_length+1)] 
        for j in range(str2_length+1)] 
        for k in range(str1_length+1)
        ]

    # generating the matrix in bottom up fashion
    # loops start from 1 as if any of the string is empty, there is no common sub-sequence
    for i in range(1, str1_length+1):
        for j in range(1, str2_length+1):
            for k in range(1, str3_length+1):
                # if a match occours, the data is updated
                if (str1[i-1] == str2[j-1] and str1[i-1] == str3[k-1]):
                    dp_matrix[i][j][k] = dp_matrix[i-1][j-1][k-1] + 1

                # in case of no match, the maximum result for the part before the current position is selected
                else:
                    dp_matrix[i][j][k] = max(
                        max(dp_matrix[i-1][j][k], dp_matrix[i][j-1][k]), 
                        dp_matrix[i][j][k-1]
                        )
    # returning the length of the longest common subsequence
    return dp_matrix[str1_length][str2_length][str3_length]

# DRIVER CODE
print(lcs_of_3("epidemiologist", "refrigeration", "supercalifragilisticexpialodocious"))