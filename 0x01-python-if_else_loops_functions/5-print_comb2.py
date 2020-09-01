#!/usr/bin/python3
for value in range(00, 100):
    if value == 99:
        print("{:02}".format(value))
    else:
        print("{:02}".format(value), end=", ")
