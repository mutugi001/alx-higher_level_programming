#!/usr/bin/python3
"""definition of class Square"""


class Square:
    """class square with its methods and attributes here"""
    def __init__(self, size=0):
        """initializing square class with args size"""
        self.__size = size

    @property
    def size(self):
        """getter of attribute size"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """setting the attribute value"""
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """finding the area of the square"""
        area = self.__size * self.__size
        return(area)
