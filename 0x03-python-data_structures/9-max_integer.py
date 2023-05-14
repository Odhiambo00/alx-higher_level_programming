#!/usr/bin/python3

def max_integer(my_list=[]):
    biggest_int = my_list[0]

    if len(my_list) == 0:
        return
    else:
        for i in my_list[1:]:
            if i > biggest_int:
                biggest_int = i
        return biggest_int
