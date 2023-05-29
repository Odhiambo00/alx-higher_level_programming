#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        qnt = a / b
    except (TypeError, ZeroDivisionError):
        qnt = None
    finally:
        print("Inside result: {}".format(qnt))
    return qnt
