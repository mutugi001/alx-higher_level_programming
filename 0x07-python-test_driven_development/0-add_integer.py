#!/usr/bin/python3
#doctest_0-add_integer.txt
def add_integer(a, b=98):
    """function to add integers together 
        args:
        a: integer 1
        b: interger 2
        returns a + b
    """
    """
    >>>add_integer(2, 3)
    6
    >>>add_integer(3, 4)
    7
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return(int(a) + int(b))
