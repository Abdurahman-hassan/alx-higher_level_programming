#!/usr/bin/python3

from add_0 import add


def main():
    """Main function"""
    a = 1
    b = 2

    print("{} + {} = {}".format(a, b, add(a, b)))


if __name__ == "__main__":
    # execute only if run as a script (not by 'import')
    main()
