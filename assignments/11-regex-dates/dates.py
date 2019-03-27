#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-03-26
Purpose: Rock the Casbah
"""

import os
import sys
import re

# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} DATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    date = args[0]
    month_s_value = {}
    month_l_value = {}
    month_short = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
    month_long = 'January February March April May June July August September October November December'.split()
    for i in range(0, 12):
        month_s_value[month_short[i]] = '0' + str(i + 1) if len(str(i + 1)) == 1 else str(i + 1)
        month_l_value[month_long[i]] = '0' + str(i + 1) if len(str(i + 1)) == 1 else str(i + 1)

    date_re_01 = re.compile('(\d{4})'
                            '[-]'
                            '(\d{1,})'
                            '[-]'
                            '(\d{1,})')

    date_re_02 = re.compile('(\d{4})'
                            '(\d{2})'
                            '(\d{2})')

    date_re_03 = re.compile('(\d{4})'
                            '[-]'
                            '(\d{1,})')

    date_re_04 = re.compile('(\d{1,})'
                            '[/]'
                            '(\d{2})')

    date_re_05 = re.compile('(\D{3})'
                            '[-]'
                            '(\d{4})')

    date_re_06 = re.compile('(\D{3})'
                            '[,]'
                            '[ ]'
                            '(\d{4})')

    date_re_07 = re.compile('(\D{4,})'
                            '[-]'
                            '(\d{4})')

    date_re_08 = re.compile('(\D{4,})'
                            '[,]'
                            '[ ]'
                            '(\d{4})')

    match1 = date_re_01.match(date) or date_re_02.match(date)
    match2 = date_re_03.match(date)
    match3 = date_re_04.match(date)
    match4 = date_re_05.match(date) or date_re_06.match(date) or date_re_07.match(date) or date_re_08.match(date)

    if match1:
        standard = '{}-{}-{}'.format(match1.group(1), match1.group(2).zfill(2), match1.group(3).zfill(2))

    elif match2:
        standard = '{}-{}-01'.format(match2.group(1), match2.group(2).zfill(2))

    elif match3:
        standard = '20{}-{}-01'.format(match3.group(2), (match3.group(1)).zfill(2))

    elif match4:
        if len(match4.group(1)) < 4:
            group_month = month_s_value[match4.group(1)]
        else:
            group_month = month_l_value[match4.group(1)]
        standard = '{}-{}-01'.format(match4.group(2), group_month)

    else: standard = 'No match'

    print('{}'.format(standard))


# --------------------------------------------------
main()
