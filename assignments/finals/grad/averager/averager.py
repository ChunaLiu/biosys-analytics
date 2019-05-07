#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-05-07
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Average all the numbers in a document',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='Input file(s)', nargs='+')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    files = args.positional

    for file in files:
        if not os.path.isfile(file):
            warn(msg='"{}" is not a file'.format(file))

        else:
            num_count = 0
            sum = 0
            fh = open(file)
            for line in fh:
                for i in line.split():
                    nums = re.compile(r"[+-]?\d+(?:\.\d+)?")
                    if nums.search(i):
                        number = nums.search(i).group(0)
                        number = float(number)
                        sum += number
                        num_count +=1
            if num_count == 0:
                avg = 0
            else:
                avg =  sum/num_count
            print('{:10.02f}: {}'.format(avg, os.path.basename(file)))



# --------------------------------------------------
if __name__ == '__main__':
    main()
