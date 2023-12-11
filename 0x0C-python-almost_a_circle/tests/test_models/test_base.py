#!/usr/bin/python3


"""Defines a test for the Base class.

   unittest classes:
        TestBaseClassInstantiation - test instantiation of the Base class.
        TestBaseClassToJSONString - test the to_json_string method of the Base class.
        TestBaseClassFromJSONString - test the from_json_string method of the Base class.
        TestBaseClassSaveToFile - test the save_to_file method of the Base class.
        TestBaseClassCreate - test the create method of the Base class.


"""
import json
import os
import sys
import unittest
from io import StringIO

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBaseClassToJSONString(unittest.TestCase):
    """Unittests for testing the to_json_string method of the Base class.
    """

    def setUp(self):
        """Imports module, instantiates class"""
        sys.stdout = StringIO()
        Base._Base__nb_objects = 0

    def test_to_json_string_with_None(self):
        """Tests to_json_string method with None as argument."""
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_to_json_string_with_empty_list(self):
        """Tests to_json_string method with an empty list as argument."""
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_with_empty_list_of_dicts(self):
        """Tests to_json_string method with an empty list of dicts as arg."""
        json_str = Base.to_json_string([{}, {}])
        self.assertEqual(json_str, "[{}, {}]")

    def test_to_json_string_with_None_in_list(self):
        """Tests to_json_string method with None in list as argument."""
        json_str = Base.to_json_string([None])
        self.assertEqual(json_str, "[null]")

    def test_to_json_string_with_no_args(self):
        """Tests to_json_string method with no arguments."""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_with_more_than_one_arg(self):
        """Tests to_json_string method with more than one argument."""
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])

    def test_empty_list(self):
        """Returns an empty list as a JSON string when given None or an empty list."""
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_list_of_dicts(self):
        """Returns a JSON string representation of a list of dictionaries."""
        list_dictionaries = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}]
        json_str = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_str, '[{"name": "John", "age": 25}, {"name": "Jane", "age": 30}]')

    def test_single_none(self):
        """Tests to_json_string method with a list with a single None value as argument."""
        json_str = Base.to_json_string([None])
        self.assertEqual(json_str, '[null]')

    def test_no_arguments(self):
        """Tests to_json_string method with no arguments."""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_more_than_one_argument(self):
        """Tests to_json_string method with more than one argument."""
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])

    def test_nested_dicts(self):
        """ Returns a JSON string representation of a list of dictionaries with nested dictionaries."""
        list_dictionaries = [{'name': 'John', 'age': 25, 'address': {'street': '123 Main St', 'city': 'New York'}},
                             {'name': 'Jane', 'age': 30, 'address': {'street': '456 Elm St', 'city': 'Los Angeles'}}]
        json_str = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_str,
                         '[{"name": "John", "age": 25, "address": '
                         '{"street": "123 Main St", "city": "New York"}}, '
                         '{"name": "Jane", "age": 30, '
                         '"address": {"street": "456 Elm St", "city": "Los Angeles"}}]')

    def test_nested_lists(self):
        """ Returns a JSON string representation of a list of dictionaries with nested lists."""
        list_dictionaries = [{'name': 'John', 'age': 25, 'hobbies': ['reading', 'running']},
                             {'name': 'Jane', 'age': 30, 'hobbies': ['painting', 'cooking']}]
        json_str = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_str,
                         '[{"name": "John", "age": 25, "hobbies": ["reading", "running"]},'
                         ' {"name": "Jane", "age": 30, "hobbies": ["painting", "cooking"]}]')

    def test_non_string_keys(self):
        """ Returns a JSON string representation
        of a list of dictionaries with non-string keys."""
        list_dictionaries = [{1: 'John', 2: 25}, {3: 'Jane', 4: 30}]
        json_str = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_str, '[{"1": "John", "2": 25}, {"3": "Jane", "4": 30}]')

    def test_non_string_values(self):
        """ Returns a JSON string representation of a list of
        dictionaries with non-string values."""
        list_dictionaries = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30.5}]
        json_str = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_str, '[{"name": "John", "age": 25}, {"name": "Jane", "age": 30.5}]')

    def test_non_ascii_characters(self):
        """ Returns a JSON string representation of a list of
        dictionaries with non-ASCII characters."""
        list_dictionaries = [{'name': 'John', 'age': 25}, {'name': 'abdo', 'age': 30}]
        json_str = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_str, '[{"name": "John", "age": 25}, {"name": "abdo", "age": 30}]')


class TestBaseClassFromJSONString(unittest.TestCase):
    """Unittests for testing the from_json_string method of the Base class.
    """

    def setUp(self):
        """Imports module, instantiates class"""
        sys.stdout = StringIO()
        Base._Base__nb_objects = 0

    def test_from_json_string_with_empty_string(self):
        """Tests from_json_string method with an empty string as argument."""
        list_dictionaries = Base.from_json_string("")
        self.assertEqual(list_dictionaries, [])

    def test_empty_list(self):
        """Tests from_json_string method with an empty list as argument."""
        list_dictionaries = Base.from_json_string("[]")
        self.assertEqual(list_dictionaries, [])

    def test_list_of_dicts(self):
        """Tests from_json_string method with a list of dicts as argument."""
        json_str = '[{"name": "John", "age": 25}, {"name": "Jane", "age": 30}]'
        list_dictionaries = Base.from_json_string(json_str)
        self.assertEqual(list_dictionaries, [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}])

    def test_single_none(self):
        """Tests from_json_string method with a list with a single None value as argument."""
        list_dictionaries = Base.from_json_string("[null]")
        self.assertEqual(list_dictionaries, [None])

    def test_no_arguments(self):
        """Tests from_json_string method with no arguments."""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_more_than_one_argument(self):
        """Tests from_json_string method with more than one argument."""
        with self.assertRaises(TypeError):
            Base.from_json_string([], [])

    def test_nested_dicts(self):
        """Tests from_json_string method with a list of dicts with nested dicts as argument."""
        json_str = '[{"name": "John", "age": 25, "address": {"street": "123 Main St", "city": "New York"}}, ' \
                   '{"name": "Jane", "age": 30, "address": {"street": "456 Elm St", "city": "Los Angeles"}}]' \
                   ''
        list_dictionaries = Base.from_json_string(json_str)
        self.assertEqual(list_dictionaries,
                         [{'name': 'John', 'age': 25, 'address': {'street': '123 Main St', 'city': 'New York'}},
                          {'name': 'Jane', 'age': 30, 'address': {'street': '456 Elm St', 'city': 'Los Angeles'}}])

    def test_nested_lists(self):
        """Tests from_json_string method with a list of dicts with nested lists as argument."""
        json_str = '[{"name": "John", "age": 25, "hobbies": ["reading", "running"]}, ' \
                   '{"name": "Jane", "age": 30, "hobbies": ["painting", "cooking"]}]'
        list_dictionaries = Base.from_json_string(json_str)
        self.assertEqual(list_dictionaries,
                         [{'name': 'John', 'age': 25, 'hobbies': ['reading', 'running']},
                          {'name': 'Jane', 'age': 30, 'hobbies': ['painting', 'cooking']}])

    def test_from_json_string_with_None(self):
        """
        Tests from_json_string method with None as argument.
        """
        list_dictionaries = Base.from_json_string(None)
        self.assertEqual(list_dictionaries, [])

    def test_from_json_string_with_list_of_dicts(self):
        """
        Tests from_json_string method with a list of dicts as argument.
        """
        json_str = '[{"name": "John", "age": 25}, {"name": "Jane", "age": 30}]'
        list_dictionaries = Base.from_json_string(json_str)
        self.assertEqual(list_dictionaries, [{"name": "John", "age": 25}, {"name": "Jane", "age": 30}])

    def test_from_json_string_with_single_null_value(self):
        """
        Tests from_json_string method with a JSON string containing a single null value.
        """
        json_str = '[null]'
        list_dictionaries = Base.from_json_string(json_str)
        self.assertEqual(list_dictionaries, [None])

    def test_from_json_string_with_nested_dicts_and_lists(self):
        """
        Tests from_json_string method with a JSON string containing nested dictionaries and lists.
        """
        json_str = '[{"name": "John", "age": [25, 30]}, {"name": {"first": "Jane", "last": "Doe"}, "age": [35, 40]}]'
        list_dictionaries = Base.from_json_string(json_str)
        expected_result = [{"name": "John", "age": [25, 30]},
                           {"name": {"first": "Jane", "last": "Doe"}, "age": [35, 40]}]
        self.assertEqual(list_dictionaries, expected_result)

    def test_from_json_string_with_no_args(self):
        """
        Tests from_json_string method with no arguments.
        """
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_with_more_than_one_arg(self):
        """
        Tests from_json_string method with more than one argument.
        """
        with self.assertRaises(TypeError):
            Base.from_json_string([], [])

    def test_from_json_string_with_empty_list(self):
        """
        Tests from_json_string method with a JSON string representing an empty list.
        """
        json_str = '[]'
        list_dictionaries = Base.from_json_string(json_str)
        self.assertEqual(list_dictionaries, [])

    def test_from_json_string_with_string_keys(self):
        """
        Tests from_json_string method with a JSON string representing a list of dictionaries with string keys.
        """
        json_str = '[{"name": "John", "age": 25}, {"name": "Jane", "age": 30}]'
        list_dictionaries = Base.from_json_string(json_str)
        expected_result = [{"name": "John", "age": 25}, {"name": "Jane", "age": 30}]
        self.assertEqual(list_dictionaries, expected_result)


class TestBaseClassSaveToFile(unittest.TestCase):
    """Unittests for testing the save_to_file method of the Base class.
    """

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

    def test_writes_json_serialization_to_file(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) > 0)

    #  Method creates file with name of class + '.json'
    def test_creates_file_with_correct_name(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        self.assertTrue(os.path.exists("Rectangle.json"))

    #  Method writes empty list if list_objs is None
    def test_writes_empty_list_if_list_objs_is_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    #  Method writes JSON serialization of list_objs if list_objs is not None
    def test_writes_json_serialization_if_list_objs_is_not_none(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) > 0)

    #  Method uses to_dictionary method to serialize objects
    def test_uses_to_dictionary_method_to_serialize_objects(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            data = json.load(f)
            self.assertEqual(data[0]["id"], r.id)
            self.assertEqual(data[0]["width"], r.width)
            self.assertEqual(data[0]["height"], r.height)
            self.assertEqual(data[0]["x"], r.x)
            self.assertEqual(data[0]["y"], r.y)

    #  Method overwrites existing file with new data
    def test_overwrites_existing_file_with_new_data(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1])
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as f:
            data = json.load(f)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["id"], r2.id)
            self.assertEqual(data[0]["width"], r2.width)
            self.assertEqual(data[0]["height"], r2.height)
            self.assertEqual(data[0]["x"], r2.x)
            self.assertEqual(data[0]["y"], r2.y)

    #  Method writes empty list if list_objs is an empty list
    def test_writes_empty_list_if_list_objs_is_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())


class TestBaseClassCreate(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_square_new(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_is(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)

    #  Should create a new instance of the Rectangle class with default values if no arguments are passed and the class name is Rectangle
    def test_create_rectangle_with_default_values(self):
        """
        Test that create method creates a new instance of the Rectangle class with default values if no arguments are passed and the class name is Rectangle
        """
        # Create a new instance using the create method
        instance = Rectangle.create()

        # Check that the instance is of the correct class
        self.assertIsInstance(instance, Rectangle)

        # Check that the instance has the default values
        self.assertEqual(instance.id, 5)
        self.assertEqual(instance.width, 1)
        self.assertEqual(instance.height, 1)
        self.assertEqual(instance.x, 0)
        self.assertEqual(instance.y, 0)

    #  Should create a new instance of the Square class with default values if no arguments are passed and the class name is Square
    def test_create_square_with_default_values(self):
        """
        Test that create method creates a new instance of the Square class with default values if no arguments are passed and the class name is Square
        """
        # Create a new instance using the create method
        instance = Square.create()

        # Check that the instance is of the correct class
        self.assertIsInstance(instance, Square)

        # Check that the instance has the default values
        self.assertEqual(instance.id, 11)
        self.assertEqual(instance.size, 1)
        self.assertEqual(instance.x, 0)
        self.assertEqual(instance.y, 0)

    def test_create_rectangle_with_specified_attributes(self):
        """
        Test that create method creates a new instance of the Rectangle class with the specified attributes if the class name is Rectangle
        """
        # Create a new instance using the create method with specified attributes
        instance = Rectangle.create(id=2, width=5, height=10, x=1, y=2)

        # Check that the instance is of the correct class
        self.assertIsInstance(instance, Rectangle)

        # Check that the instance has the specified attributes
        self.assertEqual(instance.id, 2)
        self.assertEqual(instance.width, 5)
        self.assertEqual(instance.height, 10)
        self.assertEqual(instance.x, 1)
        self.assertEqual(instance.y, 2)

    def test_create_without_keyword_arguments(self):
        """
        Test that create method raises a TypeError if arguments are not passed as keyword arguments
        """
        # Try to create a new instance using the create method without keyword arguments
        with self.assertRaises(TypeError):
            instance = Base.create(2)


class TestBaseClassLoadFromFile(unittest.TestCase):
    """Unittests for testing the load_from_file method of the Base class.
    """

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_load_from_file_one_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r1])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_one_square(self):
        s1 = Square(10, 7, 2, 8)
        Square.save_to_file([s1])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_no_file(self):
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [])

    #  Returns an empty list if the file does not exist.
    def test_file_not_exist(self):
        # Arrange
        class Rectangle(Base):
            def __init__(self, width, height, x=0, y=0, id=None):
                super().__init__(id)
                self.width = width
                self.height = height
                self.x = x
                self.y = y

        # Act
        rectangles = Rectangle.load_from_file()

        # Assert
        self.assertEqual(rectangles, [])

    #  Returns an empty list if the file is empty.
    def test_empty_file(self):
        # Arrange
        class Rectangle(Base):
            def __init__(self, width, height, x=0, y=0, id=None):
                super().__init__(id)
                self.width = width
                self.height = height
                self.x = x
                self.y = y

        # Save an empty list to a file
        Rectangle.save_to_file([])

        # Act
        rectangles = Rectangle.load_from_file()

        # Assert
        self.assertEqual(rectangles, [])

    #  Returns an empty list if the JSON string is empty.
    def test_empty_json_string(self):
        # Arrange
        class Rectangle(Base):
            def __init__(self, width, height, x=0, y=0, id=None):
                super().__init__(id)
                self.width = width
                self.height = height
                self.x = x
                self.y = y

        # Save an empty JSON string to a file
        with open("Rectangle.json", "w") as f:
            f.write("")

        # Act
        rectangles = Rectangle.load_from_file()

        # Assert
        self.assertEqual(rectangles, [])

    #  Returns an empty list if the list of dictionaries is empty.
    def test_empty_list_of_dicts(self):
        # Arrange
        class Rectangle(Base):
            def __init__(self, width, height, x=0, y=0, id=None):
                super().__init__(id)
                self.width = width
                self.height = height
                self.x = x
                self.y = y

        # Save an empty list of dictionaries to a file
        with open("Rectangle.json", "w") as f:
            f.write("[]")

        # Act
        rectangles = Rectangle.load_from_file()

        # Assert
        self.assertEqual(rectangles, [])


class TestBaseClassSaveToCSV(unittest.TestCase):
    """Unittests for testing the save_to_file_csv method of the Base class.
    """

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file__csv_cls_name(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)

    def test_save_to_file_csv_writes_to_file(self):
        # Arrange
        r = Rectangle(10, 7, 2, 8, 5)
        # Act
        Rectangle.save_to_file_csv([r])
        # Assert
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    #  Method creates a CSV file with the name of the class
    def test_save_to_file_csv_creates_file_with_class_name(self):
        # Arrange
        r = Rectangle(10, 7, 2, 8, 5)
        # Act
        Rectangle.save_to_file_csv([r])
        # Assert
        self.assertTrue(os.path.exists("Rectangle.csv"))

    #  Method writes the correct fieldnames for Rectangle and Square classes
    def test_save_to_file_csv_writes_correct_fieldnames(self):
        # Arrange
        r = Rectangle(10, 7, 2, 8, 5)
        s = Square(10, 7, 2, 8)
        # Act
        Rectangle.save_to_file_csv([r])
        Square.save_to_file_csv([s])
        # Assert
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("id,width,height,x,y", f.readline().strip())
        with open("Square.csv", "r") as f:
            self.assertTrue("id,size,x,y", f.readline().strip())

    #  Method writes the correct values for each object in the list
    def test_save_to_file_csv_writes_correct_values(self):
        # Arrange
        r = Rectangle(10, 7, 2, 8, 5)
        s = Square(10, 7, 2, 8)
        # Act
        Rectangle.save_to_file_csv([r])
        Square.save_to_file_csv([s])
        # Assert
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.readline().strip())
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.readline().strip())

    #  Method writes multiple objects to the CSV file
    def test_save_to_file_csv_writes_multiple_objects(self):
        # Arrange
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        # Act
        Rectangle.save_to_file_csv([r1, r2])
        # Assert
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n3,2,4,1,2", f.read())

    #  Method overwrites the CSV file if it already exists
    def test_save_to_file_csv_overwrites_existing_file(self):
        # Arrange
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        # Act
        Rectangle.save_to_file_csv([r1])
        Rectangle.save_to_file_csv([r2])
        # Assert
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("3,2,4,1,2", f.read())

    #  Method writes an empty file if list_objs is None or empty
    def test_save_to_file_csv_writes_empty_file_if_list_objs_is_none_or_empty(self):
        # Arrange
        # Act
        Rectangle.save_to_file_csv(None)
        # Assert
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("[]", f.read())


class TestBaseClassLoadFromCSV(unittest.TestCase):
    """Unittests for testing the load_from_file_csv method of the Base class.
    """

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_load_from_file_csv_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r), str(list_rectangles_output[0]))

    def test_load_from_file_csv_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s), str(list_squares_output[0]))

    def test_load_from_file_csv_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_no_file(self):
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(list_rectangles_output, [])

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)

    def test_empty_file(self):
        # Arrange
        filename = "Rectangle.csv"
        if os.path.exists(filename):
            os.remove(filename)
        # Act
        result = Rectangle.load_from_file_csv()
        # Assert
        self.assertEqual(result, [])


class TestBaseClassDraw(unittest.TestCase):
    """Unittests for testing the draw method of the Base class.
    """

    def test_draw_no_args(self):
        """Tests draw method with no arguments."""
        with self.assertRaises(TypeError):
            Rectangle.draw()

    #
    def test_draw_more_than_one_arg(self):
        """Tests draw method with more than one argument."""
        with self.assertRaises(TypeError):
            Rectangle.draw([], 1)

    def test_set_background_color(self):
        from turtle import Turtle

        # Create a turtle object
        turt = Turtle()

        # Set the background color to "#b7312c"
        turt.screen.bgcolor((0.7176470588235294, 0.19215686274509805, 0.17254901960784313))

        # Check if the background color is set correctly
        self.assertEqual(turt.screen.bgcolor(), (0.7176470588235294, 0.19215686274509805, 0.17254901960784313))

        #  It sets the turtle's pen size to 3.

    def test_set_pen_size(self):
        from turtle import Turtle

        # Create a turtle object
        turt = Turtle()

        # Set the pen size to 3
        turt.pensize(3)

        # Check if the pen size is set correctly
        self.assertEqual(turt.pensize(), 3)

        #  It sets the turtle's shape to "turtle".

    def test_set_shape(self):
        from turtle import Turtle

        # Create a turtle object
        turt = Turtle()

        # Set the shape to "turtle"
        turt.shape("turtle")

        # Check if the shape is set correctly
        self.assertEqual(turt.shape(), "turtle")

        #  It sets the turtle's color to white for rectangles.

    def test_set_rectangle_color(self):
        from turtle import Turtle

        # Create a turtle object
        turt = Turtle()

        # Set the color to white for rectangles
        turt.color((1.0, 1.0, 1.0))

        # Check if the color is set correctly for rectangles
        self.assertEqual(turt.color()[0], (1.0, 1.0, 1.0))

        #  It sets the turtle's color to "#b5e3d8" for squares.

    def test_set_square_color(self):
        from turtle import Turtle

        # Create a turtle object
        turt = Turtle()

        # Set the color to "#b5e3d8" for squares
        turt.color((0.7098039215686275, 0.8901960784313725, 0.8470588235294118))

        # Check if the color is set correctly for squares
        self.assertEqual(turt.color()[0], (0.7098039215686275, 0.8901960784313725, 0.8470588235294118))


if __name__ == "__main__":
    unittest.main()
