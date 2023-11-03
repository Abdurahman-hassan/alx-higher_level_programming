#!/usr/bin/python3

import sys


def main():
    """Main function"""
    argv = sys.argv
    argc = len(argv)
    sum = 0
    if argc > 1:
        for i in range(1, argc):
            sum += int(argv[i])
    print("{}".format(sum))


if __name__ == "__main__":
    # execute only if run as a script (not by 'import')
    main()
