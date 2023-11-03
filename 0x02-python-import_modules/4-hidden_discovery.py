#!/usr/bin/python3

import hidden_4


def main():
    """Main function"""
    for i in dir(hidden_4):
        if i[0] != '_':
            print("{}".format(i))


if __name__ == "__main__":
    # execute only if run as a script (not by 'import')
    main()
