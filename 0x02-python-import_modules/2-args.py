#!/usr/bin/python3
import sys


def main():
    """main function"""
    num_of_args = len(sys.argv) - 1

    if num_of_args == 0:
        print("{} arguments.".format(num_of_args))
    elif num_of_args == 1:
        print("{} argument:".format(num_of_args))
        print("{}: {}".format(num_of_args, sys.argv[1]))
    else:
        print("{} arguments:".format(num_of_args))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    # execute only if run as a script (not by 'import')
    main()
