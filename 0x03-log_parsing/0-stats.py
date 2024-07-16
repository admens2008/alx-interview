#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Define a function to print statistics
def print_stats():
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

# Define signal handler for keyboard interruption
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Regular expression for parsing the log lines
log_pattern = re.compile(
    r'(\d{1,3}\.){3}\d{1,3} - \[\S+ \S+\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)'
)

try:
    for line in sys.stdin:
        line_count += 1

        # Match the line with the regular expression
        match = log_pattern.match(line)
        if match:
            status_code = int(match.group(2))
            file_size = int(match.group(3))

            # Update total file size
            total_file_size += file_size

            # Update status code count
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

# Final print of statistics after loop ends
print_stats()

