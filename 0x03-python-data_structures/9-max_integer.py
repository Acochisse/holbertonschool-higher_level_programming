#!/usr/bin/python
def max_integer(my_list=[]):
    alt = my_list
    if len(alt) == 0:
        return None
    else:
        alt.sort()
        return (alt[-1])
