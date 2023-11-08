#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)."""
    return sum(set(my_list))

# we can do it with another readable way:
# def uniq_add(my_list=[]):
#     return sum({i for i in my_list})

# we can do it with another readable way:
# def uniq_add(my_list=[]):
#     return sum(list(set(my_list)))

# we can do it with another way:
# def uniq_add(my_list=[]):
#     new_list = []
#     for i in my_list:
#         if i not in new_list:
#             new_list.append(i)
#     return sum(new_list)

# we can do it with list comprehension:
# def uniq_add(my_list=[]):
#     new_list = []
#     [new_list.append(i) for i in my_list if i not in new_list]
#     return sum(new_list)
