#!/usr/bin/env python3
def no_c(my_string):
    stralt = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            stralt += i
    return stralt
