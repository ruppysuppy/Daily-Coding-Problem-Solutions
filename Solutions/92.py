'''
Problem:

We're given a hashmap with a key courseId and value a list of courseIds, which represents that the prerequsite of courseId is courseIds. 
Return a sorted ordering of courses such that we can finish all courses.
Return null if there is no such ordering.

Example:

Input = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
Output = ['CSC100', 'CSC200', 'CSCS300']
'''

# helper function to get the order for the pre-requisites for a course
def get_order_helper(hash_map, course, order, processed, break_limit=None, curr=0):
    # getting the break limit (function calls implying its not possible to order the course)
    if (not break_limit):
        break_limit = len(hash_map)
    
    # if the current function calls exceed the break limit None is returned for order & processed
    if (break_limit < curr):
        return None, None
    
    # if the course doesn't have any pre-req
    if (hash_map[course] == []):
        # if the course has not been processed, its added to order + processed
        if (course not in processed):
            order.append(course)
            processed.add(course)
        # returning order + processed
        return order, processed
    
    else:
        # for each pre-req, we update the order and processed
        for pre_req in hash_map[course]:
            order, processed = get_order_helper(hash_map, pre_req, order, processed, break_limit, curr+1)
            # if the ordering is not possible None is returned for order & processed
            if (order == None):
                return None, None
        
        # adding the course to order + processed
        order.append(course)
        processed.add(course)
        # returning order + processed
        return order, processed

# FUNCTION TO PERFORM THE OPERATION
def get_order(hash_map):
    # order stores the resultant order
    # processed stores the nodes processed
    order = []
    processed = set()

    # iterating over the hash_map
    for course_parent in hash_map:
        # if the node (course) hasn't been processed, we process it
        if (course_parent not in processed):
            # checking all the pre-requisite for the current course
            for course in hash_map[course_parent]:
                # if the node (course pre-requisite) hasn't been processed, we process it
                if (course not in processed):
                    # getting the order and processed nodes
                    order, processed = get_order_helper(hash_map, course, order, processed)
                    # if order == None ordering of the given courses is not possible
                    if (order == None):
                        return None
            # adding the course to order and processed
            order.append(course_parent)
            processed.add(course_parent)
    
    return order

# DRIVER CODE
prereqs = {
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': []
}
print(get_order(prereqs))

prereqs = {
    'CSC400': ['CSC300'],
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': []
}
print(get_order(prereqs))

prereqs = {
    'CSC400': ['CSC300'],
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': ['CSC400']
}
print(get_order(prereqs))