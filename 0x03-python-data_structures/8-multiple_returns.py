#!/usr/bin/python3
def multiple_returns(sentence):
    list = [0, 1]
    if sentence != "":
        list[0] = len(sentence)
        list[1] = sentence[0]
    else:
        list[0] = len(sentence)
        list[1] = None
    ret_tuple = tuple(list)
    return (ret_tuple)
