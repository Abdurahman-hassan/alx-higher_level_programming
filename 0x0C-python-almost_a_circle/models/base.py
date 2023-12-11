#!/usr/bin/python3
"""Defines a base class for all other classes in this project."""

import csv
import turtle
import json


class Base:
    """
        Base class for all other classes in this project
        Attributes:
            __nb_objects (int): The number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initialize a new Base object
            Args:
                id (int): The identity of the new Base instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Return the JSON serialization of a list of dicts
            Args:
                list_dictionaries (list): A list of dictionaries.
        """
        import json
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Write the JSON serialization of a list of objects to a file
            Args:
                list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jf:
            if list_objs is None:
                jf.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jf.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
            Return the deserialization of a JSON string
            Args:
                json_string (str):
                A JSON str representation of a list of dicts.

            Returns:
                If json_string is None or empty - an empty list.
                Otherwise - the Python list represented by json_string
        """
        import json
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Return an instance with all attributes already set
            Args:
                **dictionary (dict): Key/value pairs of attributes to initialize
                    an instance with.

            Returns:
                A instance of the class with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
            Return a list of classes instantiated from a file of JSON strings
            Reads from `<cls.__name__>.json`
            Returns:
                If the file does not exist - an empty list.
                Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jf:
                list_dicts = cls.from_json_string(jf.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a file of CSV strings.

        Reads from `<cls.__name__>.csv`

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([key, int(value)]
                                   for key, value in row.items())
                              for row in reader]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        import turtle
        import random

        t = turtle.Turtle()
        t.screen.bgcolor("#b7312c")
        t.pensize(3)
        t.shape("turtle")
        t.color("#ffffff")
        t.speed(0)
        for r in list_rectangles + list_squares:
            t.penup()
            t.setpos(r.x, r.y)
            t.pendown()
            t.fillcolor("#{:06x}".format(random.randint(0, 0xFFFFFF)))
            t.begin_fill()
            for i in range(2):
                t.forward(r.width)
                t.left(90)
                t.forward(r.height if type(r) is Rectangle else r.size)
                t.left(90)
            t.end_fill()
        t.hideturtle()
        turtle.exitonclick()
