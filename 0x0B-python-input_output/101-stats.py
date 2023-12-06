#!/usr/bin/python3

import signal
import sys


def signal_handler(sig, frame):
    """ Signal handler for CTRL+C

        Args:
            sig (int): Signal number
            frame (frame): Current stack frame
     """
    print_stats(total_size, status_codes)
    sys.exit(0)


def print_stats(total_size, status_codes):
    """ Print statistics

        Args:
            total_size (int): Total size of the file
            status_codes (dict): Dictionary of status codes
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Initialize variables
total_size = 0
status_codes = {}
line_count = 0
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

# Read from stdin
try:
    for line in sys.stdin:
        if line_count == 10:
            print_stats(total_size, status_codes)
            line_count = 1
        else:
            line_count += 1

        data = line.split()

        try:
            total_size += int(data[-1])
        except (ValueError, IndexError):
            pass

        try:
            status_code = data[-2]
            if status_code in valid_codes:
                status_codes[status_code] = status_codes.get(
                    status_code, 0) + 1
        except IndexError:
            pass

    print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise
