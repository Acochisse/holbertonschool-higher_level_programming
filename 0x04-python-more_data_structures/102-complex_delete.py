#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, x in dict(a_dictionary).items():
        if x == value:
            del a_dictionary[key]
    return a_dictionary
