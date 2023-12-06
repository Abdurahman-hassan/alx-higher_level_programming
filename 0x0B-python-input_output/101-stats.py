#!/usr/bin/python3

import signal
import sys


def signal_handler(sig, frame):
    """ Signal handler for CTRL+C """
    print_statistics()
    sys.exit(0)


def print_statistics():
    """ Print statistics """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if code in valid_codes:
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
            print_statistics()
            line_count = 0

        line_count += 1

        try:
            parts = line.split()
            status_code = str(int(parts[-2]))  # Ensure it's a valid integer then convert to string
            file_size = int(parts[-1])

            # Update statistics
            total_size += file_size
            if status_code in valid_codes:
                status_codes[status_code] = status_codes.get(status_code, 0) + 1

        except (ValueError, IndexError):
            pass

    print_statistics()

except KeyboardInterrupt:
    print_statistics()
    raise
