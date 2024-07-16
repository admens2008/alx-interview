#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''

import sys
import signal

# Initialize variables
cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

# Function to print the statistics
def print_stats():
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))

# Signal handler for keyboard interruption
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            try:
                size = int(line_list[-1])
                total_size += size
            except ValueError:
                continue

            if code in cache.keys():
                cache[code] += 1
            counter += 1

        if counter == 10:
            print_stats()
            counter = 0

except Exception as err:
    pass

finally:
    print_stats()

