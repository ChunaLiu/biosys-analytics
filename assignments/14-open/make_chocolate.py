#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-04-19
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Make Chocolate',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'small', metavar='int', type=int, help='the number of small bars')

    parser.add_argument(
        'big', metavar='int', type=int, help='the number of big bars')

    parser.add_argument(
        'goal', metavar='int', type=int, help='the number of goal kilos')

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
    small = args.small
    big = args.big
    goal = args.goal

    big_use = goal//5
    if big >= big_use:
      small_use = goal - 5 * big_use
    else:
      small_use = goal - 5 * big

    if small >= small_use:
        print(small_use)
    else:
        print('The goal chocolate cannot be done')


# --------------------------------------------------
if __name__ == '__main__':
    main()
