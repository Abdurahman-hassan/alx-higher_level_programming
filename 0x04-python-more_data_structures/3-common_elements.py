#!/usr/bin/python3

def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets."""
    return set_1 & set_2

# we can also use the intersection method
# return set_1.intersection(set_2)
# this will return a set of common elements in two sets {'C'}
