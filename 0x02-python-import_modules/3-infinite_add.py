#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    totals = 0
    argv = len(sys.argv)
    for i in range(1, argv):
        totals = totals + int(sys.argv[i])
    print("{}".format(totals))
