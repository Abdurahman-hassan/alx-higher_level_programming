#!/usr/bin/python3

def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple (<score>, <weight>)"""
    if my_list == []:
        return 0
    else:
        return (sum([x[0] * x[1] for x in my_list])
                / sum([x[1] for x in my_list]))

# we can also use the map function to do the same thing
# def weight_average(my_list=[]):
#     if my_list == []:
#         return 0
#     else:
#         return sum(map(lambda x: x[0] * x[1], my_list))
#         / sum(map(lambda x: x[1], my_list))
