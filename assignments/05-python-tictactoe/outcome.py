#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-02-20
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
        #import re and search pattern

    board = [list(state)[x:x+3] for x in range(0, 9, 3)]
    winner = []
    if board[0][2] == board[1][1] == board[2][0] != '.':
        winner = board[0][2]
    if board[0][0] == board[1][1] == board[2][2] != '.':
        winner = board[0][0]
    for i, row in enumerate(board):
        if row[0] == row[1] == row[2] != '.':
            winner = row[0]
        if board[0][i] == board[1][i] == board[2][i] != '.':
            winner = board[0][i]
    if len(winner) == 1:
        print('{} has won'.format(winner))
    else:print('No winner')


# --------------------------------------------------
main()
