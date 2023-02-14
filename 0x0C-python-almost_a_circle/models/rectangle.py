#!/usr/bin/python3
""""creating a base class here"""


class Base:
    """class created"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization of class base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


"""creating class rectangle here below"""


class Rectangle(Base):
    """class Rectangle created; attributes and methods to follow"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization of class Rectangle with args
        width, height, x, y and id"""
        Base.__init__(self, id=None)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        if id is not None:
            self.id = id

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        """setter for private attribute width"""
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > than 0")
        else:
            self.__height = value

    @property
    def x(self):
        """getter for attribute x"""
        return(self.__x)

    @x.setter
    def x(self, value):
        """setter for attribute x"""
        if not type(x) is int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """getter for attribute y"""
        return(self.__y)

    @y.setter
    def y(self, value):
        """setter for attribute y"""
        if not type(y) is int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
