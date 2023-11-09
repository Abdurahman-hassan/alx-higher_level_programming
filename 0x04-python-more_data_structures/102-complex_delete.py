#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary."""
    for key in list(a_dictionary.keys()):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary

# we can use another way to do this:
# def complex_delete(a_dictionary, value):
#     """Deletes keys with a specific value in a dictionary."""
#     for key, val in list(a_dictionary.items()):
#         if val == value:
#             del a_dictionary[key]
#     return a_dictionary
