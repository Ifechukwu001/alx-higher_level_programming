#!/usr/bin/python3
"""A module containing a Node class and a SinglyLinkedList class.

"""


class Node:
    """A Node class.

    """
    def __init__(self, data, next_node=None):
        """init method of the class.

        Args:
            data (int): Number data of the node.
            next_node (:obj:`Node`, optional): Reference to the next node.

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: data number of the node.

        Raises:
            TypeError: if data is not an integer.

        """
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """:obj:`Node`: Reference to the next node.

        Raises:
            TypeError: if next_node is not an object of Node or None.

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """A SinglyLinkedList class.

    """
    def __init__(self):
        """init method of the class.

        """
        self.__head = None

    def sorted_insert(self, value):
        """sorted_insert method of the class.

        Args:
            value (int): Data number of the new node.

        """
        self.__new = Node(value)
        if self.__head is None:
            self.__head = self.__new

        elif self.__new.data < self.__head.data:
            self.__new.next_node = self.__head
            self.__head = self.__new

        else:
            self.__current = self.__head
            while self.__current.next_node:
                if (self.__current.data <= self.__new.data) and
                (self.__new.data <= self.__current.next_node.data):
                    self.__new.next_node = self.__current.next_node
                    self.__current.next_node = self.__new
                    break
                self.__current = self.__current.next_node

            if self.__current.next_node is None:
                self.__current.next_node = self.__new
            self.__current = None
        self.__new = None

    def __str__(self):
        """__str___ method of class.

        Returns:
            str: String representation of all the nodes in the list.

        """
        self.__str_out = ""
        self.__current = self.__head
        while self.__current:
            self.__str_out += "{}".format(self.__current.data)
            self.__current = self.__current.next_node
            if self.__current:
                self.__str_out += "\n"
        self.__current = None
        return self.__str_out
