#!/usr/bin/env python3
def no_c(my_string):
    stralt = ""
    for i in my_string:
        if my_string[i] != 'c' and my_string[i] != 'C':
            stralt += i
    return stralt
