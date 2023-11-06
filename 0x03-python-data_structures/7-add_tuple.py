#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # ensure tuple_a has at least 2 elements
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    tuple_sum = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return tuple_sum
