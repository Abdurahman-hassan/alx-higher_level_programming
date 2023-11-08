#!/usr/bin/python3

def best_score(a_dictionary):
    """"Returns a key with the biggest integer value."""
    if a_dictionary is None or a_dictionary == {}:
        return None
    return max(a_dictionary, key=lambda k: a_dictionary.get(k))

# we can also use this way:
# if a_dictionary:
#     return max(a_dictionary, key=a_dictionary.get)
# return None

# we can also use this way:
# if a_dictionary:
#     return max(a_dictionary, key=lambda k: a_dictionary[k])
# return None

# we can also use this way:
# if a_dictionary:
#     return max(a_dictionary, key=a_dictionary.get)
