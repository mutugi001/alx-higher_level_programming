#!/usr/bin/python3
"""a class rectangle created"""


class Rectangle:
    """attributes go here"""
    def __init__(self, width=0, height=0):
        """initialize class rectangle:
        args: width - width of rectangle
                height - height of rectangle
                """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for attribute width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """setter for attribute width"""
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for attribute height"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """setter for attribute height"""
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
