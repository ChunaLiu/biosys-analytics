#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-04-05
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find unclustered proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-c',
        '--cdhit',
        help='Output file from CD-HIT (clustered proteins)',
        metavar='str',
        type=str,
        default=None,
        required=True)

    parser.add_argument(
        '-p',
        '--proteins',
        help='Proteins FASTA',
        metavar='str',
        type=str,
        default=None,
        required=True)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='str',
        type=str,
        default='unclustered.fa')

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
    cdhit = args.cdhit
    proteins = args.proteins
    outfile = args.outfile
    c_ids = []
    count_p = 0
    count_unclustered = 0
    p_ids = []

    if not os.path.isfile(proteins):
        die(msg='--proteins "{}" is not a file'.format(proteins))

    if not os.path.isfile(cdhit):
        die(msg='--cdhit "{}" is not a file'.format(cdhit))

    with open(cdhit, 'r') as c:
        for r in c:
            if re.search('>gi\|(\d+)', r):
                m1 = re.search('>gi\|(\d+)', r)
                c_id = m1.group(1)
                c_ids.append(c_id)

    unclustered_fh = open(outfile, 'wt')
    with open(proteins, 'r') as p:
        for protein_record in SeqIO.parse(p, 'fasta'):
            count_p += 1
            m2 = re.search('(\d+)', protein_record.id)
            p_id = m2.group(1)

            if p_id not in c_ids:
                count_unclustered += 1
                SeqIO.write(protein_record, unclustered_fh, "fasta")

        print('Wrote {:,} of {:,} unclustered proteins to "{}"'.format(count_unclustered, count_p, outfile))


    #         p_ids.append(p_id)
    #         print(full_id)
    #
    # c_ids = set(c_ids)
    # p_ids = set(p_ids)
    # unclustered_ids = p_ids.difference(c_ids)
    # for unclustered_id in unclustered_ids:
    #     if re.search(unclustered_id, )
    #
    # for e in unclustered_ids:
    #     print(e)





            # print(protein_record.id)

            # print(r)
            # re.sub('>gi\|')
            # print(re.search('>gi\|\d+', r))






# --------------------------------------------------
if __name__ == '__main__':
    main()
