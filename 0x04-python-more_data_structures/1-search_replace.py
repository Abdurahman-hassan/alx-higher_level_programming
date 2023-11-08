#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return [replace if i == search else i for i in my_list]

    # we can do it with another readable way:
    # for i in range(len(my_list)):
    #     if my_list[i] == search:
    #         my_list[i] = replace
    # return my_list
    # or this way:
    # for i, v in enumerate(my_list):
    #     if v == search:
    #         my_list[i] = replace
    # return my_list
    # or this way:
    # for i in my_list:
    #     if i == search:
    #         my_list[my_list.index(i)] = replace
    # return my_list
