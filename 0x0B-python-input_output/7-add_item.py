#!/usr/bin/python3

"""
Defines a module that loads and saves
"""

import sys
import json

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file =\
            __import__('6-load_from_json_file').load_from_json_file

def add_item():
    """
    Adds arguments to python list
    """

    try:
    items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        items = []

    for args in sys.argv[1:]:
        items.append(args)

    save_to_json_file(items, 'add_item.json')

add_item()
