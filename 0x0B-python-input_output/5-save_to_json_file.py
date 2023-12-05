#!/usr/bin/python3
"""Module for save_to_json_file function"""

import json


def save_to_json_file(my_obj, filename):
    """
        Writes an Object to a text file, using a JSON representation
        Args:
            my_obj (object): Object to write to file
            filename (str): Name of file to write to

        Returns:
            Nothing
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
