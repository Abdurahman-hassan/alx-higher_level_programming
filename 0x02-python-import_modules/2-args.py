#!/usr/bin/python3
import sys


def main():
    """main function"""

    print("{} arguments".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    # execute only if run as a script (not by 'import')
    main()
