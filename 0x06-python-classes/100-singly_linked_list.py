#!/usr/bin/python3
class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value == None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        self.__new = Node(value)
        if self.__head == None:
            self.__head = self.__new
        
        elif self.__new.data < self.__head.data:
            self.__new.next_node = self.__head
            self.__head = self.__new
        
        else:
            self.__current = self.__head
            while (self.__current.next_node):
                if ((self.__current.data <= self.__new.data) and
                (self.__new.data <= self.__current.next_node.data)):
                    self.__new.next_node = self.__current.next_node
                    self.__current.next_node = self.__new
                    break
                self.__current = self.__current.next_node
                    
            if self.__current.next_node == None:
                self.__current.next_node = self.__new
            self.__current = None
        self.__new = None


    def __str__(self):
        self.__str_out = ""
        self.__current = self.__head
        while self.__current:
            self.__str_out += "{}".format(self.__current.data)
            self.__current = self.__current.next_node
            if self.__current:
                self.__str_out += "\n"
        self.__current = None
        return self.__str_out
