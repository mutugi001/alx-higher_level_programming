#!/usr/bin/python3
import sys
argv = len(sys.argv)
if argv == 0:
    print("0 arguments.")
if argv == 2:
    print("{} arguement:".format(argv - 1))
    print("1: {}".format(sys.argv[1]))
else:
    print("{} arguments:".format(argv - 1))
    for i in range(1, argv):
        if argv == 1:
            print("{}: {}".format(i, sys.argv[i]))
