#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-02-04
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    num = sys.argv[1:]
    if len(num) != 1:
        print('Usage: {} NUM'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    i = int(num[0])
    if not 2 <= i <=9:
        print('NUM ({}) must be between 1 and 9'.format(i))
        sys.exit(1)

    else:
        grid_list = list(range(1, i**2+1))
        grid = [grid_list[x:x+i] for x in range(0, len(grid_list), i)]
        # generate i*i matrix
        #method 1:
        for row in grid:
            print(''.join((' '*(3-len(str(item)))+str(item)) for item in row))
            # total length of each integer is 3
            #method 2:
            # for item in row:
            #     print('{:3}'.format(item), end='')
            # print()
			#method 3:
			#divde i == 0


# --------------------------------------------------
main()
