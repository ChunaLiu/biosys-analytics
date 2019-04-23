#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-03-17
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
from Bio import SwissProt
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Filter Swissprot file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='Uniprot file')

    parser.add_argument(
        '-s',
        '--skip',
        help='Skip taxa',
        metavar='STR [STR ...]',
        type=str,
        nargs='+',
        default='')

    parser.add_argument(
        '-k',
        '--keyword',
        help='Take on keyword',
        metavar='STR',
        type=str,
        required=True,
        default=None)

    parser.add_argument(
        '-o',
        '--output',
        help='Output filename',
        metavar='FILE',
        default='out.fa')

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
    skip = args.skip
    keyword = args.keyword.lower()
    output = args.output
    swiss_file = args.positional
    skip_words = set([word.lower() for word in skip])
    key_word = set([keyword])

    if not os.path.isfile(swiss_file):
        die(msg='"{}" is not a file'.format(swiss_file))

    print('Processing "{}"'.format(swiss_file))

    with open(swiss_file) as fh:
        records = SwissProt.parse(fh)
        count = 0
        match = 0
        match_id = []
        for seq_record in records:
            count += 1
            taxa_skip = set([i.lower() for i in seq_record.organism_classification])
            taxa_keyword = set([j.lower() for j in seq_record.keywords])
            if not taxa_skip.intersection(skip_words) and key_word.intersection(taxa_keyword):
                match += 1
                match_id.append(seq_record.accessions[0])

    with open(output, 'a') as o:
        for r in SeqIO.parse(swiss_file, 'swiss'):
            #r.annotations is a dictionary including keys and values for each record
            if r.id in match_id:
                SeqIO.write(r, o, 'fasta')

    print('Done, skipped {} and took {}. See output in "{}".'.format(count - match, match, output))


# --------------------------------------------------
if __name__ == '__main__':
    main()
