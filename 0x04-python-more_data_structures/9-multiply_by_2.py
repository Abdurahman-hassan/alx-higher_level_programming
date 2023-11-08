#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2."""
    return {key: value * 2 for key, value in a_dictionary.items()}

# we can also use this way:
# new_dict = {}
# for key, value in a_dictionary.items():
#     new_dict[key] = value * 2
# return new_dict
