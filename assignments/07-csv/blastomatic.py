#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-03-06
Purpose: Rock the Casbah
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='BLAST output (-outfmt 6)')

    parser.add_argument(
        '-a',
        '--annotations',
        help='Annotation file',
        metavar='FILE',
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
        type=str,
        default='')

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
    annotation_file = args.annotations
    outfile = args.outfile
    BLAST_file = args.positional

    if not os.path.isfile(BLAST_file):
        die(msg='"{}" is not a file'.format(BLAST_file))

    if not os.path.isfile(annotation_file):
        die(msg='"{}" is not a file'.format(annotation_file))

    annotation = {}
    with open(annotation_file, 'rt') as f:
        for row in f.readlines():
            rec = row.split(',')
            centroid = rec[0]
            genus = rec[6]
            species = rec[7].rstrip()
            annotation[centroid] = [genus, species]

    out_fh = open(outfile, 'a') if outfile else sys.stdout
    fields = '\t'.join(['seq_id', 'pident', 'genus', 'species'])
    out_fh.write(fields + '\n')
    with open(BLAST_file) as hitfile:
        for line in hitfile:
            sseqid = line.split()[1]
            pident = line.split()[2]

            if sseqid in annotation.keys():
                genus_hit = annotation[sseqid][0] if annotation[sseqid][0] else 'NA'
                species_hit = annotation[sseqid][1] if annotation[sseqid][1] else 'NA'
                hits = '\t'.join([sseqid, pident, genus_hit, species_hit])
                out_fh.write(hits + '\n')

            else:
                sys.stderr.write('Cannot find seq "{}" in lookup\n'.format(sseqid))

    out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
