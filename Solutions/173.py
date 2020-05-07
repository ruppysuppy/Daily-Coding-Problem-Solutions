'''
Problem:

Write a function to flatten a nested dictionary. Namespace the keys with a period.

Example:

Input =
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
Output =
{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
'''

# FUNCTION TO PERFORM THE OPERATION
def flatten_dict(dictionary):
    # getting the keys in a list (essential as dict_keys would not permit dictionary modification while iterating)
    keys = list(dictionary.keys())

    # iterating through the keys
    for key in keys:
        # getting the value for the key
        temp = dictionary[key]

        # if the value is a dictionary
        if (type(temp) == dict):
            # its flattened recursively
            temp = flatten_dict(temp)
        
            # the value in the dictionary is deleted
            del dictionary[key]

            # the flatted dictionary is added to the parent dictionary using the convention "<key>.<children_keys>"
            for j in temp:
                dictionary[key + f".{j}"] = temp[j]
    
    return dictionary

# DRIVER CODE
print(flatten_dict({
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}))