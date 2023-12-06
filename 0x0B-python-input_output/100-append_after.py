#!/usr/bin/python3
""" append_after module """


def append_after(filename="", search_string="", new_string=""):
    """
        inserts a line of text to a file, after each line containing a
        specific string
        Args:
            filename (str): Name of the file.
            search_string (str): String to search
                in the file.
            new_string (str): String to insert
                after the search string.
    """
    with open(filename, mode="r+", encoding="utf-8") as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            if search_string in lines[i]:
                lines.insert(i + 1, new_string)
                i += 1
            i += 1
        f.seek(0)
        f.writelines(lines)
