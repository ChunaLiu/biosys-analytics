#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-02-17
Purpose: Rock the Casbah
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='STR', help='DNA/RNA sequence')

    parser.add_argument(
        '-c',
        '--codons',
        help='A file with codon translations',
        required=True,
        metavar='FILE',
        type=str,
        default=None)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output filename',
        metavar='FILE',
        type=str,
        default='out.txt')

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
    sequences = args.positional.upper()
    codons_table = args.codons
    output = args.outfile

    if not os.path.isfile(codons_table):
        die(msg='--codons "{}" is not a file'.format(codons_table))

    codons_dict = {}
    # with open(codons_table) as f:
    #     for line in f:
    #         # print(line)
    #         [aa, codons] = line.split()
    #         codons_dict[aa] = codons.split()
            # print(codons_dict)
    with open(codons_table) as f:
        for row in f:
            keys = row[0:3]
            codons_dict[keys] = row[4:(len(row) - 1)]

    k = 3
    n = len(sequences) - k + 1
    for i in range(0, n, k):
        codons = sequences[i:i+k]
        print(codons_dict[codons] if codons in codons_dict else '-', end='', file=open(output, 'a'))
    print('Output written to "{}"'.format(output))



# --------------------------------------------------
if __name__ == '__main__':
    main()
