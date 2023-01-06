#!/usr/bin/python3
import sys
argv = len(sys.argv)
if argv == 0:
    print("0 arguments.")
else:
    print("{} arguments:".format(argv - 1))
    for i in range(1, argv):
        print("{}: {}".format(i, sys.argv[i]))
