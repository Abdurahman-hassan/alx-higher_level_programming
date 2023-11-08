#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary."""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

# we can also use this way:
# a_dictionary.pop(key, None)
# return a_dictionary
# but this way is not recommended, because it will raise a KeyError if the key
# doesn't exist in the dictionary.
