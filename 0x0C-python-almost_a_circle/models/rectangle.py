#!/usr/bin/python3
""" Module containing Rectangle class.

"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init method

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x-ordinate of the rectangle.
            y (int): y-ordinate of the rectangle.
            id (int): id of the object.

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Width of the rectangle.

        """
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """ Height of the rectangle.

        """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """ x-ordinate of the rectangle.

        """
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """ y-oordinate of the rectangle.

        """
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
