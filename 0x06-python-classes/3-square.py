#!/usr/bin/python3
"""defining class square"""


class Square:
    """ creation of class, details and methods of square here"""
    def __init__(self, size=0):
        """initializing square class with
        arguement size which is size of square"""
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """method or function to get area of size"""
        area = self.__size * self.__size
        return(area)
