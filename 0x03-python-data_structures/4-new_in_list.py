#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if my_list is None:
        return
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list[::]
    # copy list by value not reference,
    # otherwise my_list will be modified
    # or new_list = my_list.copy()
    new_list[idx] = element
    return new_list
