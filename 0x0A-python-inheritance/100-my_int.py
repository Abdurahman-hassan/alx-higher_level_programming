#!/usr/bin/python3
"""Module for MyInt class."""


class MyInt(int):
    """MyInt class.

        args:
            int (int): integer.
    """

    def __eq__(self, other):
        """Equal.

            args:
                other (int): integer.

            returns:
                True if equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Not equal.

            args:
                other (int): integer.

            returns:
                True if not equal, False otherwise.
        """
        return super().__eq__(other)
