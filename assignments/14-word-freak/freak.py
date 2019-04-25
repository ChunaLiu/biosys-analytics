#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-04-24
Purpose: Rock the Casbah
"""

import argparse
import sys
import re
from collections import defaultdict


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Print word frequencies',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', nargs='+', help='File input(s)', type=argparse.FileType('r', encoding='UTF-8'))

    parser.add_argument(
        '-s',
        '--sort',
        help='Sort by word or frequency',
        metavar='str',
        type=str,
        default='word')

    parser.add_argument(
        '-m',
        '--min',
        help='Minimum count',
        metavar='int',
        type=int,
        default=0)

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
    sort = args.sort
    min_frequency = args.min
    files = args.positional

    words = []
    for file in files:
        for char in file.read().split():
            words.append(char)

    clean_words = []
    for word in words:
        clean_words.append(re.sub('[^a-zA-Z0-9]', '', word).lower())

    words_count = defaultdict(int)
    for i in clean_words:
        if i != '':
            words_count[i] += 1

    output = {}
    if sort == 'word':
        for key, value in sorted(words_count.items()):
            if value >= min_frequency:
                output[key] = value
    else:
        pair = sorted([(x[1], x[0]) for x in words_count.items()])
        for num, w in pair:
            if num >= min_frequency:
                output[w] = num

    for c, n in output.items():
        print('{:20} {}'.format(c, n))



# --------------------------------------------------
if __name__ == '__main__':
    main()
