#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-02-21
Purpose: Rock the Casbah
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='DIR', help='A positional argument', nargs='+')
        #nargs='+' is to get a list instead of a single value

    parser.add_argument(
        '-w',
        '--width',
        help='A named integer argument',
        metavar='int',
        type=int,
        default=50)

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
    input = args.positional
    space_width = args.width
    for i in input:
        if not os.path.isdir(i):
            warn(msg='"{}" is not a directory'.format(i))

        else:
            print(i)
            output = {}
            for filename in os.listdir(i):
                with open(os.path.join(i, filename)) as file:
                    first_line = file.readlines()[0].rstrip()
                    dots = '.' * (space_width - len(first_line) - len(filename)) # two blank spaces, should minus 2
                    output.setdefault(filename, []).append(first_line + ' ' + dots + ' ' + filename)
                    #filename as key for each first line
                    # output[filename] = first_line + ' ' + dots + ' ' + filename
            pairs = sorted([(x[1], x[0]) for x in output.items()])
            for line, name in pairs:
                print('{}'.format(line[0]))



# --------------------------------------------------
if __name__ == '__main__':
    main()
