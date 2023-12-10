#!/usr/bin/python3


"""Defines a test for the Base class."""

import sys
import unittest
from io import StringIO

from models.base import Base


class TestBaseTestInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class.

        Attributes:
            __nb_objects (int): The number of instantiated Bases.
    """

    def setUp(self):
        """Imports module, instantiates class"""
        sys.stdout = StringIO()
        Base._Base__nb_objects = 0

    def test_init_with_no_arguments(self):
        """Initializes a new Base object with no arguments."""
        base = Base()
        self.assertEqual(base.id, 1)

    def test_init_with_integer_argument(self):
        """Initializes a new Base object with an integer argument."""
        base = Base(5)
        self.assertEqual(base.id, 5)

    def test_init_with_string_argument(self):
        """Initializes a new Base object with a string argument."""
        base = Base("abc")
        self.assertEqual(base.id, "abc")

    def test_init_with_negative_integer_argument(self):
        """Initializes a new Base object with a negative integer argument."""
        base = Base(-10)
        self.assertEqual(base.id, -10)

    def test_init_with_float_argument(self):
        """Initializes a new Base object with a float argument."""
        base = Base(3.14)
        self.assertEqual(base.id, 3.14)

    def test_init_with_boolean_argument(self):
        """Initializes a new Base object with a boolean argument."""
        base = Base(True)
        self.assertEqual(base.id, True)

    def test_init_with_large_integer_argument(self):
        """Initializes a new Base object with a large integer argument."""
        base = Base(1000000000000000000000000)
        self.assertEqual(base.id, 1000000000000000000000000)

    def test_init_with_none_argument(self):
        """Initializes a new Base object with a None argument."""
        base = Base(None)
        self.assertEqual(base.id, 1)

    def test_init_with_list_argument(self):
        """Initializes a new Base object with a list argument."""
        base = Base([1, 2, 3])
        self.assertEqual(base.id, [1, 2, 3])

    def test_id(self):
        """
        Test check for id
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(3)
        b5 = Base()
        b6 = Base(0)
        b7 = Base(-1)
        b8 = Base(2)
        b9 = Base(11)
        b10 = Base(12)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, 4)
        self.assertEqual(b6.id, 0)
        self.assertEqual(b7.id, -1)
        self.assertEqual(b8.id, 2)
        self.assertEqual(b9.id, 11)
        self.assertEqual(b10.id, 12)
