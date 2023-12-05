#!/usr/bin/python3
"""Module for JSON string function"""

import json


def to_json_string(my_obj):
    """
    Function that returns
        the JSON representation of an object (string)

    Args:
        my_obj (object): object to be converted to JSON string

    Returns:
        JSON representation of an object (string)
        """
    return json.dumps(my_obj)
