#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys."""
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))

# we can also use the following:
# for key, value in sorted(a_dictionary.items()):
#     print("{}: {}".format(key, value))
