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
        self.value = value
        self.name = name
        if not self.value is int:
            raise TypeError(self.name, "must be an integer")
        if self.value <= 0:
            raise ValueError(self.name, "must be greater than 0")
        else:
            return
