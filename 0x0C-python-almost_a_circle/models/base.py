#!/usr/bin/python3
""" Module containing Base class

"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ To_json_string method

        Args:
            list_dictionaries (:obj:`list` of :obj:`dict`): List of Dictionaries

        Returns:
            str: JSON representation of the list of dictionaries.

        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ From_json_string method

        Args:
            json_string (str): Json representation.

        Returns:
            :obj:`list`: list of dictionary representations.

        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save_to_file method

        Args:
            list_objs (:obj:`list` of :obj:`Rectangle` or :obj:`Square`): List
            of Rectangles or Squares.

        """
        lists = None
        if len(list_objs) > 0:
            lists = []
            for obj in list_objs:
                lists.append(obj.to_dictionary())
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode="w", encoding="utf-8") as outfile:
            outfile.write(cls.to_json_string(lists))

    @classmethod
    def create(cls, **dictionary):
        """ Create method

        Args:
            dictionary (:obj"`dict`): Dictionary containing all the attributes
                                      of the class.

        Returns:
            :obj:`Base` or its subclasses: New instance of the class.

        """
        if cls is Base:
            instance = cls()
        else:
            instance = cls(1, 1)
            instance.update(**dictionary)
        return instance
