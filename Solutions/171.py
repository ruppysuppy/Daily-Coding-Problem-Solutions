'''
Problem:

You are given a list of data entries that represent entries and exits of groups of people into a building. 

An entry looks like this:
{"timestamp": 1526579928, "count": 3, "type": "enter"}
This means 3 people entered the building. 

An exit looks like this:
{"timestamp": 1526580382, "count": 2, "type": "exit"}
This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building. 
Return it as a pair of (start, end) timestamps. 
You can assume the building always starts off and ends up empty, i.e. with 0 people inside.
'''

# FUNCTION TO PERFORM THE OPERATION
def calc_busiest_time(list_of_events):
    # datetime can be used to parse the timestamp, but its not essential
    # sorting the events by the timestamp
    list_of_events.sort(key=lambda event: event["timestamp"])

    # dictionary to store the number of people inside the building
    dict_people_inside = {}

    # initializing the necessary variables
    event = list_of_events[0]
    last_pos = event["timestamp"]

    # people can only enter as the building had no people
    dict_people_inside[last_pos] = event["count"]

    # iterating through the events
    for event in list_of_events[1:]:
        # getting the count of people entering / leaving
        count = event["count"]

        # checking the action (entry / exit) and getting the new number of people
        if (event["type"] == "enter"):
            temp = dict_people_inside[last_pos] + count
        else:
            temp = dict_people_inside[last_pos] - count
        
        # updating the values in the dictionary
        last_pos = event["timestamp"]
        dict_people_inside[last_pos] = temp
    
    # creating a list from the dictionary [each element: (timestamp, people_inside)]
    temp_list = list(dict_people_inside.items())
    
    # sorting the list (in reverse) by number of people inside and storing the timestamp of the busiest time
    temp_list.sort(reverse=True, key=lambda element: element[1])
    start = temp_list[0][0]
    
    # sorting the list again by time stamp
    temp_list.sort(key=lambda element: element[0])
    
    # flag stores if the next index is the end timestamp
    flag = False

    # iterating through the list of timestamp and people inside
    for timestamp, _ in temp_list:
        # if flag is set, the current timestamp is the end timestamp, the control breaks out of the loop
        if (flag):
            end = timestamp
            break

        # if the current timestamp is the start, flag is set
        if (timestamp == start):
            flag = True
    
    # returning the start and end
    return start, end

# DRIVER CODE
events = [
    {"timestamp": 1526579928, "count": 3, "type": "enter"},
    {"timestamp": 1526579982, "count": 4, "type": "enter"},
    {"timestamp": 1526580054, "count": 5, "type": "exit"},
    {"timestamp": 1526580128, "count": 1, "type": "enter"},
    {"timestamp": 1526580382, "count": 3, "type": "exit"}
]
print(calc_busiest_time(events))