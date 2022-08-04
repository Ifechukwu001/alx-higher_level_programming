#!/usr/bin/python3
""" Module containing Base class

"""


class Base:
    """ Base class

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Init method

        Args:
            id (int): Id of the object.

        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
