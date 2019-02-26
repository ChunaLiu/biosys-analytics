#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-02-25
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
        description='Segregate FASTA sequences by GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FASTA', help='Input FASTA file(s)', nargs='+')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='DIR',
        type=str,
        default='out')

    parser.add_argument(
        '-p',
        '--pct_gc',
        help='Dividing line for percent GC',
        metavar='int',
        type=int,
        # choices=range(1, 101),
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
    dirname = args.outdir
    pct_gc = args.pct_gc

    if pct_gc and pct_gc not in range(1, 101):
        print('--pct_gc "{}" must be between 0 and 100'.format(pct_gc))
        sys.exit(1)

    if not os.path.isdir(dirname):
        os.makedirs(dirname)

    file_index = 0
    num_total_sequences = 0
    for file in input:
        if not os.path.isfile(file):
            warn(msg='"{}" is not a file'.format(file))

        else:
            num_sequences = 0
            file_index += 1
            print('{}: {}'.format((file_index), file))

            # with open(file) as fasta: no need to open when use SeqIO
            basename = os.path.basename(file)
            highout_name = os.path.splitext(basename)[0] + '_' + 'high' + os.path.splitext(basename)[1]
            lowout_name = os.path.splitext(basename)[0] + '_' + 'low' + os.path.splitext(basename)[1]
            high_sequences = []
            low_sequences = []
            for seq_record in SeqIO.parse(file, 'fasta'):
                num_sequences += 1
                count_gc = 0
                for char in seq_record.seq:
                    if char in 'GC':
                        count_gc += 1
                gc_content = int((count_gc/len(seq_record)) * 100)
                if gc_content >= pct_gc:
                    high_sequences.append(seq_record)
                    SeqIO.write(high_sequences, os.path.join(dirname, highout_name), "fasta")

                else:
                    low_sequences.append(seq_record)
                    SeqIO.write(low_sequences, os.path.join(dirname, lowout_name), "fasta")

                    #import Counter
                    #nucs = Counter(ecord.seq)
                    #seq_len = len(record.seq)
                    #gc_num = nucs.get('G', 0) + nucs.get('C', 0)
                    #gc = int((gc_num/seq_len) *100)

            num_total_sequences += num_sequences
    print('Done, wrote {} sequences to out dir "{}"'.format(num_total_sequences, dirname))



# --------------------------------------------------
if __name__ == '__main__':
    main()
