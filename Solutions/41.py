'''
Problem:

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. 
If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. 
All flights must be used in the itinerary.

Example:

[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL' => ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
[('SFO', 'COM'), ('COM', 'YYZ')], 'COM' => None
[('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A' => ['A', 'B', 'C', 'A', 'C'] 
'''

# FUNCTION TO PERFORM THE OPERATION
def get_itinerary(flights, starting_point, current_itinerary=[]):
    # Base case of recursion (all flights except the final destination has been added)
    if (not flights and current_itinerary):
        return current_itinerary + [starting_point]
    # if no flights are provided, None is returned
    elif (not flights):
        return None

    # resulatant_itinerary stores the final result
    resulatant_itinerary = None

    # iterating over the flight list
    for index, (src, dest) in enumerate(flights):
        # if the starting point is found the iternary using that destination is calculated (DFS)
        if (starting_point == src):
            child_itinerary = get_itinerary(flights[:index] + flights[index + 1:], dest, current_itinerary + [src])

            # if the child_itinerary is a vaild itinerary and lexicographically smaller, the resulatant_itinerary is updated
            if (child_itinerary and (not resulatant_itinerary or ("".join(child_itinerary) < "".join(resulatant_itinerary)))):
                resulatant_itinerary = child_itinerary

    return resulatant_itinerary

# DRIVER CODE
print(get_itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], "YUL"))
print(get_itinerary([('SFO', 'COM'), ('COM', 'YYZ')], "COM"))
print(get_itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], "A"))