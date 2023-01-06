#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = len(sys.argv)
    if argv == 1:
        print("0 arguments.")
    elif argv == 2:
        print("{} arguement:".format(argv - 1))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(argv - 1))
        for i in range(1, argv):
            print("{}: {}".format(i, sys.argv[i]))
