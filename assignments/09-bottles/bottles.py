#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-03-13
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-n',
        '--num_bottles',
        help='How many bottles',
        metavar='INT',
        type=int,
        default=10)

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
    num_bottles = args.num_bottles

    if num_bottles < 1:
        die(msg='N () must be a positive integer')

    for i in range(1, num_bottles + 1):



        print('\n'.join(['{} bottle{} of beer on the wall,'.format(num_bottles - i + 1, 's' if (num_bottles - i + 1) != 1 else ''),
                         '{} bottle{} of beer,'.format(num_bottles - i + 1, 's' if (num_bottles - i + 1) != 1 else ''),
                         'Take one down, pass it around,',
                         '{} bottle{} of beer on the wall!'.format(num_bottles - i, 's' if (num_bottles - i) != 1 else '')]))

        print('') if i < num_bottles else None


# --------------------------------------------------
if __name__ == '__main__':
    main()
