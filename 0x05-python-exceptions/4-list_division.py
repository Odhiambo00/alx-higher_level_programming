#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    fresh_list = []
    for i in range(list_length):
        try:
            qnt = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            qnt = 0
        except ZeroDivisionError:
            print("division by 0")
            qnt = 0
        except IndexError:
            print("out of range")
            qnt = 0
        finally:
            fresh_list.append(qnt)
    return fresh_list
