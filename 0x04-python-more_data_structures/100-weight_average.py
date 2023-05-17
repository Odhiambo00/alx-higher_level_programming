#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list and len(my_list):
        tp = 0
        bt = 0
        for tup in my_list:
            tp += (tup[0] * tup[1])
            bt += (tup[1])
        return (tp / bt)
    return 0

