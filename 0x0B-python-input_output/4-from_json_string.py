#!/usr/bin/python3
"""Module for JSON string function"""

import json


def from_json_string(my_str):
    """
    Function that returns
        an object (Python data structure)
        represented by a JSON string

    Args:
        my_str (str): JSON string to be converted to object

    Returns:
        object (Python data structure) represented by a JSON string
        """
    return json.loads(my_str)
