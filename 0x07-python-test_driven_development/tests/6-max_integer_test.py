#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test the max_integer function
    """

    def test_none(self):
        """Test for None
        """
        self.assertEqual(max_integer(), None)

    def test_empty(self):
        """Test for empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_max(self):
        """Test for max
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_end(self):
        """Test for max at the end
        """
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_max_middle(self):
        """Test for max in the middle
        """
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_max_negative(self):
        """Test for max negative
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_float(self):
        """Test for max float
        """
        self.assertEqual(max_integer([1.2, 2.3, 3.4, 4.5]), 4.5)

    def test_max_string(self):
        """Test for max string
        """
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')

    def test_with_empty(self):
        """Test for list with empty list
        """
        self.assertEqual(max_integer([[1, 2, 3], [], [4, 5, 6]]), [4, 5, 6])

    def test_one_element(self):
        """Test for list with one element
        """
        self.assertEqual(max_integer([1]), 1)

    def test_one_negative(self):
        """Test for list with one negative
        """
        self.assertEqual(max_integer([-1]), -1)

    def test_no_param(self):
        """Test for no param
        """
        self.assertEqual(max_integer(), None)

    def test_float_with_int_with_string(self):
        """Test for list with float, int and string
        """
        with self.assertRaises(TypeError):
            max_integer([1.2, 2, 'a'])

    def test_string(self):
        """Test for string
        """
        self.assertEqual(max_integer('string'), 't')

    def test_tuple(self):
        """Test for tuple
        """
        self.assertEqual(max_integer((1, 2, 3)), 3)

    def test_tuple_with_string_and_numbers(self):
        """Test for tuple with string and numbers
        """
        with self.assertRaises(TypeError):
            max_integer((1, 2, 'a'))

    def test_tuple_with_empty(self):
        """Test for tuple with empty tuple
        """
        with self.assertRaises(TypeError):
            max_integer((1, 2, ()))

    def test_none2(self):
        """Test for None
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_list_of_none(self):
        """Test for list of None
        """
        with self.assertRaises(TypeError):
            max_integer([None, None, None])

    def test_list_of_list(self):
        """Test for list of list
        """
        self.assertEqual(max_integer([[1, 2, 3], [4, 5, 6]]), [4, 5, 6])

    def test_list_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([2, 5, 234, [23, 78], 133])
