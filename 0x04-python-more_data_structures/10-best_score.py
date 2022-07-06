#!/usr/bin/python3
def best_score(a_dictionary):
    max_key = None
    max_score = -99999999
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > max_score:
                max_score = value
                max_key = key
    return max_key
