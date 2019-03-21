#!/usr/bin/env python3
"""
Author : chunanliu
Date   : 2019-03-19
Purpose: Rock the Casbah
"""

import argparse
import sys
import random
from itertools import product


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='"War" cardgame',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
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
    seed = args.seed
    suites = list('♥♠♣♦')
    num = list(str (j) for j in range(2, 11))
    char = list('JQKA')
    deck = list(product(suites, num + char))

    card_value = {}
    value = 2
    for i in deck[0:13]:
        card_value[i[1]] = value
        value += 1

    deck = sorted(deck)

    if seed is not None:
        random.seed(seed)
        random.shuffle(deck)

    P1_win = 0
    P2_win = 0
    for i in range(0, 26):
        P1_card = deck.pop()
        P2_card = deck.pop()
        card_num_P1 = card_value[P1_card[1]]
        card_num_P2 = card_value[P2_card[1]]

        if card_num_P1 > card_num_P2:
            P1_win += 1
            winner = 'P1'

        elif card_num_P1 < card_num_P2:
            P2_win += 1
            winner = 'P2'

        else: winner = 'WAR!'

        print('{:>3} {:>3} {}'.format(P1_card[0] + P1_card[1], P2_card[0] + P2_card[1], winner))


    if P1_win != P2_win:
        print('P1 {} P2 {}: Player {} wins'.format(P1_win, P2_win, '1' if P1_win > P2_win else '2'))

    else:
        print('P1 {} P2 {}: DRAW'.format(P1_win, P2_win))


# --------------------------------------------------
if __name__ == '__main__':
    main()
