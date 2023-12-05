#!/usr/bin/python3
"""Module for read_file method."""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
