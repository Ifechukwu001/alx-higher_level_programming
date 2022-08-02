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

    def to_json(self, attrs=None):
        """Convert feilds to dict

        """
        if type(attrs) is list:
            att_dict = {}
            for attr in attrs:
                value = self.__dict__.get(attr)
                if value:
                    att_dict[attr] = value
            return att_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Converts dict to feilds

        """
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
