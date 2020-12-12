"""
Problem:

We're given a hashmap with a key courseId and value a list of courseIds, which
represents that the prerequsite of courseId is courseIds. Return a sorted ordering of
courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []},
should return ['CSC100', 'CSC200', 'CSCS300'].
"""

from typing import Dict, List, Optional, Set, Tuple


def get_order_helper(
    course_map: Dict[str, str],
    course: str,
    order: List[str],
    processed: Set[str],
    break_limit: Optional[int] = None,
    curr: int = 0,
) -> Tuple[Optional[List[int]], Optional[Set[int]]]:
    if not break_limit:
        break_limit = len(course_map)
    if break_limit < curr:
        return None, None
    if course_map[course] == []:
        # if the course doesn't have any pre-req
        if course not in processed:
            order.append(course)
            processed.add(course)
        return order, processed

    for prerequisite in course_map[course]:
        order, processed = get_order_helper(
            course_map, prerequisite, order, processed, break_limit, curr + 1
        )
        if order is None:
            return None, None
    order.append(course)
    processed.add(course)
    return order, processed


def get_order(course_map: Dict[str, str]) -> Optional[List[str]]:
    order = []
    processed = set()

    for course in course_map:
        if course not in processed:
            for prerequisite in course_map[course]:
                if prerequisite not in processed:
                    order, processed = get_order_helper(
                        course_map, prerequisite, order, processed
                    )
                    if order is None:
                        return None
            order.append(course)
            processed.add(course)
    return order


if __name__ == "__main__":
    prereqs = {"CSC300": ["CSC100", "CSC200"], "CSC200": ["CSC100"], "CSC100": []}
    print(get_order(prereqs))

    prereqs = {
        "CSC400": ["CSC300"],
        "CSC300": ["CSC100", "CSC200"],
        "CSC200": ["CSC100"],
        "CSC100": [],
    }
    print(get_order(prereqs))

    prereqs = {
        "CSC400": ["CSC300"],
        "CSC300": ["CSC100", "CSC200"],
        "CSC200": ["CSC100"],
        "CSC100": ["CSC400"],
    }
    print(get_order(prereqs))


"""
SPECS:

TIME COMPLEXITY: O(courses x prerequisites)
SPACE COMPLEXITY: O(courses x prerequisites)
"""
