#!/usr/bin/python3
"""A module containing a rebel class.

"""


class MyInt(int):
    """ MyInt reverses the equal to and not equal to \
    operators.

    """
    def __eq__(self, other):
        """Inverts the equal to sign.

        Returns:
            bool: True if not equal to, False otherwise

        """
        if self - other == 0:
            return False
        return True

    def __ne__(self, other):
        """ Inverts the not equal to sign.

        Returns:
            bool: True if equal to, False otherwise

        """
        if self - other == 0:
            return True
        return False
