#!/usr/bin/python3
"""A module containing a BaseGeometry class

"""


class BaseGeometry:
    """An empty class

    """
    def area(self):
        """A non-functional method

        Raises:
            Exception: As it was not implemented.

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if the value passed is an integer.

        Args:
            name (str): name of the value.
            value (int): value associated to the name.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is not greater than zero.

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))



class Rectangle(BaseGeometry):
    """A Rectangle class

    """
    def __init__(self, width, height):
        """ init method of the class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of a rectangle.

        """
        self.integer_validator("Width", width)
        self.integer_validator("Height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area method of the class.

        Returns:
            int: area of the rectangle.

        """
        return self.__width * self.__height

    def __str__(self):
        """String representation.

        Returns:
            str: String representation.

        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)



class Square(Rectangle):
    """A Square class

    """
    def __init__(self, size):
        """ Init method of the class.

        Args:
            size (int) : Length of the square.

        """
        self.integer_validator("Size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Area of the square.

        Returns:
            int: area of the square.

        """
        return self.__size * self.__size
