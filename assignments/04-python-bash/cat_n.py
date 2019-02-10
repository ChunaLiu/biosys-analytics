#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-02-07
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    file = args[0]
    if not os.path.isfile(file):
        print('{} is not a file'.format(file))
        sys.exit(1)

    else:
        count = 0
        with open(file) as f:
            for line in f.readlines():
                count += 1
                print(' {:3}: {}'.format(count, line), end='')



# --------------------------------------------------
main()
