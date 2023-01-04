#!/usr/bin/python3
def islower(c):
    if ord(c) in range(97, 123):
        for i in range(97, 123):
            if c != chr(i):
                return(False)
            else:
            	return(True)
    else:
        return(False)
