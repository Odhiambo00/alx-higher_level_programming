#!/usr/bin/python3

def multiple_returns(sentence):
    my_sentence = ''
    length = len(sentence)
    if sentence != my_sentence:
        first = sentence[0]
        return (length, first)
    else:
        first = None
        return (length, first)
