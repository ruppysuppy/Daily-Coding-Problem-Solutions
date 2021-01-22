"""
Problem:

Write a program that computes the length of the longest common subsequence of three
given strings. For example, given "epidemiologist", "refrigeration", and
"supercalifragilisticexpialodocious", it should return 5, since the longest common
subsequence is "eieio".
"""


def lcs_of_3(str1: str, str2: str, str3: str) -> int:
    str1_length = len(str1)
    str2_length = len(str2)
    str3_length = len(str3)
    dp_matrix = [
        [[0 for i in range(str3_length + 1)] for j in range(str2_length + 1)]
        for k in range(str1_length + 1)
    ]
    # generating the matrix in bottom up
    for i in range(1, str1_length + 1):
        for j in range(1, str2_length + 1):
            for k in range(1, str3_length + 1):
                if str1[i - 1] == str2[j - 1] and str1[i - 1] == str3[k - 1]:
                    dp_matrix[i][j][k] = dp_matrix[i - 1][j - 1][k - 1] + 1
                else:
                    dp_matrix[i][j][k] = max(
                        max(dp_matrix[i - 1][j][k], dp_matrix[i][j - 1][k]),
                        dp_matrix[i][j][k - 1],
                    )
    return dp_matrix[str1_length][str2_length][str3_length]


if __name__ == "__main__":
    print(
        lcs_of_3(
            "epidemiologist", "refrigeration", "supercalifragilisticexpialodocious"
        )
    )


"""
SPECS:

TIME COMPLEXITY: O(n ^ 3)
SPACE COMPLEXITY: O(n ^ 3)
"""
