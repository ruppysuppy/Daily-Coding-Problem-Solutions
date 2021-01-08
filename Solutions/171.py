"""
Problem:

You are given a list of data entries that represent entries and exits of groups of
people into a building. An entry looks like this:

{"timestamp": 1526579928, "count": 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, "count": 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the
building. Return it as a pair of (start, end) timestamps. You can assume the building
always starts off and ends up empty, i.e. with 0 people inside.
"""

from typing import Dict, List, Tuple, Union


def calculate_busiest_time(
    list_of_events: List[Dict[str, Union[int, str]]]
) -> Tuple[int, int]:
    list_of_events.sort(key=lambda event: event["timestamp"])
    people_inside_map = {}
    event = list_of_events[0]
    last_pos = event["timestamp"]
    # people can only enter as the building at the begining
    people_inside_map[last_pos] = event["count"]
    # generating people in the building by timestamp
    for event in list_of_events[1:]:
        count = event["count"]
        if event["type"] == "enter":
            curr_people_inside = people_inside_map[last_pos] + count
        else:
            curr_people_inside = people_inside_map[last_pos] - count
        people_inside_map[event["timestamp"]] = curr_people_inside
        last_pos = event["timestamp"]
    # generating the start time
    people_inside_list = list(people_inside_map.items())
    people_inside_list.sort(reverse=True, key=lambda element: element[1])
    start = people_inside_list[0][0]
    people_inside_list.sort(key=lambda element: element[0])
    # generating the end time
    flag = False
    for timestamp, _ in people_inside_list:
        if flag:
            end = timestamp
            break
        if timestamp == start:
            flag = True
    return start, end


if __name__ == "__main__":
    events = [
        {"timestamp": 1526579928, "count": 3, "type": "enter"},
        {"timestamp": 1526579982, "count": 4, "type": "enter"},
        {"timestamp": 1526580054, "count": 5, "type": "exit"},
        {"timestamp": 1526580128, "count": 1, "type": "enter"},
        {"timestamp": 1526580382, "count": 3, "type": "exit"},
    ]
    print(calculate_busiest_time(events))


"""
SPECS:

TIME COMPLEXITY: O(n log(n))
SPACE COMPLEXITY: O(n)
"""
