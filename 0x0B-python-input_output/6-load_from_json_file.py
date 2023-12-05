#!/usr/bin/python3
"""Defines a function that creates an Object from a JSON file"""

import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file

    Args:
        filename (str): name of JSON file

    Returns:
        object: Python object created
    """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
