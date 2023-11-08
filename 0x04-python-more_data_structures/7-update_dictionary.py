#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary."""
    a_dictionary[key] = value
    return a_dictionary

# we can also use the update() method
# a_dictionary.update({key: value})
# return a_dictionary
