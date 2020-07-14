'''
Problem:

In academia, the h-index is a metric used to calculate the impact of a researcher's papers. 
It is calculated as follows:
A researcher has index h if at least h of her N papers have h citations each. 
If there are multiple h satisfying this formula, the maximum is chosen.
Given a list of paper citations of a researcher, calculate their h-index.

Example:

N = 5
citations = [4, 3, 0, 1, 5]
Output = 3 (since the researcher has 3 papers with at least 3 citations)
'''

def get_h_index(citations):
    citations.sort(reverse=True)
    for index, citation in enumerate(citations):
        if index >= citation:
            # implies that there are 'index' papers with atleast 'citation' citations
            return index
    return 0


# DRIVER CODE
print(get_h_index([4, 3, 0, 1, 5]))
print(get_h_index([4, 1, 0, 1, 1]))
print(get_h_index([4, 4, 4, 5, 4]))