#!/usr/bin/python3
"""a class rectangle created"""


class Rectangle:
    """attributes go here"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialize class rectangle:
        args: width - width of rectangle
                height - height of rectangle
                """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1 

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

    def area(self):
        """function that returns the area of the rectangle"""
        area = self.__width * self.__height
        return(area)

    def perimeter(self):
        """function that returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__height + self.__width)
        return(perimeter)

    def __str__(self):
        """function to print rectangle in character #"""
        if self.__width == 0 or self.__height == 0:
            return("")
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end='')
            if i == self.__height - 1:
                break
            else:
                print("")
        return(str())

    def __repr__(self):
        """function to print rectangle whe repr is called"""
        return("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """function that deletes the instance created"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
