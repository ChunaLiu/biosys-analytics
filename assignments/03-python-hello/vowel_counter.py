#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-02-02
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    string = sys.argv[1:]

    if len(string) != 1:
        print('Usage: {} STRING'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    if len(string) > 0:
        count = 0
        vowels = "aeiouAEIOU"
        ss = string[0]
        for i in ss:
            if i in vowels:
                count += 1

    if count == 1:
        print('There is {} vowel in "{}."'.format(count, ss))
    else: print('There are {} vowels in "{}."'.format(count, ss))



# --------------------------------------------------
main()
