#!/usr/bin/python3
"""A module containing the Rectangle class.

"""


class Rectangle:
    """A rectangle class.

    Attributes:
        number_of_instances (int): Number of objects of the class.

    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """init method

        Initialises the width and height of the class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """The width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than zero.

        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The height of the rectangle

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than zero.

        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """The area of the rectangle

        Returns:
           int: Area of the rectangle.

        """
        return self.__width * self.__height

    def perimeter(self):
        """The perimeter of the rectangle

        Returns:
            int: Perimeter of the rectangle.

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Pretty String of the class.

        Returns:
            str: Pretty String.

        """
        str_rep = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                str_rep += "#"
            str_rep += "\n"
        return str_rep

    def __repr__(self):
        """String representation of class

        Returns:
            str: String representation

        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Destructor of the class

        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1