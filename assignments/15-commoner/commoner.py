#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-04-25
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re
import logging
from tabulate import tabulate
import pandas as pd


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='Input files', nargs=2)

    parser.add_argument(
        '-m',
        '--min_len',
        help='Minimum length of words',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-n',
        '--hamming_distance',
        help='Allowed Hamming distance',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-l',
        '--logfile',
        help='Logfile name',
        metavar='str',
        type=str,
        default='.log')

    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true', default=False)

    parser.add_argument(
        '-t', '--table', help='Table output', action='store_true', default=False)

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
    min_word_len = args.min_len
    hamm_dist = args.hamming_distance
    logfile = args.logfile
    debug = args.debug
    output_table = args.table

    logging.basicConfig(
    filename=logfile,
    filemode='w',
    level=logging.DEBUG if debug else logging.CRITICAL
    )

    for file in files:
        if not os.path.isfile(file):
            die(msg='"{}" is not a file'.format(file))

    if hamm_dist < 0:
        die(msg='--distance "{}" must be > 0'.format(hamm_dist))

    f1 = open(files[0], 'r')
    f2 = open(files[1], 'r')
    logging.debug(msg='file1 = {}, file2 = {}'.format(files[0], files[1]))
    words1 = []
    words2 = []
    for content1 in f1:
        match_list1 = content1.split()
        for r1 in match_list1:
            r1 = re.sub('[^a-zA-Z0-9]', '', r1).lower()
            if len(r1) >= min_word_len:
                words1.append(r1)
    for content2 in f2:
        match_list2 = content2.split()
        for r2 in match_list2:
            r2 = re.sub('[^a-zA-Z0-9]', '', r2).lower()
            if len(r2) >= min_word_len:
                words2.append(r2)

    table_dict = {}
    table_dict['word1'] = []
    table_dict['word2'] = []
    table_dict['distance'] = []
    sum = 0
    for w1 in words1:
        for w2 in words2:
            d = dist(w1, w2)
            if d <= hamm_dist:
                table_dict['word1'].append(w1)
                table_dict['word2'].append(w2)
                table_dict['distance'].append(d)
                sum += 1
                logging.debug(msg='s1 = {}, s2 = {}, d = {}'.format(w1, w2, d))

    if sum == 0:
        print('No words in common.')

    else:

        df = pd.DataFrame(table_dict)
        df = df.drop_duplicates()
        df = df.sort_values(by=(['word1', 'word2']))
        df = df.set_index('word1')
        ascii_output = tabulate(df, headers='keys', tablefmt='psql')
        txt_output = df.to_csv(sep='\t')

        print(ascii_output if output_table else txt_output, end='')



# --------------------------------------------------
if __name__ == '__main__':
    main()
