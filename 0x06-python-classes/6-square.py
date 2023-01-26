#!/usr/bin/python3
"""define class Square below"""


class Square:
    """initialization of class square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter of attribute size"""
        return(self._size)

    @size.setter
    def size(self, value):
        """setterof attribute size"""
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """getter of attribute position"""
        return(self.__position)

    @position.setter
    def position(self, value):
        """setter of attribute position"""
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if i in position < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """method to find area of the square"""
        area = self.__size * self.__size
        return (area)

    def my_print(self):
        """method of printing the square"""
        i = 0
        j = 0
        z = 0
        index = int(self.__position[0])
        if self.__size == 0:
            print("\n", end='')
        if self.__position[1] > 0:
            print("\n", end='')
        for i in range(self.__size):
            for z in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print("")
