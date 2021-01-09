"""
Problem:

Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}

You can assume keys do not contain dots in them, i.e. no clobbering will occur.
"""

from typing import Any, Dict


def flatten_dictionary(dictionary: Dict[str, Any]) -> Dict[str, Any]:
    for key in list(dictionary.keys()):
        value = dictionary[key]
        if type(value) == dict:
            value = flatten_dictionary(value)
            del dictionary[key]
            for nested_dictionary_key in value:
                dictionary[f"{key}.{nested_dictionary_key}"] = value[
                    nested_dictionary_key
                ]
    return dictionary


if __name__ == "__main__":
    print(flatten_dictionary({
        "key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "baz": 8
            }
        }
    }))


"""
SPECS:

TIME COMPLEXITY: O(number of key-value pairs)
SPACE COMPLEXITY: O(levels of nesting)
"""
