#!/usr/bin/python3
"""Module containing Student class.

"""


class Student:
    """Student class

    """
    def __init__(self, first_name, last_name, age):
        """ Init method

        Args:
            first_name (str): First Name
            last_name (str): Last Name
            age (int): Age

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Convrt feilds to dict

        """
        return self.__dict__
