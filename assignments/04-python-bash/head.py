#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-02-07
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]
    num_args = len(args)

    if not 1 <= num_args <= 2:
        print('Usage: {} FILE [NUM_LINES]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    file = args[0]
    num = args[1] if num_args == 2 else 3
    if not os.path.isfile(file):
        print('{} is not a file'.format(file))
        sys.exit(1)

    if not int(num) > 0:
        print('lines ({}) must be a positive number'.format(num))
        sys.exit(1)

    else:
        count = 0
        with open(file) as f:
            for line in f.readlines():
                if count < int(num):
                    count += 1
                    print(' {}'.format(line), end='')
                else: break




# --------------------------------------------------
main()
