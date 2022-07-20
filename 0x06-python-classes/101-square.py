#!/usr/bin/python3
class Square:
    """ Square class with setter and getter to private feild 
        Also it contains
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        
    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size + self.__position[1]):
                if i < self.__position[1]:
                    print()
                    continue
                for j in range(self.__size + self.__position[0]):
                    if j < self.__position[0]:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()

    def __str__(self):
        self.__str_out = ""
        if self.__size == 0:
            self.__str_out += "\n"
        else:
            for i in range(self.__size + self.__position[1]):
                if i < self.__position[1]:
                    self.__str_out += "\n"
                    continue
                for j in range(self.__size + self.__position[0]):
                    if j < self.__position[0]:
                        self.__str_out += " "
                    else:
                        self.__str_out += "#"
                self.__str_out += "\n"
        return self.__str_out
