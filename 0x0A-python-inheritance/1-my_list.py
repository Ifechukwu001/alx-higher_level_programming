#!/usr/bin/python3
"""A module containing MyList class.

"""


class MyList(list):
    """MyList class - a subclass of the list class.

    """

    def print_sorted(self):
        """Prints the MyList in a sorted manner.

        """
        print(sorted(self))
