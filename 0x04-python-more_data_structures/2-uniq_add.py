#!/usr/bin/python3

"""
adds all unique integers in a list (only once for each integer)
"""


def uniq_add(my_list=[]):
    new_list = list(set(my_list))
    add = sum(new_list)
    return add
