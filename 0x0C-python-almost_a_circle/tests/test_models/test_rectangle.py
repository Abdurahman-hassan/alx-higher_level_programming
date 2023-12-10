#!/usr/bin/python3

"""Defines a test rectangle class."""

import unittest

from models.rectangle import Rectangle


class TestRectangleTestInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_create_rectangle_with_valid_parameters(self):
        """Creating a Rectangle instance
        with valid width, height, x, y, and id parameters."""
        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 1)

    def test_get_attributes(self):
        """Getting the width, height, x, y,
        and id attributes of a Rectangle instance."""
        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 1)

    def test_set_attributes(self):
        """Setting the width, height, x, y,
        and id attributes of a Rectangle instance."""
        rectangle = Rectangle(5, 10, 2, 3, 1)
        rectangle.width = 7
        rectangle.height = 12
        rectangle.x = 4
        rectangle.y = 5
        rectangle.id = 2
        self.assertEqual(rectangle.width, 7)
        self.assertEqual(rectangle.height, 12)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)
        self.assertEqual(rectangle.id, 2)

    def test_create_rectangle_with_maximum_parameters(self):
        """Creating a Rectangle instance with maximum allowed parameters."""
        rectangle = Rectangle(55, 66, 77, 88, 99)
        self.assertEqual(rectangle.width, 55)
        self.assertEqual(rectangle.height, 66)
        self.assertEqual(rectangle.x, 77)
        self.assertEqual(rectangle.y, 88)
        self.assertEqual(rectangle.id, 99)
