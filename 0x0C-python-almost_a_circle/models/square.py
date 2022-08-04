#!/usr/python3
""" Module containing the Square class.

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class.

    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Init method

        Args:
            size (int): Size of the square.
            x (int): x-ordinate of the square.
            y (int): y-ordinate of the square.
            id (int): Id of the object.

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Size of the square.

        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """ str magic method

        Returns:
            str: String representation.

        """
        return "[Square] ({}) {}/{} - \
{}".format(self.id, self.x, self.y, self.width)
