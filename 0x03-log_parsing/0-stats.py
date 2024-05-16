#!/usr/bin/python3

import sys
import signal
import re

# Global variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
lines_processed = 0


def print_stats():
    """Print statistics."""
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))


def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)


def process_line(line):
    """Process each line."""
    global total_size, lines_processed

    # Regular expression to match the input format
    pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[.*\] "GET \/projects\/260 HTTP\/1.1" (\d{3}) (\d+)$'

    match = re.match(pattern, line)
    if match:
        file_size = int(match.group(3))
        status_code = int(match.group(2))

        # Update total size
        total_size += file_size

        # Update status code count
        if status_code in status_codes:
            status_codes[status_code] += 1

        lines_processed += 1

        # Print stats after every 10 lines
        if lines_processed % 10 == 0:
            print_stats()


def main():
    """Main function."""
    # Register signal handler for keyboard interruption
    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            process_line(line.strip())
    except KeyboardInterrupt:
        print_stats()
        sys.exit(0)


if __name__ == "__main__":
    main()
