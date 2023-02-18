#!/usr/bin/python3
"""empty class creation"""


class BaseGeometry:
    """class created and attributes go here and methods"""

    def __init__(self):
        """initialization of class basegeometry"""
        pass

    def area(self, height, width):
        """method area that takes no args and raises an
        exception"""
        self.height = height
        self.width = width
        area = self.width * self.height
        print("[Rectangle] {} {}".format(self.width, self.height))
        return area

    def integer_validator(self, name, value):
        """method that validates value"""
        self.name = name
        self.value = value

        if type(self.name) is not str:
            raise TypeError("{} is not a string".format(self.name))
        if type(self.value) is not int:
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
        BaseGeometry.__init__(self)
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        """method to get the area of rectangle"""
        area = self.__width * self.__height
        print("[Rectangle] {}/{}".format(self.__width, self.__height))
        return area

    def __str__(self):
        """to return a string instead of memory object"""
        return (str())


class Square(Rectangle):
    """a new class square"""

    def __init__(self, size):
        Rectangle.__init__(self, width, height)
        self.__size = size
        Rectangle.area(self, self.__size, self.__size)
        Rectangle.integer_validator(self, self.__size, self.__size)
