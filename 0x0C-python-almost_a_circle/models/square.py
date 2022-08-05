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

    def update(self, *args, **kwargs):
        """ Update method

        Args:
            args (:obj:`tuple`): Variable attributes to be updated.
            kwargs (:obj:`dict`): Variable attributes to be updated.

        """
        keys = ["id", "size", "x", "y"]
        for key, arg in zip(keys, args):
            if key == "id":
                self.id = arg
            elif key == "size":
                self.width = arg
                self.height = arg
            elif key == "x":
                self.x = arg
            elif key == "y":
                self.y = arg

        if len(args) == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def __str__(self):
        """ str magic method

        Returns:
            str: String representation.

        """
        return "[Square] ({}) {}/{} - \
{}".format(self.id, self.x, self.y, self.width)
