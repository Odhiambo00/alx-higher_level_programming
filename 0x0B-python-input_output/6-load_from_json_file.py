#!/usr/bin/python3

"""
Defines load_from_json function
"""


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”
    """

    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
