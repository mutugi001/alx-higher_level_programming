#!/usr/bin/python3
"""empty class creation"""


class BaseGeometry:
    """class created and attributes go here and methods"""

    def area(self):
        """method area that takes no args and raises an
        exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value"""
        self.name = name
        self.value = value

        if self.value is not int:
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))


"""class rectangle to create a rectangle"""


class Rectangle(BaseGeometry):
    """class rectangle created"""

    def __init__(self, width, height):
        """initialization of class rectangle with args:
        width- width of rectangle
        height - height of rectangle"""
        self.__width = width
        self.__height = height

        BaseGeometry.integer_validator(self, name, value)
        integer_validator("width", self.__width)
        integer_validator("height", self.__height)
