#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-04-14
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='De Bruijn Graphs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='str', help='FASTA FILE')

    parser.add_argument(
        '-k',
        '--overlap',
        help='k-mer',
        metavar='int',
        type=int,
        default=3)

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
def find_kmers(sequence, int_k):
    kmers = []
    len_sequence = len(sequence)
    for i in range(0, len_sequence - int_k + 1):
        kmer = sequence[i:i+int_k]
        if kmer not in kmers:
            kmers.append(kmer)
    return kmers


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    k = args.overlap
    fasta_file = args.positional

    if not os.path.isfile(fasta_file):
        die(msg='"{}" is not a file'.format(fasta_file))

    if k <= 0:
        die(msg='-k "{}" must be a positive integer'.format(k))

    fh = open(fasta_file, 'r')
    first_kmers = {}
    last_kmers = {}
    for rec in SeqIO.parse(fh, 'fasta'):
        first_kmer = str(rec.seq[0:k])
        last_kmer = str(rec.seq[-k:])
        if first_kmer not in first_kmers:
            first_kmers[rec.id] = first_kmer
        if last_kmer not in last_kmers:
            last_kmers[rec.id] = last_kmer
    for key_last in last_kmers.keys():
        for key_first in first_kmers.keys():
            if key_first != key_last and first_kmers[key_first] == last_kmers[key_last]:
                print(key_last, key_first)
                


# --------------------------------------------------
if __name__ == '__main__':
    main()
