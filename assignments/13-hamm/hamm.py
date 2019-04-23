#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-04-12
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import logging


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='File inputs', nargs=2)

    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true', default=False)

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
def dist(s1, s2):
    count = 0
    max_len = max(len(s1), len(s2))
    min_len = min(len(s1), len(s2))
    count += (max_len - min_len)
    if s1 != s2:
        for j in range(0, min_len):
            if s1[j] != s2[j]:
                count +=1
    return count


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    files = args.positional
    debug = args.debug

    logging.basicConfig(
    filename='.log',
    filemode='w',
    level=logging.DEBUG if debug else logging.CRITICAL
    )

    for i in files:
        if not os.path.isfile(i):
            die(msg='"{}" is not a file'.format(i))

    f1 = open(files[0], 'r')
    f2 = open(files[1], 'r')
    logging.debug(msg='file1 = {}, file2 = {}'.format(files[0], files[1]))
    words1 = []
    words2 = []

    for content1 in f1:
        match_list1 = content1.split()
        for r1 in match_list1:
            words1.append(r1)
    for content2 in f2:
        match_list2 = content2.split()
        for r2 in match_list2:
            words2.append(r2)

    pairs = zip(words1, words2)
    sum = 0
    for word1, word2 in pairs:
        d = dist(word1, word2)
        sum += d
        logging.debug(msg='s1 = {}, s2 = {}, d = {}'.format(word1, word2, d))
    print(sum)


# --------------------------------------------------
if __name__ == '__main__':
    main()
