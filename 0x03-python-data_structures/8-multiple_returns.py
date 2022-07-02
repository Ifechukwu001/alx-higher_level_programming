#!/usr/bin/python3
def multiple_returns(sentence):
    first = None
    str_len = len(sentence)
    if str_len > 0:
        first = sentence[0]
    return str_len, first
