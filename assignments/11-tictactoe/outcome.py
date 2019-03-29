#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-03-28
Purpose: Rock the Casbah
"""

import os
import sys
import re


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} STATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    state = args[0]
    if not re.search('^[.XO]{9}$', state):
        print('State "{}" must be 9 characters of only ., X, O'.format(state))
        sys.exit(0)

    state_re_X1 = re.compile('([X]{3})'
                             '[.XO]{6}')

    state_re_X2 = re.compile('[.XO]{3}'
                             '([X]{3})'
                             '[.XO]{3}')

    state_re_X3 = re.compile('[.XO]{6}'
                             '([X]{3})')

    state_re_X4 = re.compile('([X]{1})'
                             '[.XO]{2}'
                             '([X]{1})'
                             '[.XO]{2}'
                             '([X]{1})'
                             '[.XO]{2}')

    state_re_X5 = re.compile('[.XO]{1}'
                             '([X]{1})'
                             '[.XO]{2}'
                             '([X]{1})'
                             '[.XO]{2}'
                             '([X]{1})'
                             '[.XO]{1}')

    state_re_X6 = re.compile('[.XO]{2}'
                             '([X]{1})'
                             '[.XO]{2}'
                             '([X]{1})'
                             '[.XO]{2}'
                             '([X]{1})')

    state_re_X7 = re.compile('([X]{1})'
                             '[.XO]{3}'
                             '([X]{1})'
                             '[.XO]{3}'
                             '([X]{1})')

    state_re_X8 = re.compile('[.XO]{2}'
                             '([X]{1})'
                             '[.XO]{1}'
                             '([X]{1})'
                             '[.XO]{1}'
                             '([X]{1})'
                             '[.XO]{2}')

    state_re_O1 = re.compile('([O]{3})'
                             '[.XO]{6}')

    state_re_O2 = re.compile('[.XO]{3}'
                             '([O]{3})'
                             '[.XO]{3}')

    state_re_O3 = re.compile('[.XO]{6}'
                             '([O]{3})')

    state_re_O4 = re.compile('([O]{1})'
                             '[.XO]{2}'
                             '([O]{1})'
                             '[.XO]{2}'
                             '([O]{1})'
                             '[.XO]{2}')

    state_re_O5 = re.compile('[.XO]{1}'
                             '([O]{1})'
                             '[.XO]{2}'
                             '([O]{1})'
                             '[.XO]{2}'
                             '([O]{1})'
                             '[.XO]{1}')

    state_re_O6 = re.compile('[.XO]{2}'
                             '([O]{1})'
                             '[.XO]{2}'
                             '([O]{1})'
                             '[.XO]{2}'
                             '([O]{1})')

    state_re_O7 = re.compile('([O]{1})'
                             '[.XO]{3}'
                             '([O]{1})'
                             '[.XO]{3}'
                             '([O]{1})')

    state_re_O8 = re.compile('[.XO]{2}'
                             '([O]{1})'
                             '[.XO]{1}'
                             '([O]{1})'
                             '[.XO]{1}'
                             '([O]{1})'
                             '[.XO]{2}')

    match_X = state_re_X1.match(state) or state_re_X2.match(state) or state_re_X3.match(state) or state_re_X4.match(state) or \
              state_re_X5.match(state) or state_re_X6.match(state) or state_re_X7.match(state) or state_re_X8.match(state)
    match_O = state_re_O1.match(state) or state_re_O2.match(state) or state_re_O3.match(state) or state_re_O4.match(state) or \
              state_re_O5.match(state) or state_re_O6.match(state) or state_re_O7.match(state) or state_re_O8.match(state)

    if match_X:
        print('X has won')

    elif match_O:
        print('O has won')

    else:
        print('No winner')

    #original
    # board = [list(state)[x:x+3] for x in range(0, 9, 3)]
    # winner = []
    # if board[0][2] == board[1][1] == board[2][0] != '.':
    #     winner = board[0][2]
    # if board[0][0] == board[1][1] == board[2][2] != '.':
    #     winner = board[0][0]
    # for i, row in enumerate(board):
    #     if row[0] == row[1] == row[2] != '.':
    #         winner = row[0]
    #     if board[0][i] == board[1][i] == board[2][i] != '.':
    #         winner = board[0][i]
    # if len(winner) == 1:
    #     print('{} has won'.format(winner))
    # else:print('No winner')


# --------------------------------------------------
main()
