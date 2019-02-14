#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-02-07
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe board',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--state',
        help='Board state',
        metavar='str',
        type=str,
        default='.........')

    parser.add_argument(
        '-p',
        '--player',
        help='Player',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-c',
        '--cell',
        help='Cell to apply -p',
        metavar='str',
        type=int,
        default=None)

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
    state = args.state
    player = args.player
    cell = args.cell
    grid_list = list(range(1, 10))
    grid = [grid_list[x:x+3] for x in range(0, 9, 3)]

    if len(sys.argv) == 1:
        print('-'*13)
        for row in grid:
            print('|', row[0], '|', row[1], '|', row[2], '|')
            print('-'*13)
        sys.exit(0)

    state_char = '.-XO'
    for char in state:
        if state != '.........' and (len(state) != 9 or (char not in state_char)):
            print(die(msg='Invalid state "{}", must be 9 characters of only -, X, O'.format(state)))

    player_char = 'XO'
    if player not in player_char:
        print(die(msg='Invalid player "{}", must be X or O'.format(player)))

    if cell is not None and not 1 <= cell <= 9:
        print(die(msg='Invalid cell "{}", must be 1-9'.format(cell)))

    if (any([cell, player]) and not all([cell, player])) is True:
            print('Must provide both --player and --cell')
            sys.exit(1)

    state_list = list(state)
    for ii, cc in enumerate(state_list):
        if cc is '.':
            state_list[ii] = str(ii + 1)
        if cell is not None and len(player) > 0:
            if state[int(cell - 1)] in player_char:
                print(die(msg='Cell {} already taken'.format(cell)))
            else:
                state_list[int(cell - 1)] = player
    state_grid = [state_list[x:x+3] for x in range (0, 9, 3)]
    print('-'*13)
    for r in state_grid:
            print('|', r[0], '|', r[1], '|', r[2], '|')
            print('-'*13)


# --------------------------------------------------
if __name__ == '__main__':
    main()
