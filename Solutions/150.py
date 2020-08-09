"""
Problem:

Given a list of points, a central point, and an integer k, find the nearest k points from the central point.

Example:

Input = [(0, 0), (5, 4), (3, 1)], (1, 2), 2, 
Output = [(0, 0), (3, 1)]
"""

# helper function to calculate the distance
def get_dist(point1, point2):
    # finding the distance using Pythagora's theorem
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


# FUNCTION TO PERFORM THE OPERATION
def KNN(arr, center, k):
    # getting the points sorted by distance and returning the first k values
    return sorted(arr, key=lambda pt: get_dist(pt, center))[:k]


# DRIVER CODE
arr = [(0, 0), (5, 4), (3, 1)]
center = (1, 2)
k = 2

print(KNN(arr, center, k))
