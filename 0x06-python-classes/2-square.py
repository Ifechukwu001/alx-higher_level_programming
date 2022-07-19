#!/usr/bin/python3
class Square:
    """ Square class with setter to private feild """
    def __init__(self, size=0):
        self.size_s = size

    @property
    def size_s(self):
        return self.__size

    @size_s.setter
    def size_s(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
