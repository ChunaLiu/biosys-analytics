#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-04-03
Purpose: Rock the Casbah
"""

import os
import sys
import re


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 2:
        print('Usage: {} PASSWORD ALT'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    password = args[0]
    alt = args[1]

    pass_re_01 = re.compile(password)
    pass_re_02 = re.compile(password[0].upper() + password[1:])
    pass_re_03 = re.compile(password.upper())
    pass_re_04 = re.compile('.?' + password + '.?')

    match = pass_re_01.match(alt) or pass_re_02.match(alt) or pass_re_03.match(alt) or pass_re_04.match(alt)

    if match:
        print('ok')
    else: print('nah')








# --------------------------------------------------
main()
