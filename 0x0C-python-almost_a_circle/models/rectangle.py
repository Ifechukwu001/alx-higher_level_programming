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

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is not greater than 0.

        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is not greater than 0.

        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x-ordinate of the rectangle.

        Raises:
            TypeError: if x is not an integer.
            ValueError: if x is less than 0.

        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y-oordinate of the rectangle.

        Raises:
            TypeError: if y is not an integer.
            ValueError: if y is less than 0.

        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Area method

        Returns:
            int: Area of the rectangle.

        """
        return self.__width * self.__height

    def display(self):
        """ Display method

        """
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()
