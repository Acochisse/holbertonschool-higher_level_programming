#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv):
    if n == 1:
        print("{} arguments. ".format(n - 1))
    elif n == 2:
        print("{} argument:".format(n - 1))
    else:
        print("{} arguments:".format(n - 1))
    for i in range(1, n):
        print("{:d}: {:s}".format(i, argv[i]))
