#!/usr/bin/python3

"""
A function that prints a text with 2 new lines after each of
these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints indented text

    Args:
        text (str): Text to be printed

    Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()

    str_result = ''
    chars = ['.', '?', ':']

    for char in text:
        if char.isspace() and str_result.endswith('\n'):
            continue
        else:
            str_result += char
        if char in chars:
            str_result += '\n\n'
    print(str_result)
