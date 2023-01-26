#!/usr/bin/python3
"""class square definition"""


class Square:
    """details of class square and attributes"""
    def __init__(self, size=0):
        """initialization of square
        Args : size giving the size of Square"""
        if type(size) is int:
            self.__size = size
        else:
            """raising errors of type and value and exceptions"""
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
