#!/usr/bin/python3
"""A module containing a Square class.

"""


class Square:
    """A Square class.

    """
    def __init__(self, size=0, position=(0, 0)):
        """init method of the class.

        Args:
           size (int): Width of the square.
           position (:obj: `tuple`): x, y coordinate of the square.


        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: size of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than zero.

        """
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
        """:obj: `tuple`: Coordinate of the square.

        Raises:
            TypeError: if position is not a positive tuple of length 2.

        """
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2
        and isinstance(value[0], int) and isinstance(value[1], int)
        and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """area method of the class.

        Returns:
            int: area of the square.

        """
        return self.__size * self.__size

    def my_print(self):
        """my_print method of the class.

        """
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
