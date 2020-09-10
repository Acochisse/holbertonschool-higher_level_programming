#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    highest = 0
    key = None
    for x, y in a_dictionary.items():
        if y > highest:
            highest = y
            key = x
    return key
