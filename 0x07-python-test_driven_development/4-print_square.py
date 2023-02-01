#!/usr/bin/python3
def print_square(size):
    """function that prints the size of a aquare using the character #
    args size is the size of the square
    """
    if not (isinstance(size, int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#",end='')
        print("")
