"""
Problem:

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

Example:

Input = [(30, 75), (0, 50), (60, 150)]
Output = 2
"""

# FUNCTION TO PERFORM THE OPERATION
def find_num_rooms(intervals):
    # Creating an empty dictionary to store the rooms required (+ve for start, -ve for end)
    D = {}

    # Populating the dictionary
    for v in intervals:
        # If the start is already in the dictionary, its value is incremented, else its set to 1
        if v[0] in D:
            D[v[0]] = D[v[0]] + 1
        else:
            D[v[0]] = 1

        # If the end is already in the dictionary, its value is decremented, else its set to -1
        if v[1] in D:
            D[v[1]] = D[v[1]] - 1
        else:
            D[v[1]] = -1

    # Sorting the dictionary by their time
    sorted_events = sorted(D.items(), key=lambda x: x[0])
    # Variables to store the maximum number of rooms required and rooms required at the moment
    max_rooms = 0
    rooms = 0

    # Looping over the events and checking the number of rooms required
    # If a class ends, the value in the dict is -ve, so upon addition, it reduces the number of rooms required
    for k, v in sorted_events:
        rooms += v

        # If the number of rooms required surpasses the maximum number of rooms required, max_rooms is set using the value of rooms
        if rooms > max_rooms:
            max_rooms = rooms

    return max_rooms


# DRIVER CODE
lectures = [(30, 75), (0, 50), (60, 150)]
print("Max Rooms needed:", find_num_rooms(lectures))
