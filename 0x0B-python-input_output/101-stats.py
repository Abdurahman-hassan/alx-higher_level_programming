#!/usr/bin/python3

import sys
import signal


def signal_handler(sig, frame):
    """ Signal handler for CTRL+C

    Args:
        sig (int): Signal number.
        frame (frame): Current stack frame.
    """
    print_statistics()
    sys.exit(0)


def print_statistics():
    """ Print statistics
        Prints the total file size and the number
        of times each HTTP status code
        appears in the log.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Read from stdin
for line in sys.stdin:
    try:
        parts = line.split()
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Update statistics
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1

        # Every 10 lines, print statistics
        if line_count % 10 == 0:
            print_statistics()

    except Exception as e:
        # You can handle or print exceptions here if needed
        pass

# Print final statistics
print_statistics()
